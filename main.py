import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import os
from settings import GetSettings
from mtz import ShowData


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MTZ v1.0')
        self.resize(300, 200)

        self.btn1 = QPushButton('Визуализировать')
        self.btn1.clicked.connect(self.evt_btn_clicked1)
        self.btn1.setFixedHeight(35)

        self.btn2 = QPushButton('Настройки', self)
        self.btn2.clicked.connect(self.evt_btn_clicked2)
        self.btn2.setFixedHeight(35)

        self.btn3 = QPushButton('я гей', self)
        self.btn3.clicked.connect(self.evt_btn_clicked3)
        self.btn3.setFixedHeight(35)

        self.layout = QGridLayout()
        self.layout.addWidget(self.btn1, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.btn2, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.btn3, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.setLayout(self.layout)

    def evt_btn_clicked1(self):
        res = QFileDialog.getOpenFileName(self, 'Open File', 'C:', 'TXT File (*.txt)')
        try:
            if res[0][-4:] == '.txt':
                ShowData(res[0])
        except:
            pass

    def evt_btn_clicked2(self):
        pass

    def evt_btn_clicked3(self):
        get_age, b_ok = QMessageBox.question(self, 'anime', 'у меня не друзей, у меня не друзей, у меня не друзей, у меня не друзей, у меня не друзей, у меня не друзей, ')
        if b_ok:
            self.close()
        else:
            self.close()


if __name__ == '__main__':
    if not os.path.exists('temp'):
        os.mkdir('temp')
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('static/mgri.ico'))
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
