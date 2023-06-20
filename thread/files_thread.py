# from Qt import QtWidgets, QtGui, QtCore
# from Qt import QtCompat
from PyQt5.QtWidgets import *

from PyQt5 import uic, QtWidgets, QtCore, QtGui
from source.ui import read_db
from source import download_location
import requests
import os
import time
import stat

link_ = []
path_list = list()


class files_thread(QtCore.QThread):
    _data = QtCore.Signal(int)
    rows = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(files_thread, self).__init__(parent)
        self._manager = parent

    def run(self):
        while True:
            location = download_location()
            get_fils = os.listdir(location)
            for files in get_fils:
                if files not in path_list:
                    path_list.append(get_fils)


        for data in path_list:
            self._manager.ui.listWidget_3.addItem(data)






