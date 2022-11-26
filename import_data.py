import sys
import os
import webbrowser
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGridLayout, QFileDialog, QMessageBox
from convert_to_txt import ConvertExcelToTxt


class ChooseFile(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.file_path = ""

        self.configure_window()  # Method to configure window parameters

        self.layout = QGridLayout()  # Defining layouts for PyQt5 window

        # Defining menu_layout variables
        self.btn1 = QPushButton("Выбрать файл", self)
        self.btn2 = QPushButton("Документация", self)
        self.btn3 = QPushButton("Справка", self)

        self.layouts_configure()  # Method to configure layouts

        self.show()

    # Method to config main window
    def configure_window(self):
        self.setWindowTitle('MTZ v1.0')
        self.resize(480, 160)

    # Method to configure layouts interposition and their relations
    def layouts_configure(self):
        self.btn1.clicked.connect(self.choose_file_button_ev)
        self.btn1.setFixedHeight(35)

        self.btn2.clicked.connect(self.documentation_button)
        self.btn2.setFixedHeight(35)

        self.btn3.clicked.connect(self.evt_btn_clicked3)
        self.btn3.setFixedHeight(35)

        self.layout.addWidget(self.btn1, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.btn2, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.btn3, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)

        self.setLayout(self.layout)

    # Method to get path to file for future work
    def choose_file_button_ev(self):
        file_path_temp = self.choose_file()
        if file_path_temp is None:
            return
        self.file_path = file_path_temp
        self.switch()

    # Method to choose .txt or .xlsx file from interactive window
    def choose_file(self) -> str or None:
        res = QFileDialog.getOpenFileName(self, 'Open File', 'C:', 'Data files (*.xlsx *.txt)')
        try:
            if res[0][-4:] == '.txt':
                return res[0]
            elif res[0][-5:] == '.xlsx':
                converted_file = ConvertExcelToTxt(res[0])
                if converted_file.status:
                    return converted_file.output_file_path
                else:
                    print("Something gone wrong, read text upper")
                    return None
            else:
                print("Wy did you break file manager window?")
                return None
        except Exception as err:
            print(err)
            return None

    # Placeholder for button 3 future function
    def evt_btn_clicked3(self):
        get_age, b_ok = QMessageBox.question(self, 'Справка', '12134')
        try:
            if b_ok:
                self.close()
            else:
                self.close()
        except Exception as err:
            print(err)

    def switch(self):
        self.switch_window.emit(self.file_path)

    def error_window(self):
        pass

    # Method to open documentation link in browser
    @staticmethod
    def documentation_button():
        webbrowser.open('https://dipperok.github.io/mtz_kursivaya_documentation/')


if __name__ == '__main__':
    if not os.path.exists('temp'):
        os.mkdir('temp')
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('static/mgri.ico'))
    dlgMain = ChooseFile()
    dlgMain.show()
    sys.exit(app.exec_())
