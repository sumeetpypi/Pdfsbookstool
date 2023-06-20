
from source import download_location
import requests
import os
from PyQt5 import QtWidgets, QtGui, QtCore

import time


link_ = []
path_list = list()


class file_thread(QtCore.QThread):
    _data = QtCore.Signal(int)
    rows = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(file_thread, self).__init__(parent)
        self._manager = parent

    def run(self):
        data_list = self._manager.download
        for data in data_list:
            title = data.get('title')
            print(">>>>>>>>>>>>>>>>> get title of the books",title)
            category = data.get('category')
            title_ = "{}".format(title)
            categories_ = "{}".format(category)
            make_title = title_.replace(" ", "-")
            make_category = categories_.replace(" ", "-")
            make_file_name = "{}.pdf".format(make_title)
            make_link = "https://www.techpdfs.com/static/books/{}/{}/{}".format(make_category, make_title,
                                                                                make_file_name)
            offset = 0

            response = requests.get(make_link)
            filesize = requests.head(make_link)

            size = filesize.headers['content-length']

            # check_content = r.headers['Content-Type']

            download_path = download_location()
            find_word = self._manager.ui.tableWidget.findItems(title, QtCore.Qt.MatchExactly)
            time.sleep(1)
            for rows in find_word:
                print(">>>>>>>>>>>>>>>>>>> rows", rows)
                rows_ = rows.row()
                print("row text", rows_)

                progress_bar = self._manager.progress

                path_to_download = os.path.join(download_path, make_file_name)
                print(rows_)
                self.rows.emit(rows_)

                try:
                    self._manager.ui.tableWidget.setCellWidget(rows_, 3, progress_bar)

                except:
                    pass

            with open(path_to_download, 'wb') as output_file:
                for chunk in response.iter_content(chunk_size=1025):
                    if not chunk:
                        break
                    output_file.seek(offset)
                    offset = offset + len(chunk)
                    process = offset / float(size) * 100
                    progress_bar = int(process)
                    self._data.emit(progress_bar)
                    output_file.write(chunk)

        # data_list.clear()
