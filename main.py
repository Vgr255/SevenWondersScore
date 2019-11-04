import sys
from functools import partial

from PyQt5.QtWidgets import *


class SevenWonders(QDialog):
    NumGridRows = 1
    NumButtons = 4

    def __init__(self):
        super(SevenWonders, self).__init__()
        self.val = QSpinBox()
        self.val.setValue(0)
        self.val.setMinimum(0)

        b1 = QPushButton("-5")
        b2 = QPushButton("-1")
        b3 = QPushButton("+1")
        b4 = QPushButton("+5")
        b1_func = partial(self.increment, -5)
        b2_func = partial(self.increment, -1)
        b3_func = partial(self.increment, 1)
        b4_func = partial(self.increment, 5)
        b1.clicked.connect(b1_func)
        b2.clicked.connect(b2_func)
        b3.clicked.connect(b3_func)
        b4.clicked.connect(b4_func)
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(b1)
        self.mainLayout.addWidget(b2)
        self.mainLayout.addWidget(self.val)
        self.mainLayout.addWidget(b3)
        self.mainLayout.addWidget(b4)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Military")

    def increment(self, number):
        self.val.setValue(self.val.value() + number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # dialog = SevenWonders()
    # sys.exit(dialog.exec_())
    mainLayout = QGridLayout()
    d1 = SevenWonders()
    d2 = SevenWonders()



