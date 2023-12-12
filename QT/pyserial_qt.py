import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QComboBox, QLabel
)

class SerialApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.serial_port = None
        self.init_ui()

    def init_ui(self):
        # 主窗口设置
        self.setWindowTitle('PyQt5 串口通信')
        self.setGeometry(100, 100, 300, 150)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 垂直布局
        layout = QVBoxLayout(central_widget)

        # 可用串口下拉菜单
        self.port_list_combo_box = QComboBox()
        self.refresh_ports()
        layout.addWidget(self.port_list_combo_box)

        # 连接按钮
        connect_button = QPushButton('连接')
        connect_button.clicked.connect(self.connect_to_serial_port)
        layout.addWidget(connect_button)

        # 状态标签
        self.status_label = QLabel('未连接')
        layout.addWidget(self.status_label)

    def refresh_ports(self):
        # 刷新可用串口列表
        self.port_list_combo_box.clear()
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            self.port_list_combo_box.addItem(f"{port}: {desc}", port)

    def connect_to_serial_port(self):
        selected_port = self.port_list_combo_box.currentData()

        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()

        try:
            self.serial_port = serial.Serial(
                selected_port,
                baudrate=9600,
                timeout=1
            )
            self.status_label.setText(f"已连接到 {selected_port}")
        except serial.SerialException as e:
            self.status_label.setText("连接失败")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = SerialApp()
    main_app.show()
    sys.exit(app.exec_())
