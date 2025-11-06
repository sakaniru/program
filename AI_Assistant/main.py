import sys, os, threading, queue
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QSystemTrayIcon, QMenu, QAction, QTextEdit, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PIL import Image
import pyttsx3
import keyboard
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from torch import float16
import re

# --- HF 模型設定 ---
os.environ["HF_HOME"] = "E:/hf_cache"

model_name = "Qwen/Qwen2.5-1.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",    # 自動選擇最佳精度（float16 或 bfloat16）
    device_map="auto"      # 自動分配 GPU / CPU
)

model.config.pad_token_id = tokenizer.eos_token_id

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    truncation=True,
    temperature=0.7,
    top_k=30,
    top_p=0.95,
)

# --- 路徑設定 ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
character_path = os.path.join(BASE_DIR, "assets/character/assistant.png")
tray_path = os.path.join(BASE_DIR, "assets/icons/tray.png")

if not os.path.exists(character_path):
    raise FileNotFoundError(f"找不到角色圖: {character_path}")

os.makedirs(os.path.dirname(tray_path), exist_ok=True)
img = Image.open(character_path)
img_small = img.resize((32, 32), Image.Resampling.LANCZOS)
img_small.save(tray_path)

# --- 對話視窗 ---
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI 助理對話")
        self.setGeometry(100, 100, 400, 400)

        # --- 聊天視窗元件 ---
        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("輸入訊息...")
        self.send_button = QPushButton("送出")
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_box)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        # --- 對話歷史 ---
        self.chat_history_list = []
        self.max_history = 10

        # --- TTS ---
        self.tts_queue = queue.Queue()
        self.tts_engine = pyttsx3.init()
        self.tts_thread = threading.Thread(target=self._tts_worker, daemon=True)
        self.tts_thread.start()

    def send_message(self):
        user_text = self.input_box.text().strip()
        if not user_text:
            return
        self.chat_box.append(f"🧑 你: {user_text}")
        self.input_box.clear()
        response = self.ai_response(user_text)
        self.chat_box.append(f"🤖 助理: {response}\n")
        self.tts_queue.put(response)

    def _tts_worker(self):
        voices = self.tts_engine.getProperty('voices')
        default_voice = voices[0].id if voices else None
        chinese_voice_id = next((v.id for v in voices if 'zh' in str(v.languages[0])), default_voice)
        english_voice_id = next((v.id for v in voices if 'en' in str(v.languages[0])), default_voice)

        while True:
            text = self.tts_queue.get()
            if text is None:
                break

            # 拆段但不要過度切
            segments = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z0-9\s.,!?;:]+', text)

            for seg in segments:
                if not seg.strip():
                    continue

                try:
                    # 判斷中英文，切換語音
                    if any(u'\u4e00' <= c <= u'\u9fff' for c in seg):
                        self.tts_engine.setProperty('voice', chinese_voice_id)
                    else:
                        self.tts_engine.setProperty('voice', english_voice_id)

                    # 只在播放前 stop 已在播放的 TTS
                    if self.tts_engine.isBusy():
                        self.tts_engine.stop()

                    self.tts_engine.say(seg)
                except Exception as e:
                    print(f"[TTS錯誤] 無法播放此段文字: {seg}，原因: {e}")

            # 統一播放
            try:
                self.tts_engine.runAndWait()
            except Exception as e:
                print(f"[TTS錯誤] runAndWait 失敗: {e}")

            self.tts_queue.task_done()


    def ai_response(self, text):
        try:
            # --- 更新對話歷史 ---
            self.chat_history_list.append(f"使用者：{text}")

            # --- 截斷歷史，只保留最近 max_history 條 ---
            if len(self.chat_history_list) > self.max_history:
                self.chat_history_list = self.chat_history_list[-self.max_history:]

            # --- Qwen 對話最佳化 prompt ---
            prompt = f"""
            你是一個有禮貌且自然的桌面 AI 助理。
            以中文為主，必要時可混用英文數字，語氣自然。
            回答限制在 1~3 句之內，不要出現重複句、符號、過長內容或「--- 對話結束 ---」等奇怪片段。
            使用者：{text}
            助理：
            """

            # --- 呼叫模型 ---
            result = generator(
                prompt,
                max_new_tokens=100,
                do_sample=True,
                top_k=30,
                top_p=0.9,
                repetition_penalty=1.2,
                temperature=0.7,
                truncation=True,
                eos_token_id=tokenizer.eos_token_id
            )

            generated = result[0]["generated_text"]

            # --- 只取助理回覆部分 ---
            if "助理：" in generated:
                reply = generated.split("助理：")[-1].strip()
            else:
                reply = generated.strip()

            # --- 清理輸出 ---
            reply = re.sub(r'(\b\d+\b)(?:\W+\1)+', r'\1', reply)  # 重複數字
            reply = re.sub(r'(.)\1{5,}', r'\1', reply)            # 過度重複符號
            reply = re.sub(r'助理[:：]\s*', '', reply)           # 移除多餘開頭
            reply = re.sub(r'\n+', '\n', reply).strip()          # 多餘換行

            # --- 限制回覆長度 ---
            reply = reply[:150]

            # --- 更新歷史 ---
            self.chat_history_list.append(f"助理：{reply}")

            return reply

        except Exception as e:
            return f"[錯誤] {e}"

# --- 角色窗 ---
class CharacterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Assistant")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.label = QLabel(self)
        pixmap = QPixmap(character_path)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        self.resize(pixmap.width(), pixmap.height())
        self.offset = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None

# --- 主程式 ---
def run_ui():
    app = QApplication(sys.argv)
    window = CharacterWindow()
    window.show()
    chat_window = ChatWindow()
    chat_window.show()

    tray_icon = QSystemTrayIcon(QIcon(tray_path), parent=app)
    tray_menu = QMenu()
    
    toggle_action = QAction("顯示/隱藏角色")
    toggle_action.triggered.connect(lambda: window.setVisible(not window.isVisible()))
    tray_menu.addAction(toggle_action)
    
    chat_action = QAction("開啟對話視窗")
    chat_action.triggered.connect(chat_window.show)
    tray_menu.addAction(chat_action)
    
    def exit_app():
        chat_window.tts_queue.put(None)  # 通知 TTS 線程退出
        app.quit() 
    
    quit_action = QAction("退出助理")
    quit_action.triggered.connect(exit_app)
    tray_menu.addAction(quit_action)
    
    tray_icon.setContextMenu(tray_menu)
    tray_icon.show()

    keyboard.add_hotkey("f9", lambda: chat_window.setVisible(not chat_window.isVisible()))
    keyboard.add_hotkey("f8", lambda: window.setVisible(not window.isVisible()))
    keyboard.add_hotkey("f10", exit_app)  # F10 也呼叫安全退出

    sys.exit(app.exec())  

if __name__ == "__main__":
    run_ui()
