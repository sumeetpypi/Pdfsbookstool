from source import read_file
import os
import sqlite3


def get_images(category, offset=None):
    data_dict = list()
    data = read_file()
    conn = sqlite3.connect(data)
    cur = conn.cursor()
    database_exits = True

    if not os.path.exists(data):
        database_exits = False

    try:
        if database_exits:
            select_query = "select image, title, download_url, categories, time_stamp from books_db where categories = '{}' limit 21 ".format(
                category)
            get_data = cur.execute(select_query)
            fetch_data = get_data.fetchall()
            for x in fetch_data:
                data_dict.append(x)

        return data_dict

    except Exception as e:
        pass


def download_section(title):
    data_dict = list()
    data = read_file()
    conn = sqlite3.connect(data)
    cur = conn.cursor()
    database_exits = True

    if not os.path.exists(data):
        database_exits = False

    # year_ = "{}-year".format(title)
    try:
        if database_exits:
            select_query = "select categories, title, size, pages, description, download_url  from books_db where title = '{}'".format(
                title)
            get_data = cur.execute(select_query)
            fetch_data = get_data.fetchall()
            for x in fetch_data:

                data_dict.append(x)

        return data_dict

    except Exception as e:
        pass


def get_file_details(title):
    data_dict = list()
    data = read_file()
    conn = sqlite3.connect(data)
    cur = conn.cursor()
    database_exits = True

    if not os.path.exists(data):
        database_exits = False

    title_ = "{}".format(title).replace("...", "")
    try:
        if database_exits:
            select_query = "select image, title, size, pages, description, download_url, categories  from books_db where title " \
                           "LIKE '{}%' limit 1".format(title_)
            get_data = cur.execute(select_query)
            fetch_data = get_data.fetchall()
            for x in fetch_data:
                data_dict.append(x)

        return data_dict

    except Exception as e:
        pass


def slider_data(title, category=None, offset=None):
    data_dict = list()
    data = read_file()
    conn = sqlite3.connect(data)
    cur = conn.cursor()
    database_exits = True

    if not os.path.exists(data):
        database_exits = False

    try:
        if database_exits:

            select_query = "select image, title, download_url, categories, time_stamp from books_db where title = '{}' and categories = '{}' limit 5 ".format(
                title, category)
            get_data = cur.execute(select_query)
            fetch_data = get_data.fetchall()

            for x in fetch_data:
                time_stamp = x[4]

                select_query = "select image, title, download_url, categories, time_stamp from books_db where time_stamp > '{}'  and categories = '{}' limit 5 ".format(
                    time_stamp, category)
                get_data = cur.execute(select_query)
                fetch_data = get_data.fetchall()

                return fetch_data

    except Exception as e:
        pass


def search(title):
    data_dict = list()
    data = read_file()
    conn = sqlite3.connect(data)
    cur = conn.cursor()
    database_exits = True

    if not os.path.exists(data):
        database_exits = False

    get_string = "{}".format(title).partition(" ")[0]


    try:
        if database_exits:
            select_query = "select image, title, download_url, categories, time_stamp from books_db where title LIKE '{}%' limit 5 ".format(
                get_string)
            get_data = cur.execute(select_query)
            fetch_data = get_data.fetchall()
            return fetch_data

    except Exception as e:
        pass


def search_slider_(title,  offset=None):
    data_dict = list()
    data = read_file()
    conn = sqlite3.connect(data)
    cur = conn.cursor()
    database_exits = True

    if not os.path.exists(data):
        database_exits = False

    try:
        if database_exits:

            select_query = "select image, title, download_url, categories, time_stamp from books_db where title = '{}' limit 5 ".format(
                title)
            get_data = cur.execute(select_query)
            fetch_data = get_data.fetchall()

            for x in fetch_data:
                time_stamp = x[4]

                select_query = "select image, title, download_url, categories, time_stamp from books_db where time_stamp > '{}'  limit 5 ".format(
                    time_stamp)
                get_data = cur.execute(select_query)
                fetch_data = get_data.fetchall()

                return fetch_data

    except Exception as e:
        pass

