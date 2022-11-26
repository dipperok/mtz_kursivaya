import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mtz import ShowData

matplotlib.use('Qt5Agg')


class VisualMTZ(QWidget):
    def __init__(self, file_path):

        super(VisualMTZ, self).__init__()

        self.file_path = file_path
        print(self.file_path)

        self.configure_window()  # Method to configure window parameters

        # Defining layouts for PyQt5 window
        self.layout = QGridLayout()
        self.menu_layout = QGridLayout()
        self.graph_layout = QVBoxLayout()

        # Defining menu_layout variables
        self.btn1 = QPushButton("Визуализировать 1", self)
        self.btn2 = QPushButton("Визуализировать 2", self)
        self.btn3 = QPushButton("Визуализировать 3", self)
        self.btn4 = QPushButton("Визуализировать 4", self)

        self.create_menu_layout()  # method to configure menu_layout dependencies

        # Defining graph_layout and matplotlib variables
        self.figure, self.axs = plt.subplots(1, figsize=(5, 5), constrained_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.cb = None

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

        self.btn2.clicked.connect(self.visual_mtz_file)
        self.btn2.setFixedHeight(35)

        self.btn3.clicked.connect(self.visual_mtz_file)
        self.btn3.setFixedHeight(35)

        self.btn4.clicked.connect(self.visual_mtz_file)
        self.btn4.setFixedHeight(35)

        self.menu_layout.addWidget(self.btn1, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn2, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn3, 0, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn4, 0, 3, 1, 2, QtCore.Qt.AlignHCenter)

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

    # Method to visualisation mtz file
    def visual_mtz_file(self):
        if self.cb:
            self.figure.delaxes(self.figure.axes[1])

        file_data = ShowData(self.file_path)  # Object with calculated vars for mtz file

        # Configuration graph view
        self.axs.set_xticks(file_data.position_y)
        self.axs.set_yticks(file_data.position_z)
        self.axs.set_xticklabels(file_data.list_x)
        self.axs.set_yticklabels(file_data.list_y)
        self.axs.set_xlim([0, file_data.position_y[-1]])
        self.axs.set_ylim([file_data.position_z[-1], 0])

        # Creating graph
        p2 = self.axs.imshow(file_data.rho, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
        self.cb = self.figure.colorbar(p2, ax=self.axs)
        self.figure.canvas.draw()

    def error_window(self):
        pass