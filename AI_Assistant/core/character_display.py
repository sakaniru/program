import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import os
from PIL import Image

# 建立 icons 資料夾（如果不存在）
os.makedirs("assets/icons", exist_ok=True)

# 開啟完整角色圖
img = Image.open("assets/character/assistant.png")

# 縮小到 32x32
img_small = img.resize((32, 32), Image.ANTIALIAS)

# 儲存成 tray.png
img_small.save("assets/icons/tray.png")

def run_ui():
    app = QApplication(sys.argv)
    window = CharacterWindow()
    window.show()

    tray_icon = QSystemTrayIcon(QIcon("assets/icons/tray.png"), parent=app)
    tray_menu = QMenu()

    # 顯示/隱藏角色
    toggle_action = QAction("顯示/隱藏角色")
    toggle_action.triggered.connect(lambda: window.setVisible(not window.isVisible()))
    tray_menu.addAction(toggle_action)

    # 退出程式
    quit_action = QAction("退出助理")
    quit_action.triggered.connect(app.quit)
    tray_menu.addAction(quit_action)  # <- 這行之前缺少

    tray_icon.setContextMenu(tray_menu)

    # 左鍵點擊托盤切換角色視窗
    tray_icon.activated.connect(lambda reason: window.setVisible(not window.isVisible())
                               if reason == QSystemTrayIcon.Trigger else None)

    tray_icon.show()
    sys.exit(app.exec_())
class CharacterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Assistant")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel(self)
        pixmap = QPixmap("assets/character/assistant.png")
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



    