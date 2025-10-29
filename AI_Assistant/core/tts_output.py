import pyttsx3

# def speak_text(text: str):
#     """文字轉語音並播放"""
#     try:
#         engine = pyttsx3.init()
#         engine.setProperty('rate', 170)     # 語速
#         engine.setProperty('volume', 1.0)   # 音量（0.0 ~ 1.0）

#         # 嘗試找中文語音
#         voices = engine.getProperty('voices')
#         for voice in voices:
#             if "Chinese" in voice.name or "ZH" in voice.id:
#                 engine.setProperty('voice', voice.id)
#                 break

#         print(f"🤖 助理說：{text}")
#         engine.say(text)
#         engine.runAndWait()

#     except Exception as e:
#         print(f"❌ 語音輸出錯誤：{e}")
from core.tts_output import speak_text

if __name__ == "__main__":
    speak_text("你好，我是你的語音助理。")
