import sys
import os
import matplotlib
import matplotlib.pyplot as plt
import webbrowser
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QGridLayout, QFileDialog, QMessageBox
from pathlib import Path
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from mtz import ShowData
from convert_to_txt import ConvertExcelToTxt
from settings import GetSettings

matplotlib.use('Qt5Agg')


class DlgMain(QDialog):
    def __init__(self):
        super(DlgMain, self).__init__()

        self.configure_window()  # Method to configure window parameters

        # Defining layouts for PyQt5 window
        self.layout = QGridLayout()
        self.menu_layout = QGridLayout()
        self.graph_layout = QVBoxLayout()

        # Defining menu_layout variables
        self.btn1 = QPushButton("Визуализировать")
        self.btn2 = QPushButton("Документация", self)
        self.btn3 = QPushButton("Справка", self)

        self.create_menu_layout()  # method to configure menu_layout dependencies

        # Defining graph_layout and matplotlib variables
        self.figure, self.axs = plt.subplots(1, figsize=(5, 5), constrained_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.create_graph_layout()  # method to configure graph_layout dependencies

        self.layouts_configure()  # Method to configure layouts

        self.show()

    # Method to config main window
    def configure_window(self):
        self.setWindowTitle('MTZ v1.0')
        self.resize(1920, 1080)

    # Method to configure menu_layout vars and their alignments
    def create_menu_layout(self):
        self.btn1.clicked.connect(self.visual_mtz_file)
        self.btn1.setFixedHeight(35)

        self.btn2.clicked.connect(self.evt_btn_clicked2)
        self.btn2.setFixedHeight(35)

        self.btn3.clicked.connect(self.evt_btn_clicked3)
        self.btn3.setFixedHeight(35)

        self.menu_layout.addWidget(self.btn1, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn2, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn3, 0, 2, 1, 2, QtCore.Qt.AlignHCenter)

    # Method to configure graph_layout vars and their alignments
    def create_graph_layout(self):
        self.graph_layout.addWidget(self.toolbar)
        self.graph_layout.addWidget(self.canvas)

    # Method to configure layouts interposition and their relations
    def layouts_configure(self):
        self.layout.addLayout(self.graph_layout, 0, 0)
        self.layout.addLayout(self.menu_layout, 1, 0)
        self.setLayout(self.layout)

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

    # Method to visualisation mtz file
    def visual_mtz_file(self):
        file_path = self.choose_file()

        if file_path is None:
            return

        file_data = ShowData(file_path)  # Object with calculated vars for mtz file

        # Configuration graph view
        self.axs.set_xticks(file_data.position_y)
        self.axs.set_yticks(file_data.position_z)
        self.axs.set_xticklabels(file_data.list_x)
        self.axs.set_yticklabels(file_data.list_y)
        self.axs.set_xlim([0, file_data.position_y[-1]])
        self.axs.set_ylim([file_data.position_z[-1], 0])

        # Creating graph
        p2 = self.axs.imshow(file_data.rho, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
        self.figure.colorbar(p2, ax=self.axs)
        self.figure.canvas.draw()

    def error_window(self):
        pass

    # Method to open documentation link in browser
    @staticmethod
    def evt_btn_clicked2():
        webbrowser.open('https://dipperok.github.io/mtz_kursivaya_documentation/')


if __name__ == '__main__':
    if not os.path.exists('temp'):
        os.mkdir('temp')
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('static/mgri.ico'))
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
