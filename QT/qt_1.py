import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# 更新标签的函数
def update_label():
    label.setText("你好，世界！")

# 创建一个应用（Application）实例
app = QApplication(sys.argv)

# 创建一个窗口（Widget）实例
window = QWidget()
window.setWindowTitle('串口通信工具')

# # 创建一个标签（Label）实例
label = QLabel('点击下面的按钮更新这段文字。', window)

# # 创建一个按钮（Button）实例，并连接到更新标签的函数
# button = QPushButton('点击我', window)
# button.clicked.connect(update_label)
#
# # 创建一个垂直布局（VBox）
# layout = QVBoxLayout()
# layout.addWidget(label)
# layout.addWidget(button)
#
# # 将布局设置到窗口中
# window.setLayout(layout)

# 显示窗口
window.show()

# 运行应用，并在退出时清理
sys.exit(app.exec_())
