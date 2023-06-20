import os
import urllib
from functools import partial
import PIL
import Qt
from PySide.QtGui import QSplitter
from Qt import QtWidgets, QtGui
from Qt import QtCompat
from Qt import QtCore

import sys

list = [1, 2, 3, 4, 4, 5, 6, 6]


class view_thread(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(view_thread, self).__init__(parent)
        ui_file = os.path.join(os.path.dirname(__file__), 'start_application.ui')
        self.ui = QtCompat.loadUi(ui_file, self)
        self._manager = parent
        self.data()
        # self.thread = file_thread(parent=self)
        # self.thread.start_.connect(self.data)
        # self.ui.progressBar.setValue(0)
        # self.thread.start()

    def data(self):
        self.ui.verticalLayout.addWidget(books_main_page())


if __name__ == '__main__':
    _projects = QtWidgets.QApplication(sys.argv)
    app = view_thread()
    app.show()
    sys.exit(_projects.exec_())
