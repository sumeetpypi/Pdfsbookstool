import os
import urllib

# from PySide.QtGui import QSplitter
from Qt import QtWidgets, QtGui, Qt

from Qt import QtCompat
from Qt import QtCore
import sys
from read_db import get_images, download_section
from source import image_file
from read_file_ftp import read_ftp
from view_files import view_files_details


class image_panel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(image_panel, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), 'images_panel.ui')
        self.ui = QtCompat.loadUi(ui_file, self)
        self.name = dict()
        self.text = None
        self.show_images()
        self.signals_slots()

    @property
    def data_names(self):
        return self.name

    def books(self):
        image_list = []
        self.images = read_ftp()
        images = self.images.data_1()

        for data in images:
            data_dict = dict()
            image = data.get("path")
            title = data.get("title")
            make_title = str(title)[0:14]
            data = urllib.urlopen(image).read()
            title_ = '{}...'.format(make_title)

            Image2 = QtGui.QImage()
            Image2.loadFromData(data)
            pixmap = QtGui.QPixmap.fromImage(Image2).scaled(150, 110, QtCore.Qt.KeepAspectRatio,
                                                            QtCore.Qt.SmoothTransformation)

            data_dict[title_] = pixmap

            image_list.append(data_dict)

        return image_list

    def show_images(self):

        image_list = self.books()
        for data in image_list:
            for k, v in data.items():
                # print k
                # print ">>>>>>>>>>>>>>>>>> show image" , data.get(k)
                layout = QtWidgets.QVBoxLayout()
                # self.image = QtWidgets.QPushButton()
                # self.text = QtWidgets.QPushButton()
                #
                # self.image.setIcon(data.get(k))
                # self.image.setStyleSheet("background-color: transparent; width:60px;")
                # self.image.setIconSize(QtCore.QSize(150, 110))
                # self.text.setText(k)
                # self.text.setStyleSheet("background-color: transparent; ")
                #
                # layout.addWidget(self.image)
                #
                # layout.addWidget(self.text)
                #
                # self.ui.horizontalLayout.addLayout(layout)
                icon = QtGui.QIcon(data.get(k))
                item_ = QtWidgets.QListWidgetItem()
                item_.setIcon(icon)
                item_.setToolTip(k)
                # item_.setVisible(True)
                # item.setBackground(QtGui.QColor('#b2ad7f'))
                size = QtCore.QSize(220, 200)
                self.ui.listWidget.setIconSize(size)
                self.ui.listWidget.setSpacing(4)
                self.ui.listWidget.addItem(item_)


    def get_text_1(self):
        self.close()
        # self.data = self.text.text()
        # print  ">>>>>>>>> check name", self.data
        current_row = self.ui.listWidget.currentRow()
        # self.data = self.ui.listWidget.item(current_row).text()
        self.data = self.ui.listWidget.item(current_row).toolTip()

        self.name['title'] = self.data
        self.file_name = view_files_details(self)
        self.file_name.show()

    def signals_slots(self):
        self.ui.listWidget.currentItemChanged.connect(self.get_text_1)


if __name__ == '__main__':
    _projects = QtWidgets.QApplication(sys.argv)
    # customDarkPalette.customDarkPalette(compliled_projects)
    app = image_panel()
    app.show()
    sys.exit(_projects.exec_())
