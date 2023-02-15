# Art of Making Hand Washing
from PyQt6 import QtWidgets
import sys

# Art of Making Hand Washing
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtCore import QThread, QObject, pyqtSignal
import sys
from time import sleep
import keyboard
from time import time
from twilio.rest import Client


class Worker1(QObject):

    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        while True:
            try:
                sleep(1/15)
                self.progress.emit(1)
            except:
                continue


class Info(QtWidgets.QMainWindow):

    def __init__(self):
        super(Info, self).__init__()

        self._widget = QtWidgets.QWidget()
        uic.loadUi('info_in.ui', self._widget)

        self._widget.findChild(
            QtWidgets.QPushButton, 'submit').clicked[bool].connect(self.buttonPressed)

        self._widget.findChild(
            QtWidgets.QPushButton, 'quit').clicked[bool].connect(self.shutdown)

        self.setWindowTitle("Info")

        self._widget.show()

    def buttonPressed(self):
        print("Button Pressed")
        self.phone_number = self._widget.phone_number.toPlainText()
        self.adult_name = self._widget.adult_name.toPlainText()
        self.child_name = self._widget.child_name.toPlainText()
        window.update_info(self.phone_number,
                           self.adult_name, self.child_name)

    def shutdown(self):
        self._widget.close()


class Ui(QtWidgets.QMainWindow):
    def update_info(self, phone_number, adult_name, child_name):
        self.phone_number = phone_number
        self.adult_name = adult_name
        self.child_name = child_name

    def __init__(self):
        super(Ui, self).__init__()

        self._widget = QtWidgets.QWidget()
        uic.loadUi('test.ui', self._widget)

        self._widget.findChild(
            QtWidgets.QPushButton, 'the_button').clicked[bool].connect(self.buttonPressed)
        self._widget.findChild(
            QtWidgets.QPushButton, 'the_quit').clicked[bool].connect(self.shutdown)

        self.setWindowTitle("AoM")

        self._widget.show()
        self.time_temp = 0
        self.time_total = 0
        self.current_mode = "Start"
        self.adult_name = None
        self.child_name = None
        self.phone_number = None

        self.thread1 = QThread()
        self.worker1 = Worker1()

        self.worker1.moveToThread(self.thread1)

        self.thread1.started.connect(self.worker1.run)
        self.worker1.finished.connect(self.thread1.quit)
        self.worker1.finished.connect(self.worker1.deleteLater)
        self.thread1.finished.connect(self.thread1.deleteLater)
        self.worker1.progress.connect(self.update_gui)

        self.thread1.start()

    def shutdown(self):
        self._widget.close()

    def buttonPressed(self):
        print("Button Pressed")
        if self.current_mode == "Start":
            self.current_mode = "Finish"
            self.time_temp = time()
            self._widget.the_button.setStyleSheet(
                "background-color: rgb(136, 4, 0);\ncolor: white;\nborder-radius: 4px;\n")
            self._widget.the_button.setText(self.current_mode)
        elif self.current_mode == 'Finish':
            self.current_mode = "Start"
            self._widget.the_button.setStyleSheet(
                "background-color: green;\ncolor: white;\nborder-radius: 4px;\n")
            self._widget.timer.setStyleSheet(
                "background-color: black;\ncolor: white;\nborder-radius: 4px;\n")
            self._widget.the_button.setText(self.current_mode)
            if self.time_total < 20:
                self.message = f"Dear {self.adult_name}: your child, {self.child_name}, washed their hands but for less than 20 seconds."
                self.send_text(self.message, self.phone_number)
            elif self.time_total >= 20:
                self.message = f"Dear {self.adult_name}: your child, {self.child_name}, washed their hands well."
                self.send_text(self.message, self.phone_number)
            self.time_total = 0

        else:
            self.current_mode = 'Error'

    def update_gui(self):
        print("Updating")
        # if keyboard.is_pressed("w") and self.current_mode == "Finish":
        #     self.time_total += time.now() - self.time_temp
        #     self.time_temp = time.now()
        # else:
        #     self.time_temp = time.now()
        # self.percentage = self.total / 20 * 100
        # if self.percentage < 50:
        #     self._widget.timer.setStyleSheet(
        #         f"background-color: rgb(255, 0, 0, {100-self.percentage*2});\ncolor: black;\nborder-radius: 4px;\n")
        # elif self.percentage >= 50:
        #     if self.percentage > 100:
        #         self.percentage = 100
        #     self._widget.timer.setStyleSheet(
        #         f"background-color: rgb(0, 255, 0, {(self.percentage - 50) * 2});\ncolor: black;\nborder-radius: 4px;\n")

    def send_text(self, text, number):
        account_sid = 'ACdb01d919bb45f18f2b47fb052e07e7ce'
        auth_token = '23a9bf620deb596c8680f8cda26bbd96'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            messaging_service_sid='MG9c4c10cc5ef2e3fd67307eb513c51b63',
            body=text,
            to=number
        )


app2 = QtWidgets.QApplication(sys.argv)
app1 = QtWidgets.QApplication(sys.argv)

window = Ui()
window1 = Info()

sys.exit(app2.exec())
