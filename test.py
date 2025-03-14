import sys
import pygetwindow as gw
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
)
from PySide6.QtGui import QScreen, QPixmap, QPainter, QPen
from PySide6.QtCore import Qt, QRect, QPoint

class ScreenshotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle("屏幕截图工具")
        self.setGeometry(100, 100, 400, 200)
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        # 截图按钮
        self.btn_dingtalk = QPushButton("截取钉钉窗口", self)
        
        layout.addWidget(self.btn_dingtalk)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def setup_connections(self):
        """连接信号与槽"""
        self.btn_dingtalk.clicked.connect(self.capture_dingtalk_window)

    def capture_dingtalk_window(self):
        """截取钉钉窗口"""
        dingtalk_windows = [win for win in gw.getWindowsWithTitle('钉钉') if win.visible]
        if not dingtalk_windows:
            QMessageBox.warning(self, "错误", "未找到钉钉窗口")
            return
        
        dingtalk_window = dingtalk_windows[0]
        x, y, width, height = dingtalk_window.left, dingtalk_window.top, dingtalk_window.width, dingtalk_window.height
        
        screen = QApplication.primaryScreen()
        if screen:
            pixmap = screen.grabWindow(0, x, y, width, height)
            self.save_screenshot(pixmap)

    def save_screenshot(self, pixmap):
        """保存截图到文件"""
        import time
        file_name = f'screenshot_{time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())}.png'
        if file_name:
            success = pixmap.save(file_name)
            if success:
                QMessageBox.information(self, "成功", "截图保存成功！")
            else:
                QMessageBox.warning(self, "错误", "保存文件失败！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScreenshotWindow()
    window.show()
    sys.exit(app.exec())