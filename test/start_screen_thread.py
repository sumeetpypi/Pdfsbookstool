import ftplib

from Qt import QtWidgets, QtGui, QtCore
from Qt import QtCompat
from source.ui import read_db
from source.ui.files import download_location
import requests
import os
import sys
import time

link_ = []
path_list = list()
server = ftplib.FTP()
server.connect('184.168.97.210', 21)
details = "Flask@123model"
server.login('x2pgfjvp21ro', details)

download_path = download_location()
path_to_download = os.path.join(download_path, "Mastering-KVM-Virtualization.pdf")


# path_list.append(make_path)

class file_thread(QtCore.QThread):
    _data = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(file_thread, self).__init__(parent)
        self._manager = parent

    def callback(self, data):
        # if not os.path.exists(path_to_download):

        file = open("Mastering-KVM-Virtualization.pdf", 'wb')
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        data = len(data)
        # self._data.emit(data)
        file.write(data)

    def run(self):
        data = self._manager.parent_widgets
        for links in data:
            print links
            make_image_name = os.path.basename(links)

            title = str(make_image_name)
            make_name = "{}.pdf".format(title)

            # collections = open(path_to_download, 'wb')
            # print ">>>>>>>>>>>>>>>>>", collections
            # pos = collections.tell()
            # print pos
            server.cwd(links)
            # server.sendcmd('TYPE I')
            # sock = server.transfercmd(make_path, rest=pos)
            # print sock
            # buf = sock.recv(1024 * 1024)
            # print buf

            make_image_path = 'RETR {}'.format(make_name)
            server.retrbinary(make_image_path, self.callback, 1024)

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
