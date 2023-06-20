# import os
# import requests
# from source.ui.files import download_location
#
#
#
#
# def download_func(url):
#
#     print ">>>>>>>>>>>", url
#     response = requests.get(url, stream=True)
#     filesize = requests.head(url)
#     print filesize
#     size = filesize.headers['content-length']
#     print "<<<<<<<<<<<<<<< check file size ", size
#     # check_content = r.headers['Content-Type']
#
#     download_path = download_location()
#
#     path_to_download = os.path.join(download_path, "Entity-Information-Life-Cycle-For-Big-Data.pdf")
#     offset = 0
#     with open("Entity-Information-Life-Cycle-For-Big-Data.pdf", 'wb') as output_file:
#         for chunk in response.iter_content(chunk_size=1025):
#             if not chunk:
#                 break
#             output_file.seek(offset)
#             offset = offset + len(chunk)
#             process = offset / float(size) * 100
#             progress_bar = int(process)
#             print progress_bar
#             output_file.write(chunk)
#
#
# url = "https://www.techpdfs.com/static/books/popular-books/Entity-Information-Life-Cycle-For-Big-Data/Entity-Information-Life-Cycle-For-Big-Data.pdf"
#
# download_func(url=url)
