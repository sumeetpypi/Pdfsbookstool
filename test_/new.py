import json
import os
from PySide.QtGui import QSplitter
from Qt import QtWidgets, QtGui
from Qt import QtCompat
from Qt import QtCore

import sys
import time

image_ = dict()


class view_files_details(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(view_files_details, self).__init__(parent)
        ui_file = os.path.join(os.path.dirname(__file__), 'test_.ui')
        QtCompat.loadUi(ui_file, self)
        self.signals()


    def signals(self):
        self.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        self.label.setText("we all are one")


if __name__ == "__main__":
    _projects = QtWidgets.QApplication(sys.argv)
    app = view_files_details()
    app.show()
    sys.exit(_projects.exec_())
