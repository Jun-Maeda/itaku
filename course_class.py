# course_master.csvからコース番号を入力することでコースの情報を取り込んで辞書に入れる
import csv

file_path = "course_master.csv"


# csvを辞書に変換して計算をするクラスを作成
class course_info:
    def __init__(self,name):
        self.name = name

    def course_name(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['コース番号'] == self.name:
                    course_name = str(row['コース名'])
                    return course_name

    def course_kyori(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['コース番号'] == self.name:
                    course_kyori = row['距離']
                    return course_kyori

    def course_week(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['コース番号'] == self.name:
                    course_week = row['曜日']
                    return course_week

# course_2 = course_info('2')
# print(course_2.course_week())
