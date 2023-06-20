import json
import os
import urllib
from functools import partial
import PIL
import Qt
from PySide.QtGui import QSplitter
from Qt import QtWidgets, QtGui
from Qt import QtCompat
from read_db import get_file_details
from read_file_ftp import read_ftp
from source import collection_path
from Qt import QtCore
import sys
import time

image_ = dict()


class serach_from_db(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(serach_from_db, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), 'search_db.ui')
        self.ui = QtCompat.loadUi(ui_file, self)
        self.parent = parent
        self.show()
        self.connection()
        self.view_details()

    @property
    def close(self):
        return self.close()

    def connection(self):
        # self.parent.ui.listWidget_2.customContextMenuRequested.connect(lambda x: self.context_menu(self.parent.ui.listWidget_2, x))
        self.ui.download_queue.clicked.connect(self.add_to_download_queue)

    def exit_button(self):
        self.exit()

    def view_details(self):
        file_text = self.parent.data_names
        print ">>>> check dict", file_text
        file_name = file_text.get('title')
        file_data = get_file_details(title=file_name)
        print file_data
        for details in file_data:
            print ">>>> sql data", details
            title_ = details[1]
            image = details[0]
            category = details[6]
            description = details[4]

            title_ = "{}".format(title_)
            categories_ = "{}".format(category)
            make_title = title_.replace(" ", "-")
            make_category = categories_.replace(" ", "-")
            make_file_name = "{}.jpg".format(make_title)
            make_link = "https://www.techpdfs.com/static/books/{}/{}/{}".format(make_category, make_title,
                                                                                make_file_name)
            data = urllib.urlopen(make_link).read()

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(data)

            image_['image'] = pixmap
            title_format = "{}".format(title_)
            image_['title'] = title_

            # description_ = "Description: {}".format(description)
            self.ui.main_image_2.setPixmap(pixmap.scaled(220, 200, QtCore.Qt.KeepAspectRatio,
                                                         QtCore.Qt.SmoothTransformation))
            self.ui.title.setText(title_format)
            self.ui.description.setPlainText(description)
            # self.ui.description.setWordWrap(True)

    def add_to_download_queue(self):
        collection_data = dict()
        original_dict = dict()
        data_list = list()

        image = image_.get('image')
        title = image_.get('title')
        list_count = self.parent.ui.listWidget_2.count()
        for i in range(list_count):
            get_text = self.parent.ui.listWidget_2.item(i).text()
            if title in get_text:
                return

        item = QtWidgets.QListWidgetItem(image, title)
        item.setBackground(QtGui.QColor('#D8DEE4'))
        self.parent.ui.listWidget_2.setSpacing(4)
        original_dict[title] = str(image)
        collection_data["books"] = list()
        collection_data["books"].append(original_dict)
        data = json.dumps(collection_data, indent=4)
        # if not os.path.exists(collection_path()):
        #     os.makedirs(collection_path())
        #     time.sleep(1)
        #     make_path = os.path.join(collection_path(), "collection.json")
        #     with open(make_path, "w") as outfile:
        #         outfile.write(data)
        #
        # if os.path.exists(collection_path()):
        #     make_path = os.path.join(collection_path(), "collection.json")
        #     with open(make_path, "r") as outfile_:
        #         get_data = json.load(outfile_)
        #         with open(make_path, "w") as outfile:
        #             data = json.dumps(collection_data, indent=4)
        #             get_data["books"].append(data)
        #             outfile.write(get_data)

        self.parent.ui.listWidget_2.addItem(item)
