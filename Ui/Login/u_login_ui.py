# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginchido.ui'
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 700)
        Dialog.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1a1a1a, stop:1 #4a4a4a);")
        self.backgroundImage = QtWidgets.QLabel(Dialog)
        self.backgroundImage.setGeometry(QtCore.QRect(0, 0, 500, 700))
        self.backgroundImage.setStyleSheet("border-image: url(:/images/coffee_bg.jpg);\nopacity: 0.2;")
        self.backgroundImage.setText("")
        self.backgroundImage.setObjectName("backgroundImage")
        self.mainContainer = QtWidgets.QWidget(Dialog)
        self.mainContainer.setGeometry(QtCore.QRect(50, 100, 400, 500))
        self.mainContainer.setStyleSheet("background: rgba(40, 40, 40, 0.9);\nborder-radius: 20px;\nborder: 2px solid #5d432c;")
        self.mainContainer.setObjectName("mainContainer")
        
        # Título
        self.titleLabel = QtWidgets.QLabel(self.mainContainer)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 400, 80))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: #c7a17a;\nbackground: transparent;\nqproperty-alignment: AlignCenter;\ntext-shadow: 0 0 10px #c7a17a;")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("MgtFood")
        
        # Campos de entrada
        self.userInput = QtWidgets.QLineEdit(self.mainContainer)
        self.userInput.setGeometry(QtCore.QRect(50, 150, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.userInput.setFont(font)
        self.userInput.setStyleSheet("QLineEdit {background: #2a2a2a; border: 2px solid #5d432c; border-radius: 10px; padding: 10px; color: #c7a17a;}\nQLineEdit:focus {border-color: #c7a17a;}")
        self.userInput.setPlaceholderText("Usuario")
        
        self.passwordInput = QtWidgets.QLineEdit(self.mainContainer)
        self.passwordInput.setGeometry(QtCore.QRect(50, 220, 300, 50))
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet("QLineEdit {background: #2a2a2a; border: 2px solid #5d432c; border-radius: 10px; padding: 10px; color: #c7a17a;}\nQLineEdit:focus {border-color: #c7a17a;}")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setPlaceholderText("Contraseña")
        
        # Botón
        self.loginButton = QtWidgets.QPushButton(self.mainContainer)
        self.loginButton.setGeometry(QtCore.QRect(100, 300, 200, 50))
        font.setPointSize(16)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton {background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #5d432c, stop:1 #c7a17a); color: white; border-radius: 10px;}\nQPushButton:hover {background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #c7a17a, stop:1 #5d432c);}")
        self.loginButton.setText("Iniciar Sesión")
        
        # Footer
        self.footerText = QtWidgets.QLabel(self.mainContainer)
        self.footerText.setGeometry(QtCore.QRect(0, 430, 400, 30))
        font.setPointSize(10)
        font.setItalic(True)
        self.footerText.setFont(font)
        self.footerText.setStyleSheet("color: #c7a17a; background: transparent; qproperty-alignment: AlignCenter;")
        self.footerText.setText("MgtFood - 2025")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Life: A New Brew"))