import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
from PySide6.QtCore import QThread, Signal, QTimer
from ui_mainwindow import Ui_MainWindow
import serial
import serial.tools.list_ports
from threading import RLock
import time
from functools import reduce
from PySide6.QtWidgets import QMessageBox


class SerialThread(QThread):
    data_received = Signal(bytes)
    available_port = Signal(str, bool)
    lock = RLock()

    def __init__(self, serial):
        super().__init__()
        self.serial = serial
        self.running = True
        self.available_ports = []
    
    def run(self):
        while self.running:
            self.lock.acquire()
            while self.serial.is_open:
                try:
                    if self.serial.in_waiting:
                        data = self.serial.read(self.serial.in_waiting)
                        self.data_received.emit(data)  # 发送数据到主线程
                except Exception as e:
                    print(e)
                    self.serial.close()
            self.lock.release()
            available_device = [port.device for port in serial.tools.list_ports.comports()]
            for device in available_device:
                if device not in self.available_ports:
                    self.available_port.emit(device, True)
                    self.available_ports.append(device)
            for device in self.available_ports:
                if device not in available_device:
                    self.available_port.emit(device, False)
                    self.available_ports.remove(device)

    def stop(self):
        self.running = False



def frame(road_num):
    # 设置控制命令
    cmd = f'A0 0{road_num} 04'
    check_sum = (sum([int(x, 16) for x in cmd.split(' ')])) % 256
    print(f'--{cmd} {check_sum:02X}--')
    return bytes.fromhex(f'{cmd} {check_sum:02X}')


class TaskTread(QThread):
    task_completed = Signal(str)

    def __init__(self, tasks, serial):
        super().__init__()
        self.tasks = tasks
        self.serial = serial

    def run(self):
        for Qitem, seconds in self.tasks.items():
            if seconds == '0':
                continue
            num = Qitem.objectName()[4]
            self.serial.write(frame(num))
            time.sleep(int(seconds))
            self.serial.write(frame(num))
            self.task_completed.emit(num)
            time.sleep(0.01)
        self.task_completed.emit('_all')



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serial_thread = None
        self.serial = serial.Serial()
        self.serial_thread = SerialThread(self.serial)
        self.serial_thread.data_received.connect(self.handle_serial_data)
        self.serial_thread.available_port.connect(self.handle_com)
        self.serial_thread.start()
        self.task_thread_dict = {}

        self.connect_signals()

    def connect_signals(self):
        self.ui.open_serial_button.clicked.connect(self.toggle_serial)
    
        for i in range(1, 5):
            self.ui.__dict__[f'road{i}_open'].clicked.connect(self.toggle_road)

        self.ui.road_all_open.clicked.connect(self.toggle_all_road)
        self.ui.road_all_selected.stateChanged.connect(self.toggle_check_all_road)


    def open_serial(self):
        port = self.ui.serial_port.currentText()
        self.serial.port = port
        self.serial.baudrate = 9600
        self.serial.open()
        self.ui.open_serial_button.setText("关闭")

    def close_serial(self):
        self.serial.close()
        self.ui.open_serial_button.setText("打开")
    
    def toggle_serial(self):
        # 打开串口
        if self.serial.is_open:
            self.close_serial()
            self.ui.open_serial_button.setText("打开")
            self.ui.serial_port.setEnabled(True)
        else:
            self.open_serial()
            self.ui.open_serial_button.setText("关闭")
            self.ui.serial_port.setEnabled(False)

    def send_data(self, data):
        if self.serial.is_open:
            print("发送data", data)
            self.serial.write(bytes(data))
    
    def toggle_road(self):
        if not self.serial.is_open:
            QMessageBox.warning(self, "Warning", "串口未打开")
            return
        sender_button = self.sender()
        num = sender_button.objectName()[4]
        if sender_button.text() == "打开":
            seconds = self.ui.__dict__[f"road{num}_set_time"].text()
            if seconds and int(seconds) != 0:
                sender_button.setEnabled(False)
                sender_button.setStyleSheet("opacity: 0.5;")
                task_dict = {sender_button: seconds}
                # self.task_thread = TaskTread(task_dict, self.serial)
                # self.task_thread.task_completed.connect(self.enable_road_button)
                # self.task_thread.start()
                task_thread = TaskTread(task_dict, self.serial)
                task_thread.task_completed.connect(self.enable_road_button)
                task_thread.start()
                self.task_thread_dict[num] = task_thread
            else:
                sender_button.setText("关闭")
                self.send_data(frame(num))
        else:
            sender_button.setText("打开")
            self.send_data(frame(num))
    
    def toggle_check_all_road(self):
        if self.ui.road_all_selected.isChecked():
            seconds = int(self.ui.road_all_set_time.text())
            for i in range(1, 5):
                self.ui.__dict__[f'road{i}_selected'].setChecked(True)
                self.ui.__dict__[f"road{i}_set_time"].setValue(seconds)
        else:
            for i in range(1, 5):
                self.ui.__dict__[f'road{i}_selected'].setChecked(False)

    def toggle_all_road(self):
        if not self.serial.is_open:
            QMessageBox.warning(self, "Warning", "串口未打开")
            return
        if self.ui.road_all_open.text() == "打开":
            # self.ui.road_all_open.setText("关闭")
            # 获取1~4check状态
            task_dict = {}
            for i in range(1, 5):
                if self.ui.__dict__[f'road{i}_selected'].isChecked() and self.ui.__dict__[f"road{i}_set_time"].text() !='0':
                    self.ui.__dict__[f'road{i}_open'].setEnabled(False)
                    task_dict[self.ui.__dict__[f'road{i}_open']] = self.ui.__dict__[f"road{i}_set_time"].text()
            if task_dict:
                self.ui.road_all_open.setEnabled(False)
                self.task_thread = TaskTread(task_dict, self.serial)
                self.task_thread.task_completed.connect(self.enable_road_button)
                self.task_thread.start()
        else:
            self.ui.road_all_open.setText("打开")
            for i in range(1, 5):
                self.ui.__dict__[f'road{i}_open'].setEnabled(True)


    def handle_serial_data(self, data):
        print("revive data: ", data.hex().upper())

    def handle_com(self, com, status):
        if status:
            self.ui.serial_port.addItem(com)
        else:
            self.ui.serial_port.removeItem(self.ui.serial_port.findText(com))
    
    def enable_road_button(self, num):
        self.ui.__dict__[f'road{num}_open'].setEnabled(True)



    def closeEvent(self, event):
        if self.serial_thread:
            self.serial_thread.stop()
            self.serial_thread.wait()
        event.accept()



if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
