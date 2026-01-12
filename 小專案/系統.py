from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QStackedWidget, QLabel, QTabWidget
)
import sys


class RibbonWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("二手書交易平台")
        self.resize(1000, 600)

        # ==== Ribbon Tabs ====
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)  # 分頁在上面
        self.tabs.setFixedHeight(120)  # Ribbon 高度

        # 每頁一個 Ribbon Group 區塊
        self.tabs.addTab(self.create_home_tab(), "常用")
        self.tabs.addTab(self.create_insert_tab(), "插入")
        self.tabs.addTab(self.create_settings_tab(), "設定")

        # ==== 中央內容頁 ====
        self.pages = QStackedWidget()
        self.pages.addWidget(QLabel("📌 常用頁面內容"))
        self.pages.addWidget(QLabel("🧱 插入頁面內容"))
        self.pages.addWidget(QLabel("⚙️ 設定頁面內容"))

        # 切換頁面
        self.tabs.currentChanged.connect(self.pages.setCurrentIndex)

        # ==== 主 Layout ====
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(self.tabs)
        layout.addWidget(self.pages)

        self.setCentralWidget(container)

    # ----- Ribbon Page: 常用 -----
    def create_home_tab(self):
        page = QWidget()
        layout = QHBoxLayout(page)

        layout.addWidget(QPushButton("複製"))
        layout.addWidget(QPushButton("貼上"))
        layout.addWidget(QPushButton("清除"))

        return page

    # ----- Ribbon Page: 插入 -----
    def create_insert_tab(self):
        page = QWidget()
        layout = QHBoxLayout(page)

        layout.addWidget(QPushButton("插入文字"))
        layout.addWidget(QPushButton("插入圖片"))
        layout.addWidget(QPushButton("插入表格"))

        return page

    # ----- Ribbon Page: 設定 -----
    def create_settings_tab(self):
        page = QWidget()
        layout = QHBoxLayout(page)

        layout.addWidget(QPushButton("主題設定"))
        layout.addWidget(QPushButton("快捷鍵"))
        layout.addWidget(QPushButton("版本資訊"))

        return page


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RibbonWindow()
    window.show()
    sys.exit(app.exec_())
