import os
import sys
import math

import farabi
from dynamic import dynamic

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QLabel, QLineEdit, QPushButton)

sys.path.append(os.path.abspath('.')+'/plugins')

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Escape:
            self.clear()
        else:
            super().keyPressEvent(event)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.globs = {'dynam':dynamic}

        mathDir = dir(math)
        for x in mathDir:
            if not x.startswith('_'):
                self.globs[x] = eval('math.'+x)
        fbDir = dir(farabi)
        for x in fbDir:
            if not x.startswith('_'):
                self.globs[x] = eval('farabi.'+x)

        exec('class dynam(dynam):\n\tdef eval(self):\n\t\treturn eval(self.val)', self.globs)
        self.globs['sqrt'] = sqrt

        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(2,2,2,2)
        self.setLayout(self.layout)

        if getattr(sys, 'frozen', False):
            icon = QIcon(os.path.join(sys._MEIPASS, "Sculator.ico"))
        else:
            icon = QIcon("Sculator.ico")

        self.setWindowIcon(icon)
        self.setWindowTitle('sculator')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.createApp()
        self.show()
    def createApp(self):
        font = QFont()
        font.setPointSize(9)

        txt = QLabel('Enter your equation: ')
        ent = LineEdit()
        ent.setFont(font)
        ent.returnPressed.connect(lambda: self.equation(ent.text()))
        btn = QPushButton('ok')
        btn.clicked.connect(lambda: self.equation(ent.text()))
        self.lbl = QLabel('None')
        self.lbl.setFont(font)
        self.lbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(txt)
        self.layout.addWidget(ent,0,1)
        self.layout.addWidget(btn,0,2)
        self.layout.addWidget(self.lbl,1,1)
    def equation(self,txt):
        self.lbl.setStyleSheet('color: black')
        try:
            out = eval(txt,self.globs)
            self.lbl.setText(str(out))
        except:
            try:
                exec(txt,self.globs)
                self.lbl.setText('Done')
            except Exception as e:
                self.lbl.setStyleSheet('color: red')
                self.lbl.setText(str(e))

def sqrt(num, forge=2):
    return round(num**(1/forge))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    app.exec_()
