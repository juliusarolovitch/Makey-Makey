# Form implementation generated from reading ui file '/Users/juliusarolovitch/Desktop/Makey Makey/info_in.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 271)
        Form.setStyleSheet("background-color: white;")
        self.adult_name = QtWidgets.QPlainTextEdit(parent=Form)
        self.adult_name.setGeometry(QtCore.QRect(120, 60, 261, 41))
        self.adult_name.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border-radius: 8px;")
        self.adult_name.setObjectName("adult_name")
        self.phone_number = QtWidgets.QPlainTextEdit(parent=Form)
        self.phone_number.setGeometry(QtCore.QRect(120, 110, 261, 41))
        self.phone_number.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border-radius: 8px;")
        self.phone_number.setObjectName("phone_number")
        self.child_name = QtWidgets.QPlainTextEdit(parent=Form)
        self.child_name.setGeometry(QtCore.QRect(120, 160, 261, 41))
        self.child_name.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border-radius: 8px;")
        self.child_name.setObjectName("child_name")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 20, 401, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.submit = QtWidgets.QPushButton(parent=Form)
        self.submit.setGeometry(QtCore.QRect(210, 220, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans")
        font.setPointSize(14)
        self.submit.setFont(font)
        self.submit.setStyleSheet("background-color: green; color: white; border-radius: 6px;")
        self.submit.setObjectName("submit")
        self.quit = QtWidgets.QPushButton(parent=Form)
        self.quit.setGeometry(QtCore.QRect(90, 220, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Hiragino Sans")
        font.setPointSize(14)
        self.quit.setFont(font)
        self.quit.setStyleSheet("background-color: rgb(136, 4, 0); color: white; border-radius: 6px;")
        self.quit.setObjectName("quit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.adult_name.setPlaceholderText(_translate("Form", "Type Here"))
        self.phone_number.setPlaceholderText(_translate("Form", "Type Here"))
        self.child_name.setPlaceholderText(_translate("Form", "Type Here"))
        self.label.setText(_translate("Form", "Input Information"))
        self.label_2.setText(_translate("Form", "Your Name:"))
        self.label_3.setText(_translate("Form", "Phone #:"))
        self.label_4.setText(_translate("Form", "Child\'s Name:"))
        self.submit.setText(_translate("Form", "Submit"))
        self.quit.setText(_translate("Form", "Quit"))
