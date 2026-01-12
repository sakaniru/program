import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QHBoxLayout
import random


# ======== 訊息池（改為"有順序的列表"） ========
buyer_chat_log = [("system", "系統：歡迎使用二手書交易平台！<br>")]
seller_chat_log = [
    ("system", "系統：歡迎使用二手書交易平台！"),
    ("system", "請注意：賣方上架書籍21天後，平台將自動下架。<br>")
]


# 生成買家 / 賣家匿名名稱
random_username = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
buyer_name = "".join(random.choice(random_username) for _ in range(16))
while True:
    seller_name = "".join(random.choice(random_username) for _ in range(16))
    if seller_name != buyer_name:
        break


# ======== 買家視窗 ========
class BuyerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("買家對平台")
        self.resize(350, 400)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("買家對平台對話區"))

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        layout.addWidget(self.chat)

        self.input = QLineEdit()
        self.input.setPlaceholderText("輸入訊息給平台...")
        layout.addWidget(self.input)

        send_btn = QPushButton("送出給平台")
        send_btn.clicked.connect(self.send_message)
        layout.addWidget(send_btn)

        self.setLayout(layout)
        self.update_chat()

    def send_message(self):
        text = self.input.text().strip()
        if text:
            buyer_chat_log.append(("buyer", f"買家 {buyer_name}: {text}"))
            self.input.clear()
            self.update_chat()
            platform.update_chats()

    def update_chat(self):
        html = ""
        for sender, msg in buyer_chat_log:
            if sender == "buyer":
                html += f"<div style='color:black; text-align:left;'>{msg}</div>"
            elif sender == "platform":
                html += f"<div style='color:black; text-align:right;'>{msg}</div>"
            else:  # system
                html += f"<div style='color:black; text-align:center;'>{msg}</div>"
        self.chat.setHtml(html)


# ======== 賣家視窗 ========
class SellerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("賣家對平台")
        self.resize(350, 400)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("賣家對平台對話區"))

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        layout.addWidget(self.chat)

        self.input = QLineEdit()
        self.input.setPlaceholderText("輸入訊息給平台...")
        layout.addWidget(self.input)

        send_btn = QPushButton("送出給平台")
        send_btn.clicked.connect(self.send_message)
        layout.addWidget(send_btn)

        self.setLayout(layout)
        self.update_chat()

    def send_message(self):
        text = self.input.text().strip()
        if text:
            seller_chat_log.append(("seller", f"賣家 {seller_name}: {text}"))
            self.input.clear()
            self.update_chat()
            platform.update_chats()

    def update_chat(self):
        html = ""
        for sender, msg in seller_chat_log:
            if sender == "seller":
                html += f"<div style='color:black; text-align:left;'>{msg}</div>"
            elif sender == "platform":
                html += f"<div style='color:black; text-align:right;'>{msg}</div>"
            else:
                html += f"<div style='color:black; text-align:center;'>{msg}</div>"
        self.chat.setHtml(html)


# ======== 平台視窗 ========
class PlatformWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("平台客服中心")
        self.resize(700, 400)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("平台客服訊息中心"))

        self.chat_buyer = QTextEdit(); self.chat_buyer.setReadOnly(True)
        self.chat_seller = QTextEdit(); self.chat_seller.setReadOnly(True)

        chats = QHBoxLayout()
        chats.addWidget(self.chat_buyer)
        chats.addWidget(self.chat_seller)
        layout.addLayout(chats)

        self.input = QLineEdit()
        self.input.setPlaceholderText("輸入平台回應訊息...")
        layout.addWidget(self.input)

        btns = QHBoxLayout()
        btn_buyer = QPushButton("回覆給買家")
        btn_seller = QPushButton("回覆給賣家")
        btn_buyer.clicked.connect(self.send_to_buyer)
        btn_seller.clicked.connect(self.send_to_seller)
        btns.addWidget(btn_buyer)
        btns.addWidget(btn_seller)
        layout.addLayout(btns)

        self.setLayout(layout)
        self.update_chats()

    def send_to_buyer(self):
        text = self.input.text().strip()
        if text:
            buyer_chat_log.append(("platform", f"平台：{text}"))
            self.input.clear()
            self.update_chats()
            buyer.update_chat()

    def send_to_seller(self):
        text = self.input.text().strip()
        if text:
            seller_chat_log.append(("platform", f"平台：{text}"))
            self.input.clear()
            self.update_chats()
            seller.update_chat()

    def update_chats(self):
        html = ""
        for sender, msg in buyer_chat_log:
            if sender == "buyer":
                html += f"<div style='color:black; text-align:left;'>{msg}</div>"
            elif sender == "platform":
                html += f"<div style='color:black; text-align:right;'>{msg}</div>"
            else:
                html += f"<div style='color:black; text-align:center;'>{msg}</div>"
        self.chat_buyer.setHtml(html)

        html = ""
        for sender, msg in seller_chat_log:
            if sender == "seller":
                html += f"<div style='color:black; text-align:left;'>{msg}</div>"
            elif sender == "platform":
                html += f"<div style='color:black; text-align:right;'>{msg}</div>"
            else:
                html += f"<div style='color:black; text-align:center;'>{msg}</div>"
        self.chat_seller.setHtml(html)


# ======== 主程式啟動 ========
app = QApplication(sys.argv)

buyer = BuyerWindow()
seller = SellerWindow()
platform = PlatformWindow()

buyer.show()
seller.show()
platform.show()

sys.exit(app.exec_())
