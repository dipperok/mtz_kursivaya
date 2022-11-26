import sys
import os
from PyQt5 import QtWidgets, QtGui

from import_data import ChooseFile
from visual_data import VisualMTZ


class AppController:
    def __init__(self):
        self.first_window = None
        self.second_window = None
        pass

    def intro_window(self):
        self.first_window = ChooseFile()
        self.first_window.switch_window.connect(self.graph_window)
        self.first_window.show()

    def graph_window(self, path_to_working_file):
        self.second_window = VisualMTZ(path_to_working_file)
        self.first_window.close()
        self.second_window.show()


def main():
    if not os.path.exists('temp'):
        os.mkdir('temp')

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('static/mgri.ico'))

    controller = AppController()
    controller.intro_window()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
