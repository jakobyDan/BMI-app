# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bmi_c.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import QCoreApplication, QRect, QMetaObject
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QStatusBar, QWidget, QLabel, QLineEdit, QPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Váha
        self.label_weight = QLabel(self.centralwidget)
        self.label_weight.setGeometry(QRect(20, 20, 100, 30))
        self.label_weight.setText("Váha (kg):")

        self.input_weight = QLineEdit(self.centralwidget)
        self.input_weight.setGeometry(QRect(130, 20, 100, 30))

        # Výška
        self.label_height = QLabel(self.centralwidget)
        self.label_height.setGeometry(QRect(20, 60, 100, 30))
        self.label_height.setText("Výška (cm):")

        self.input_height = QLineEdit(self.centralwidget)
        self.input_height.setGeometry(QRect(130, 60, 100, 30))

        # Tlačítko
        self.button_calc = QPushButton(self.centralwidget)
        self.button_calc.setGeometry(QRect(20, 100, 210, 40))
        self.button_calc.setText("Spočítat BMI")

        # Výsledek
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setGeometry(QRect(20, 160, 300, 30))
        self.label_result.setText("")

        # Menu bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "BMI Kalkulačka", None))
