import os
import urllib

from PySide6.QtWidgets import QSplitter
from Qt import QtWidgets, QtGui

from Qt import QtCompat
from Qt import QtCore
import sys
from read_db import get_images, download_section, slider_data
import read_d
from source.thread import download_thread
from source.thread import files_thread
from read_file_ftp import read_ftp
from view_files import view_files_details
from images_panel import image_panel

title = dict()
data_list = list()


class books_main_page(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(books_main_page, self).__init__(parent)
        ui_file = os.path.join(os.path.dirname(__file__), 'main_ui.ui')
        self.ui = QtCompat.loadUi(ui_file, self)
        self._manager = parent
        self._parent = parent
        self.name = dict()
        # self.get_screen_size()
        self.progressBar = QtWidgets.QProgressBar(minimumWidth=50)
        self.progressBar.setValue(0)
        self.progressBar.setGeometry(150, 150, 150, 20)
        self.btn = QtWidgets.QPushButton("download")
        self.setWindowTitle('Download Books')
        self.image_text = None
        self.links = dict()
        self.downloadThread = None
        self.rows = dict()
        self._links = list()
        self._row_list = list()
        self.add_spliter()
        self.show_images()
        self.signals_slots()
        self.files_thread()
        # self.add_button_in_list()
        # self.ui.frame_2.hide()

    def get_screen_size(self):
        self.screen_count = QtWidgets.QDesktopWidget().screenCount()
        # self.w = QtWidgets.QDesktopWidget.screenGeometry(self.screen_count)
        return QtWidgets.QDesktopWidget.availableGeometry(self.screen_count)

    def files_thread(self):
        self.files_threads = files_thread.files_thread(parent=self)
        self.files_threads.start()

    @property
    def data_names(self):
        return self.name

    @property
    def progress(self):
        return self.progressBar

    # @property
    # def data_names(self):
    #     return self._parent

    @property
    def download(self):
        return self._links

    def add_spliter(self):
        spliter = QSplitter()
        spliter_2 = QSplitter()
        widget = self.ui.scrollArea_2
        categories = self.ui.scrollArea_3
        # section_1 = self.ui.scrollArea_3
        # section_2 = self.ui.scrollArea_4
        widget_2 = self.ui.books_2
        spliter.addWidget(widget)
        spliter.addWidget(categories)
        spliter.addWidget(widget_2)

        # spliter_2.addWidget(section_1)
        # spliter_2.addWidget(section_2)
        data = self.ui.splitter
        data.addWidget(spliter)

    def signals_slots(self):
        self.ui.start_download_4.clicked.connect(self._download)
        self.ui.listWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.listWidget_2.customContextMenuRequested.connect(lambda x: self.context_menu(self.ui.listWidget_2, x))
        self.ui.listWidget.currentItemChanged.connect(self.get_text_1)
        self.ui.listWidget_4.currentItemChanged.connect(self.get_text_2)
        self.ui.slider.clicked.connect(self.add_button_in_list)
        self.ui.search_button.clicked.connect(self.search_items)
        self.ui.slider_2.clicked.connect(self.search_slider)

    def _connections(self):
        self.thread()

    def get_images(self, args):
        images = get_images(category=args)
        return images

    def books(self):
        image_list = []
        self.images = read_ftp()
        images = self.images.data_1()

        for data in images:
            data_dict = dict()
            image = data.get("path")
            title = data.get("title")
            make_title = str(title)[0:14]
            data = urllib.request.urlopen(image).read()
            title_ = '{}...'.format(make_title)

            Image2 = QtGui.QImage()
            Image2.loadFromData(data)
            pixmap = QtGui.QPixmap.fromImage(Image2).scaled(150, 110, QtCore.Qt.KeepAspectRatio,
                                                            QtCore.Qt.SmoothTransformation)

            data_dict[title_] = pixmap

            image_list.append(data_dict)

        return image_list

        # pixmap.fromImage(Image2)
        # item = QtWidgets.QListWidgetItem(pixmap, "sumeet")
        # item.setBackground(QtGui.QColor('#b2ad7f'))
        # self.ui.listWidget.setSpacing(4)
        # self.ui.listWidget.addItem(item)

        # self.images = read_ftp()
        # images = self.images.data_3()
        # print "check images", images
        # for data in images:
        #     image = data.get("image")
        #     title = data.get("title")
        #     make_title = str(title)[0:14]
        #     title_ = '{}...'.format(make_title)
        #     Image2 = QtGui.QImage()
        #     Image2.loadFromData(image.getvalue())
        #     pixmap = QtGui.QPixmap.fromImage(Image2).scaled(120, 120, QtCore.Qt.KeepAspectRatio,
        #                                                     QtCore.Qt.SmoothTransformation)
        #
        #     vertical_layout = QtWidgets.QVBoxLayout()
        #     horizontal_layout = QtWidgets.QHBoxLayout()
        #     image_label = QtWidgets.QLabel()
        #     image_label.setScaledContents(True)
        #     self.image_text = QtWidgets.QPushButton(title)
        #
        #     self.image_text.setStyleSheet('width:20px; background-color:transparent')
        #     image_label.setPixmap(pixmap)
        #
        #     vertical_layout.addWidget(image_label)
        #     vertical_layout.addWidget(self.image_text)
        #
        #     self.ui.horizontalLayout_5.addLayout(vertical_layout)

        # pixmap.fromImage(Image2)
        # item = QtWidgets.QListWidgetItem(pixmap, "sumeet")
        # item.setBackground(QtGui.QColor('#b2ad7f'))
        # self.ui.listWidget.setSpacing(4)
        # self.ui.listWidget.addItem(item)

    def books_details_section(self):
        item = self.ui.listWidget.currentItem().text()
        data = download_section(title=item)
        for data_ in data:
            title_ = '{}'.format(data_[1])
            data = urllib.urlopen(data_[0]).read()
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(data)
            self.ui.image.setPixmap(pixmap)
            description = "Description: {}".format(data_[4])
            file_size = "File Size: {}".format(data_[2])
            pages = "pages: {}".format(data_[3])
            formating = "Format: {}".format("PDF")
            language = "Language: {}".format("English")
            self.ui.title.setText(title_)
            self.ui.description.setPlainText(description)
            self.ui.filesize.setText(file_size)
            self.ui.pages.setText(pages)
            self.ui.format.setText(formating)
            self.ui.language.setText(language)
            image_ = self.read_image()
            button_icon = QtGui.QPixmap(image_)
            self.ui.title.setIcon(QtGui.QIcon(button_icon))

    def _download(self):
        get_images = image_file()
        pause_image = os.path.join(get_images, "icons8-pause-50.png")
        start_button = os.path.join(get_images, "icons8-start-50 (1).png")

        row_list = list()
        find_word = self.ui.tableWidget.findItems("Queued", QtCore.Qt.MatchExactly)
        for i in find_word:
            self.data_link = dict()
            rows = i.row()
            text = self.ui.tableWidget.item(rows, 0).text()
            text_1 = self.ui.tableWidget.item(rows, 1).text()
            self.data_link['title'] = text
            self.data_link['category'] = text_1
            self._links.append(self.data_link)

        self.downloadThread = download_thread.file_thread(parent=self)
        self.downloadThread._data.connect(self.set_progressbar_value)
        self.downloadThread.rows.connect(self.get_rows)
        self.downloadThread.start()
        self.ui.start_download_4.setIcon(QtGui.QIcon(pause_image))
        if self.ui.start_download_4.isChecked():
            self.ui.start_download_4.setIcon(QtGui.QIcon(pause_image))

        # self.ui.listWidget_2.itemActivated.connect(self.add_to_download)
        # self.ui.tableWidget.setCellWidget(0, 2, progressBar)
        # item_title = self.ui.tableWidget.item(current_row, 0)
        # item_category = self.ui.tableWidget.item(current_row, 1)
        # titles = item_title.text()
        # self.links["title"] = item_title
        # self.links["category"] = item_category

    def get_rows(self, rows):
        self.rows['rows'] = rows

    def add_to_download(self):
        list_items = dict()
        current_list_widget = self.ui.listWidget_2.currentRow()
        get_text = self.ui.listWidget_2.item(current_list_widget).text()

        _count = self.ui.tableWidget.rowCount()
        for i in range(_count):

            variable_text = self.ui.tableWidget.item(i, 0).text()
            if get_text in variable_text:
                return

        data = download_section(title=get_text)
        for data_items in data:
            tittle_ = data_items[1]

            size_ = data_items[2]
            category = data_items[0]


            _title = QtWidgets.QTableWidgetItem(tittle_)
            category_ = QtWidgets.QTableWidgetItem(category)
            status = QtWidgets.QTableWidgetItem("Queued")
            row_cout = self.ui.tableWidget.rowCount()

            self.ui.tableWidget.insertRow(row_cout)
            self.ui.tableWidget.setItem(row_cout, 0, _title)
            self.ui.tableWidget.setItem(row_cout, 1, category_)
            self.ui.tableWidget.setItem(row_cout, 3, status)
            # self.ui.tableWidget.setCellWidget(row_cout, 2, self.btn)
            # current_row = self.ui.tableWidget.currentRow()

    def get_download_state(self):
        current_row = self.ui.tableWidget.currentRow()
        return current_row

    # def download_thread(self):
    #     current_row = self.ui.tableWidget.currentRow()
    #     self.ui.tableWidget.setCellWidget(current_row, 3, self.progressBar)
    #     # self.ui.tableWidget.setCellWidget(0, 2, progressBar)
    #     item_title = self.ui.tableWidget.item(current_row, 0)
    #     item_category = self.ui.tableWidget.item(current_row, 1)
    #     titles = item_title.text()
    #     self.links["title"] = item_title
    #     self.links["category"] = item_category
    #
    #     self.downloadThread = download_thread.file_thread(parent=self)
    #     self.downloadThread._data.connect(self.set_progressbar_value)
    #     self.downloadThread.start()

    def set_progressbar_value(self, value):
        try:
            self.progressBar.setValue(value)
            if value == 100:
                rows = self.rows.get('rows')
                _title = QtWidgets.QTableWidgetItem("Done")
                self.ui.tableWidget.setItem(rows, 3, _title)

                if self.downloadThread.isFinished():

                    del self._links[:]
                    self.downloadThread.exit()

        except:
            pass

    def remove_file_from_list(self):
        current_list_widget = self.ui.listWidget_2.currentRow()

        self.ui.listWidget_2.takeItem(current_list_widget)

    def context_menu(self, widget, position):
        # image = image_file()
        # image_path = os.path.join(image, "delete.png")
        item = widget.itemAt(position)
        menu = QtWidgets.QMenu()
        remove_action = menu.addAction("Delete")
        add_to_download = menu.addAction("Download")
        remove_action.triggered.connect(lambda: self.remove_file_from_list())
        add_to_download.triggered.connect(self.add_to_download)
        menu.exec_(widget.mapToGlobal(position))

    def books(self):
        image_list = []
        self.images = read_ftp()
        images = self.images.data_1()

        for data in images:
            data_dict = dict()
            image = data.get("path")
            title = data.get("title")
            time_stamp = data.get(("time_stamp"))
            make_title = str(title)[0:14]
            data = urllib.urlopen(image).read()
            title_ = '{}'.format(title)
            Image2 = QtGui.QImage()
            Image2.loadFromData(data)
            pixmap = QtGui.QPixmap.fromImage(Image2).scaled(150, 110, QtCore.Qt.KeepAspectRatio,
                                                            QtCore.Qt.SmoothTransformation)

            data_dict[title_] = pixmap
            # data_dict["time_stamp"] = time_stamp

            image_list.append(data_dict)
        return image_list

    def show_images(self):
        image_list = self.books()
        for data in image_list:
            for keys, v in data.items():



                icon = QtGui.QIcon(data.get(keys))

                item_ = QtWidgets.QListWidgetItem()
                item_.setIcon(icon)
                item_.setToolTip(keys)
                # item_.setVisible(True)
                # item.setBackground(QtGui.QColor('#b2ad7f'))
                size = QtCore.QSize(220, 200)
                self.ui.listWidget.setIconSize(size)
                self.ui.listWidget.setSpacing(4)
                self.ui.listWidget.addItem(item_)

    def books_(self):
        image_list = []
        # images = self.add_button_in_list()
        # print "check images", images
        for data in data_list:
            data_dict = dict()
            image = data.get("path")
            title = data.get("title")
            time_stamp = data.get(("time_stamp"))
            make_title = str(title)[0:14]
            data = urllib.urlopen(image).read()
            title_ = '{}'.format(title)
            Image2 = QtGui.QImage()
            Image2.loadFromData(data)
            pixmap = QtGui.QPixmap.fromImage(Image2).scaled(150, 110, QtCore.Qt.KeepAspectRatio,
                                                            QtCore.Qt.SmoothTransformation)

            data_dict[title_] = pixmap
            # data_dict["time_stamp"] = time_stamp

            image_list.append(data_dict)
        return image_list

    def show_images_(self):
        image_list = self.books_()
        for data in image_list:
            for keys, v in data.items():


                icon = QtGui.QIcon(data.get(keys))

                item_ = QtWidgets.QListWidgetItem()
                item_.setIcon(icon)
                item_.setToolTip(keys)
                # item_.setVisible(True)
                # item.setBackground(QtGui.QColor('#b2ad7f'))
                size = QtCore.QSize(220, 200)
                self.ui.listWidget.setIconSize(size)
                self.ui.listWidget.setSpacing(4)
                self.ui.listWidget.addItem(item_)

    def show_search_images_(self):
        image_list = self.books_()
        for data in image_list:
            for keys, v in data.items():

                icon = QtGui.QIcon(data.get(keys))

                item_ = QtWidgets.QListWidgetItem()
                item_.setIcon(icon)
                item_.setToolTip(keys)
                # item_.setVisible(True)
                # item.setBackground(QtGui.QColor('#b2ad7f'))
                size = QtCore.QSize(220, 200)
                self.ui.listWidget_4.setIconSize(size)
                self.ui.listWidget_4.setSpacing(4)
                self.ui.listWidget_4.addItem(item_)

    def add_button_in_list(self):
        del data_list[:]
        rowcount = self.ui.listWidget.count()
        number_list = list()
        for i in range(rowcount):
            number_list.append(i)
            data = self.ui.listWidget.item(i).toolTip()

        data_ = self.ui.listWidget.item(max(number_list)).toolTip()
        self.images = read_ftp()
        images = self.images.data_2(title=data_, category="popular books")
        for data in images:
            data_list.append(data)

        self.books_()

        self.show_images_()

    def search_slider(self):
        del data_list[:]
        rowcount = self.ui.listWidget_4.count()
        number_list = list()
        for i in range(rowcount):
            number_list.append(i)
            data = self.ui.listWidget_4.item(i).toolTip()

        data_ = self.ui.listWidget_4.item(max(number_list)).toolTip()

        self.images = read_ftp()
        images = self.images.search_slider_(title=data_)
        for data in images:
            data_list.append(data)

        self.books_()

        self.show_search_images_()

    def search_items(self):
        del data_list[:]
        self.ui.listWidget_4.clear()
        text = self.ui.search_item.text()
        self.images = read_ftp()
        images = self.images.search_data_(title=text)
        for data in images:
            data_list.append(data)

        self.books_()

        self.show_search_images_()

    def get_text_1(self):
        # self.data = self.text.text()
        # print  ">>>>>>>>> check name", self.data
        current_row = self.ui.listWidget.currentRow()
        # self.data = self.ui.listWidget.item(current_row).text()
        self.data = self.ui.listWidget.item(current_row).toolTip()

        self.name['title'] = self.data
        self.file_name = view_files_details(self)
        self.file_name.show()

    def get_text_2(self):
        # self.data = self.text.text()
        # print  ">>>>>>>>> check name", self.data
        current_row = self.ui.listWidget_4.currentRow()
        # self.data = self.ui.listWidget.item(current_row).text()
        self.data = self.ui.listWidget_4.item(current_row).toolTip()

        self.name['title'] = self.data
        self.file_name = view_files_details(self)
        self.file_name.show()

    def read_image(self):
        icon = image_file()
        path = os.path.join(icon, 'pdf.png')
        return path


if __name__ == '__main__':
    _projects = QtWidgets.QApplication(sys.argv)
    # customDarkPalette.customDarkPalette(compliled_projects)
    app = books_main_page()
    app.show()
    sys.exit(_projects.exec_())
