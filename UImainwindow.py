# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/veigar/Documents/7wonders/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Military = QtWidgets.QGroupBox(self.centralwidget)
        self.Military.setGeometry(QtCore.QRect(10, 10, 231, 61))
        self.Military.setObjectName("Military")
        self.numbox = IncrSpinBox(self.Military)
        self.numbox.setGeometry(QtCore.QRect(90, 20, 50, 30))
        self.numbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numbox.setReadOnly(False)
        self.numbox.setObjectName("numbox")
        self.n1 = QtWidgets.QPushButton(self.Military)
        self.n1.setGeometry(QtCore.QRect(50, 20, 30, 30))
        self.n1.setObjectName("n1")
        self.n5 = QtWidgets.QPushButton(self.Military)
        self.n5.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.n5.setObjectName("n5")
        self.p5 = QtWidgets.QPushButton(self.Military)
        self.p5.setGeometry(QtCore.QRect(190, 20, 30, 30))
        self.p5.setObjectName("p5")
        self.p1 = QtWidgets.QPushButton(self.Military)
        self.p1.setGeometry(QtCore.QRect(150, 20, 30, 30))
        self.p1.setObjectName("p1")
        self.Treasury = QtWidgets.QGroupBox(self.centralwidget)
        self.Treasury.setGeometry(QtCore.QRect(10, 70, 231, 61))
        self.Treasury.setObjectName("Treasury")
        self.numbox_5 = IncrSpinBox(self.Treasury)
        self.numbox_5.setGeometry(QtCore.QRect(90, 20, 50, 30))
        self.numbox_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numbox_5.setReadOnly(False)
        self.numbox_5.setObjectName("numbox_5")
        self.n1_5 = QtWidgets.QPushButton(self.Treasury)
        self.n1_5.setGeometry(QtCore.QRect(50, 20, 30, 30))
        self.n1_5.setObjectName("n1_5")
        self.n5_5 = QtWidgets.QPushButton(self.Treasury)
        self.n5_5.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.n5_5.setObjectName("n5_5")
        self.p5_5 = QtWidgets.QPushButton(self.Treasury)
        self.p5_5.setGeometry(QtCore.QRect(190, 20, 30, 30))
        self.p5_5.setObjectName("p5_5")
        self.p1_5 = QtWidgets.QPushButton(self.Treasury)
        self.p1_5.setGeometry(QtCore.QRect(150, 20, 30, 30))
        self.p1_5.setObjectName("p1_5")
        self.Civillian = QtWidgets.QGroupBox(self.centralwidget)
        self.Civillian.setGeometry(QtCore.QRect(10, 190, 231, 61))
        self.Civillian.setObjectName("Civillian")
        self.numbox_2 = IncrSpinBox(self.Civillian)
        self.numbox_2.setGeometry(QtCore.QRect(90, 20, 50, 30))
        self.numbox_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numbox_2.setReadOnly(False)
        self.numbox_2.setObjectName("numbox_2")
        self.n1_2 = QtWidgets.QPushButton(self.Civillian)
        self.n1_2.setGeometry(QtCore.QRect(50, 20, 30, 30))
        self.n1_2.setObjectName("n1_2")
        self.n5_2 = QtWidgets.QPushButton(self.Civillian)
        self.n5_2.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.n5_2.setObjectName("n5_2")
        self.p5_2 = QtWidgets.QPushButton(self.Civillian)
        self.p5_2.setGeometry(QtCore.QRect(190, 20, 30, 30))
        self.p5_2.setObjectName("p5_2")
        self.p1_2 = QtWidgets.QPushButton(self.Civillian)
        self.p1_2.setGeometry(QtCore.QRect(150, 20, 30, 30))
        self.p1_2.setObjectName("p1_2")
        self.Wonder = QtWidgets.QGroupBox(self.centralwidget)
        self.Wonder.setGeometry(QtCore.QRect(10, 130, 231, 61))
        self.Wonder.setObjectName("Wonder")
        self.numbox_3 = IncrSpinBox(self.Wonder)
        self.numbox_3.setGeometry(QtCore.QRect(90, 20, 50, 30))
        self.numbox_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numbox_3.setReadOnly(False)
        self.numbox_3.setObjectName("numbox_3")
        self.n1_3 = QtWidgets.QPushButton(self.Wonder)
        self.n1_3.setGeometry(QtCore.QRect(50, 20, 30, 30))
        self.n1_3.setObjectName("n1_3")
        self.n5_3 = QtWidgets.QPushButton(self.Wonder)
        self.n5_3.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.n5_3.setObjectName("n5_3")
        self.p5_3 = QtWidgets.QPushButton(self.Wonder)
        self.p5_3.setGeometry(QtCore.QRect(190, 20, 30, 30))
        self.p5_3.setObjectName("p5_3")
        self.p1_3 = QtWidgets.QPushButton(self.Wonder)
        self.p1_3.setGeometry(QtCore.QRect(150, 20, 30, 30))
        self.p1_3.setObjectName("p1_3")
        self.Commercial = QtWidgets.QGroupBox(self.centralwidget)
        self.Commercial.setGeometry(QtCore.QRect(10, 250, 231, 61))
        self.Commercial.setObjectName("Commercial")
        self.numbox_4 = IncrSpinBox(self.Commercial)
        self.numbox_4.setGeometry(QtCore.QRect(90, 20, 50, 30))
        self.numbox_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numbox_4.setReadOnly(False)
        self.numbox_4.setObjectName("numbox_4")
        self.n1_4 = QtWidgets.QPushButton(self.Commercial)
        self.n1_4.setGeometry(QtCore.QRect(50, 20, 30, 30))
        self.n1_4.setObjectName("n1_4")
        self.n5_4 = QtWidgets.QPushButton(self.Commercial)
        self.n5_4.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.n5_4.setObjectName("n5_4")
        self.p5_4 = QtWidgets.QPushButton(self.Commercial)
        self.p5_4.setGeometry(QtCore.QRect(190, 20, 30, 30))
        self.p5_4.setObjectName("p5_4")
        self.p1_4 = QtWidgets.QPushButton(self.Commercial)
        self.p1_4.setGeometry(QtCore.QRect(150, 20, 30, 30))
        self.p1_4.setObjectName("p1_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSeven_Wonders_Score_Calculator = QtWidgets.QMenu(self.menubar)
        self.menuSeven_Wonders_Score_Calculator.setObjectName("menuSeven_Wonders_Score_Calculator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSeven_Wonders_Score_Calculator.menuAction())

        self.retranslateUi(MainWindow)
        self.p5.clicked.connect(self.numbox.stepFiveUp)
        self.p1.clicked.connect(self.numbox.stepUp)
        self.n1.clicked.connect(self.numbox.stepDown)
        self.n5.clicked.connect(self.numbox.stepFiveDown)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Military.setTitle(_translate("MainWindow", "Military"))
        self.n1.setText(_translate("MainWindow", "-1"))
        self.n5.setText(_translate("MainWindow", "-5"))
        self.p5.setText(_translate("MainWindow", "+5"))
        self.p1.setText(_translate("MainWindow", "+1"))
        self.Treasury.setTitle(_translate("MainWindow", "Treasury"))
        self.n1_5.setText(_translate("MainWindow", "-1"))
        self.n5_5.setText(_translate("MainWindow", "-5"))
        self.p5_5.setText(_translate("MainWindow", "+5"))
        self.p1_5.setText(_translate("MainWindow", "+1"))
        self.Civillian.setTitle(_translate("MainWindow", "Civillian"))
        self.n1_2.setText(_translate("MainWindow", "-1"))
        self.n5_2.setText(_translate("MainWindow", "-5"))
        self.p5_2.setText(_translate("MainWindow", "+5"))
        self.p1_2.setText(_translate("MainWindow", "+1"))
        self.Wonder.setTitle(_translate("MainWindow", "Wonder"))
        self.n1_3.setText(_translate("MainWindow", "-1"))
        self.n5_3.setText(_translate("MainWindow", "-5"))
        self.p5_3.setText(_translate("MainWindow", "+5"))
        self.p1_3.setText(_translate("MainWindow", "+1"))
        self.Commercial.setTitle(_translate("MainWindow", "Commercial"))
        self.n1_4.setText(_translate("MainWindow", "-1"))
        self.n5_4.setText(_translate("MainWindow", "-5"))
        self.p5_4.setText(_translate("MainWindow", "+5"))
        self.p1_4.setText(_translate("MainWindow", "+1"))
        self.menuSeven_Wonders_Score_Calculator.setTitle(_translate("MainWindow", "Seven Wonders Score Calculator"))
from incrspinbox import IncrSpinBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())