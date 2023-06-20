from Qt import QtWidgets, QtGui, QtCore
from Qt import QtCompat
from source.ui import read_db
from source.ui.files import download_location
import requests
import os
import sys
import time

link_ = []


class file_thread(QtCore.QThread):
    start_ = QtCore.Signal(int)
    finished = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(file_thread, self).__init__(parent)
        self._manager = parent

    def run(self):

        for i in range(100):
            self.start_.emit(i)
            time.sleep(1)
        self.finished.emit()

    #     offset = 0
    #     print ">>>>>>>>>>>", url
    #     r = requests.get(url, stream=True)
    #     filesize = r.headers['Content-Length']
    #     check_content = r.headers['Content-Type']
    #     download_path = download_location()
    #     path_to_download = os.path.join(download_path, name)
    #     with open(path_to_download, 'wb') as output_file:
    #         for chunk in r.iter_content(chunk_size=1025):
    #             if not chunk:
    #                 break
    #             output_file.seek(offset)
    #             offset = offset + len(chunk)
    #             process = offset / float(filesize) * 100
    #             progress_bar = int(process)
    #             print progress_bar
    #             self._data.emit(progress_bar)
    #             output_file.write(chunk)
    #

    # title = self._manager.ui.tableWidget.item(0, 0).text()
    # get_link = read_db.download_section(title=title)
    # print ">>>>>>>>>>>>>>", get_link
    # for links in get_link:
    #     link = links[4]
    #     print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  check", link
    #     collections = links[1]
    #     print collections
    #     make_file_name = "{}.pdf".format(collections)
    #     makefile = make_file_name.replace(" ", "-")
    #     self.download_func(links[5], makefile)

    # download_link = str(links[5])
    # if not download_link.startswith("https://www.pdfdrive.com"):
    #     make_url = "https://www.{}".format(download_link)
    #     self.download_func(make_url, makefile)
    # else:
    #     self.download_func(download_link, makefile)
