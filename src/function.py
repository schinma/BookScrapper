import requests

def download(link, file_name):
    page = requests.get(link).text
    file = open(file_name, "w", encoding="utf8")
    file.write(page)
    file.close()