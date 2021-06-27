import csv

def save_to_file(notices):
    file = open("notice.csv", mode = "w",newline="", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "name", "date"])

    for notice in notices:
        writer.writerow(notice)
    return