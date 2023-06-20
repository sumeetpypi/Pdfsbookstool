import ftplib
import hashlib
import os
import urllib

# import requests

from read_db import get_images, download_section, slider_data, search, search_slider_
from io import BytesIO


class read_ftp(object):
    def __int__(self):
        super(read_ftp, self).__init__()
        self.readFiles_ftp()

    def get_images(self, args):
        images = get_images(category=args)
        return images

    def gets_slider(self, title, category):
        slider = slider_data(title=title, category=category)
        return slider

    def search_(self, title):
        slider = search(title=title)
        return slider

    def search_slider(self, title):
        slider = search_slider_(title=title)
        return slider


    def search_data(self, title):
        data_ = list()
        titles_list = list()

        path_list = list()
        images = self.search_(title=title)
        for images in images:
            new_dict = dict()
            name = images[0]
            title = images[1]
            categories = images[3]
            time_stamp = images[4]

            new_dict['title'] = title
            new_dict['category'] = categories
            new_dict['time_stamp'] = time_stamp
            # name_change = str(name).replace(" ", "-")
            # title_change = str(title).replace(" ", "-")
            # categories = str(categories).replace(" ", "-")
            # make_path = '/project/static/books/{}/{}'.format(categories, title_change)

            title_ = "{}".format(title)
            categories_ = "{}".format(categories)
            make_title = title_.replace(" ", "-")
            make_category = categories_.replace(" ", "-")
            make_file_name = "{}.jpg".format(make_title)
            make_link = "https://www.techpdfs.com/static/books/{}/{}/{}".format(make_category, make_title,
                                                                                make_file_name)
            new_dict['path'] = make_link
            path_list.append(new_dict)

        return path_list

    def slider_func(self, title, category=None):
        data_ = list()
        titles_list = list()
        path_list = list()
        images = self.gets_slider(title=title, category=category)
        for images in images:
            new_dict = dict()
            name = images[0]
            title = images[1]
            categories = images[3]
            time_stamp = images[4]

            new_dict['title'] = title
            new_dict['category'] = categories
            new_dict['time_stamp'] = time_stamp
            # name_change = str(name).replace(" ", "-")
            # title_change = str(title).replace(" ", "-")
            # categories = str(categories).replace(" ", "-")
            # make_path = '/project/static/books/{}/{}'.format(categories, title_change)

            title_ = "{}".format(title)
            categories_ = "{}".format(categories)
            make_title = title_.replace(" ", "-")
            make_category = categories_.replace(" ", "-")
            make_file_name = "{}.jpg".format(make_title)
            make_link = "https://www.techpdfs.com/static/books/{}/{}/{}".format(make_category, make_title,
                                                                                make_file_name)
            new_dict['path'] = make_link
            path_list.append(new_dict)

        return path_list

    def search_slider__(self, title, category=None):
        data_ = list()
        titles_list = list()

        path_list = list()
        images = self.search_slider(title=title)
        for images in images:
            new_dict = dict()
            name = images[0]
            title = images[1]
            categories = images[3]
            time_stamp = images[4]

            new_dict['title'] = title
            new_dict['category'] = categories
            new_dict['time_stamp'] = time_stamp
            # name_change = str(name).replace(" ", "-")
            # title_change = str(title).replace(" ", "-")
            # categories = str(categories).replace(" ", "-")
            # make_path = '/project/static/books/{}/{}'.format(categories, title_change)

            title_ = "{}".format(title)
            categories_ = "{}".format(categories)
            make_title = title_.replace(" ", "-")
            make_category = categories_.replace(" ", "-")
            make_file_name = "{}.jpg".format(make_title)
            make_link = "https://www.techpdfs.com/static/books/{}/{}/{}".format(make_category, make_title,
                                                                                make_file_name)
            new_dict['path'] = make_link
            path_list.append(new_dict)

        return path_list

    def readFiles_ftp(self, category, offset=None):
        data_ = list()
        titles_list = list()

        path_list = list()
        images = self.get_images(args=category)
        for images in images:
            new_dict = dict()
            name = images[0]
            title = images[1]
            categories = images[3]
            time_stamp = images[4]

            new_dict['title'] = title
            new_dict['category'] = categories
            new_dict['time_stamp'] = time_stamp
            # name_change = str(name).replace(" ", "-")
            # title_change = str(title).replace(" ", "-")
            # categories = str(categories).replace(" ", "-")
            # make_path = '/project/static/books/{}/{}'.format(categories, title_change)

            title_ = "{}".format(title)
            categories_ = "{}".format(categories)
            make_title = title_.replace(" ", "-")
            make_category = categories_.replace(" ", "-")
            make_file_name = "{}.jpg".format(make_title)
            make_link = "https://www.techpdfs.com/static/books/{}/{}/{}".format(make_category, make_title,
                                                                                make_file_name)
            new_dict['path'] = make_link
            path_list.append(new_dict)

        return path_list

        # print server.dir('/project/database/')

        # for data in path_list:
        #     data_dict = dict()
        #     path = data.get('path')
        #     print path
        #     data = urllib.urlopen(path).read()
        #     print data
        #     # make_image_name = os.path.basename(path)
        #     # # title = str(make_image_name).replace("-", " ")
        #     # # print title
        #     # make_name = "{}.jpg".format(make_image_name)
        #     # server.cwd(path)
        #     # image_bytes = BytesIO()
        #     # make_image_path = 'RETR {}'.format(make_name)
        #     # server.retrbinary(make_image_path, image_bytes.write)
        #     # image_bytes.seek(0)
        #
        #     # get_title = data.get('title')
        #     # data_dict["title"] = get_title
        #     #
        #     # data_dict["image"] = image_bytes
        #     # print data_dict
        #     # data_.append(data_dict)
        #
        # return data_

    def get_details_image_obj(self, title, category, image=None):
        data_ = list()

        path_list = list()
        images = self.get_images(args=category)
        for images in images:
            new_dict = dict()
            name = images[0]
            title = images[1]
            categories = images[3]
            new_dict['title'] = title
            new_dict['category'] = categories

            # name_change = str(name).replace(" ", "-")
            # title_change = str(title).replace(" ", "-")
            # categories = str(categories).replace(" ", "-")
            # make_path = '/project/static/books/{}/{}'.format(categories, title_change)

            title_ = "{}".format(title)
            categories_ = "{}".format(categories)
            make_title = title_.replace(" ", "-")
            make_category = categories_.replace(" ", "-")
            make_file_name = "{}.jpg".format(make_title)
            make_link = "https://www.techpdfs.com/static/books/{}/{}/{}".format(make_category, make_title,
                                                                                make_file_name)
            new_dict['path'] = make_link
            path_list.append(new_dict)

        return path_list

        # path_list = list()
        # name_change = str(title).replace(" ", "-")
        # image_change = str(image).replace(" ", "-")
        # categories = str(category).replace(" ", "-")
        # print categories
        # make_path = '/project/static/books/{}/{}'.format(categories, name_change)
        # print ">>>>>", make_path
        # # print server.dir('/project/database/')
        #
        # data_dict = dict()
        # make_image_name = os.path.basename(make_path)
        # title = str(make_image_name).replace("-", " ")
        # print title
        # make_name = "{}.jpg".format(make_image_name)
        # server.cwd(make_path)
        # image_bytes = BytesIO()
        # make_image_path = 'RETR {}'.format(make_name)
        # server.retrbinary(make_image_path, image_bytes.write)
        # image_bytes.seek(0)
        # data_dict["title"] = title
        # data_dict["image"] = image_bytes
        # print data_dict
        # data_.append(data_dict)
        # return data_

    def data_1(self):
        self.data = self.readFiles_ftp(category="popular books")

        return self.data

    def data_2(self, title=None, category=None):
        self.data = self.slider_func(title=title, category=category)

        return self.data

    def search_data_(self, title):
        self.data = self.search_data(title=title)

        return self.data

    def search_slider_(self, title):
        self.data = self.search_slider__(title=title)

        return self.data

if __name__ == "__main__":
    x = read_ftp()
    x.data_1()
