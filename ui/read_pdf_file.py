import os
import urllib
import PyPDF2
from PySide.QtGui import QSplitter
from Qt import QtWidgets, QtGui
from Qt import QtCompat
from Qt import QtCore
import sys
from read_db import get_images, download_section, slider_data
from source import image_file
from source.thread import download_thread
from source.thread import files_thread
from read_file_ftp import read_ftp
from view_files import view_files_details
from images_panel import image_panel

title = dict()
data_list = list()



class read_pdf(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(read_pdf, self).__init__(parent)
        ui_file = os.path.join(os.path.dirname(__file__), 'read_pdf.ui')
        self.ui = QtCompat.loadUi(ui_file, self)
        self.slots_signals()

    def slots_signals(self):
        self.ui.add_file.clicked.connect(self.get_existing_dir)

    def get_existing_dir(self):
        selected_dir = QtWidgets.QFileDialog.getOpenFileName(self, caption='Choose Directory',
                                                                  directory=os.getcwd())

        print selected_dir

        pdfFileObj = open(selected_dir[0], 'rb')

        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            vertical_layout = QtWidgets.QVBoxLayout()
            plainText = QtWidgets.QTextEdit()
            data = pageObj.extractText()

            plainText.setPlainText(data)

            vertical_layout.addWidget(plainText)
            self.ui.verticalLayout_2.addLayout(vertical_layout)






if __name__ == '__main__':
    _projects = QtWidgets.QApplication(sys.argv)
    # customDarkPalette.customDarkPalette(compliled_projects)
    app = read_pdf()
    app.show()
    sys.exit(_projects.exec_())
