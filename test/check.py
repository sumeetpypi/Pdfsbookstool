import os
import urllib

from PySide.QtGui import QSplitter
from Qt import QtWidgets, QtGui

from Qt import QtCompat
from Qt import QtCore
import sys
# from read_db import get_images, download_section
# from source import image_file
# from source.thread import download_thread
# from read_file_ftp import read_ftp
from test import view_files_details
from start_screen_thread import file_thread

title = dict()


class books_main_page(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(books_main_page, self).__init__(parent)
        self._parent = list()
        ui_file = os.path.join(os.path.dirname(__file__), 'main_ui.ui')
        self.ui = QtCompat.loadUi(ui_file, self)
        self.ui.pushButton.clicked.connect(self.send_data)

    @property
    def parent_widgets(self):
        return self._parent

    def send_data(self):
        make_path = '/project/static/books/{}/{}'.format("popular-books", "Mastering-KVM-Virtualization")
        self._parent.append(make_path)
        self.downloadThread = file_thread(parent=self)
        self.downloadThread._data.connect(self.set_progressbar_value)
        self.downloadThread.start()

    def set_progressbar_value(self, value):
        # print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> check value", value
        self.progressBar.setValue(value)
        # if value == 100:
        #     print ">> data"
        #     return


if __name__ == '__main__':
    _projects = QtWidgets.QApplication(sys.argv)
    # customDarkPalette.customDarkPalette(compliled_projects)
    app = books_main_page()
    app.show()
    sys.exit(_projects.exec_())
