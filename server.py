import sys
from PySide6.QtCore import QThread, Signal
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from PySide6.QtWidgets import QApplication, QMainWindow

class UdpServer(QThread):
    udp_data_received = Signal(bytes)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.udp_socket = QUdpSocket()
        self.udp_socket.bind(QHostAddress.Any, self.port)
        self.udp_socket.readyRead.connect(self.read_data)
        self.running = True

    def run(self):
        while self.running:
            QThread.msleep(100)

    def read_data(self):
        while self.udp_socket.hasPendingDatagrams():
            datagram, _, _ = self.udp_socket.readDatagram(self.udp_socket.pendingDatagramSize())
            self.udp_data_received.emit(datagram)

    def stop(self):
        self.running = False
        self.udp_socket.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.udp_server = UdpServer(12345)  # 设备监听的端口
        self.udp_server.udp_data_received.connect(self.handle_udp_data)
        self.udp_server.start()

    def handle_udp_data(self, data):
        print("Received UDP data:", data)

    def closeEvent(self, event):
        if self.udp_server:
            self.udp_server.stop()
            self.udp_server.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())