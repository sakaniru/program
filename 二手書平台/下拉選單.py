from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton
import sys

# class Demo(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("選擇課程")
#         self.resize(200, 100)

#         layout = QVBoxLayout()

#         # ✨👇 在這裡換成你自己的資料
#         data_list = [
#             "英文",
#             "數學",
#             "程式設計",
#             "國文",
#             "資料結構",
#             "離散數學",
#             "微積分",
#             "計算機概論"
#         ]

#         self.combo = QComboBox()
#         self.combo.addItems(data_list)   # ← 加入你自己設計的資料
#         layout.addWidget(self.combo)


#         self.setLayout(layout)
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("選擇科系")
        self.resize(200, 100)

        layout = QVBoxLayout()

        # ✨👇 在這裡換成你自己的資料
        data_list = [
            "資訊管理系","應用英文系","財務金融系","企業管理系","商業設計管理系",
            "國際企業系","資訊工程系","電子工程系","機械工程系","土木工程系",
        ]

        self.combo = QComboBox()
        self.combo.addItems(data_list)   # ← 加入你自己設計的資料
        layout.addWidget(self.combo)


        self.setLayout(layout)


app = QApplication(sys.argv)
demo = Demo()
demo.show()
sys.exit(app.exec_())
