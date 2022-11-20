import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from settings import GetSettings


#
# app = QApplication(sys.argv)  # create application
# dlgMain = QMainWindow()  # create main gui window
# dlgMain.setWindowTitle('MTZ v1.0')
# dlgMain.show()
#
# app.exec_()
#
#
#
# import sys
# from PyQt5.QtWidgets import *
#
# class DlgMain(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('MTZ v1.0')
#         self.resize(300, 200)
#         self.ledText = QLineEdit('123', self)
#         self.ledText.move(90, 50)
#
#         self.btnUpdate = QPushButton('update', self)
#         self.btnUpdate.move(90, 80)
#         self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)
#
#     def evt_btn_update_clicked(self):
#         self.setWindowTitle(self.ledText.text())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dlgMain = DlgMain()
#     dlgMain.show()
#     sys.exit(app.exec_())
#
#
# class DlgMain(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.resize(400, 200)
#         self.btn = QPushButton('Show Msg', self)
#         self.btn.move(35,50)
#         self.btn.clicked.connect(self.evt_btn_clicked)
#
#
#     def evt_btn_clicked(self):

#         # res = QMessageBox.question(self, 'anime', 'anime dlya pidorov')
#         #if res == QMessageBox.Yes:
#         #    QMessageBox.information(self, '', 'Yas')
#         #elif res == QMessageBox.No:
#         #    QMessageBox.information(self, '', 'No')
#
#         res = QMessageBox()
#         res.setText('anime dlya pidorov')
#         res.setIcon(QMessageBox.Information)
#         res.setWindowTitle('anime')
#         res.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#         res.exec_()
#
#
#     def evt_btn_update_clicked(self):
#         self.setWindowTitle(self.ledText.text())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dlgMain = DlgMain()
#     dlgMain.show()
#     sys.exit(app.exec_())
#
#
#
# class DlgMain(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.resize(400, 200)
#         self.btn1 = QPushButton('Show Input2', self)
#         self.btn1.move(35, 50)
#         self.btn1.clicked.connect(self.evt_btn_clicked2)
#
#         self.btn2 = QPushButton('Show Input1', self)
#         self.btn2.move(35, 15)
#         self.btn2.clicked.connect(self.evt_btn_clicked1)
#
#         self.btn3 = QPushButton('Show Input3', self)
#         self.btn3.move(35, 85)
#         self.btn3.clicked.connect(self.evt_btn_clicked3)
#
#     def evt_btn_clicked1(self):
#         get_name, b_ok = QInputDialog.getText(self, 'Title', 'Enter name')
#         if b_ok:
#             QMessageBox.information(self, 'name', 'ur name: ' + get_name)
#         else:
#             QMessageBox.information(self, 'name', 'закрыл :c')
#
#     def evt_btn_clicked2(self):
#         get_age, b_ok = QInputDialog.getInt(self, 'Title', 'age', 18, 18, 99, 1)  # дефолт минимальное максимальное шаг
#         if b_ok:
#             QMessageBox.information(self, 'name', 'ur age: ' + str(get_age))
#         else:
#             QMessageBox.information(self, 'name', 'закрыл :c')
#
#     def evt_btn_clicked3(self):
#         colors = ['orange', 'red', 'yellow', 'green', 'pink']
#         s_color, b_ok = QInputDialog.getItem(self, 'Title', 'color:', colors, editable=False)  # дефолт минимальное максимальное шаг
#         if b_ok:
#             QMessageBox.information(self, 'name', 'ur color: ' + s_color)
#         else:
#             QMessageBox.information(self, 'name', 'закрыл :c')
#             Get_settings('settings.ini')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dlgMain = DlgMain()
#     dlgMain.show()
#     sys.exit(app.exec_())


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.btn1 = QPushButton('1', self)
        self.btn1.clicked.connect(self.evt_btn_clicked)

        self.btn2 = QPushButton('2', self)
        self.btn2.clicked.connect(self.evt_btn_clicked)

        self.btn3 = QPushButton('3', self)
        self.btn3.clicked.connect(self.evt_btn_clicked)

        self.layout = QGridLayout()
        layout.addWidget(btn1, 0, 0, 1, 2, Qt.AlingHCenter)

    def evt_btn_clicked1(self):
        res = QFileDialog.getOpenFileName(self, 'Open File', 'C:', 'JPG File (*.jpg);;PNG File (*.png)')
        print(res)

    def evt_btn_clicked2(self):
        pass

    def evt_btn_clicked3(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
