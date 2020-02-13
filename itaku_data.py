# itaku_master.csvから委託者番号を入力することで委託の情報を取り込んで辞書に入れる
import csv

file_path = "itaku_master.csv"


# csvを辞書に変換して計算をするクラスを作成
class itaku_master:
    def __init__(self,name):
        self.name = name

    def itaku_name(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    itaku_name = str(row['名前'])
                    return itaku_name

    def course1(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    course1 = row['コース番号1']
                    return course1

    def course2(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    course2 = row['コース番号2']
                    return course2

    def course3(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    course3 = row['コース番号3']
                    return course3

    def car(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    car = row['社用車']
                    return car

    def tanka(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    tanka = int(row['単価'])
                    return tanka

    def sonota(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    sonota = int(row['その他'])
                    return sonota

    def memo(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    memo = row['メモ']
                    return memo


    def information(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    info = row['連絡事項']
                    return info

    def information(self):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['スタッフ番号'] == self.name:
                    info = row['連絡事項']
                    return info




# # インスタンス化して結果を出力
# hiroshi = itaku_master("458")
# try:
#     print(hiroshi.itaku_name())
# except:
#     pass

#
# with open(file_path, newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         if row['スタッフ番号'] == "458":
#             itaku_name = row['名前']
#             course1 = row['コース番号1']
#             course2 = row['コース番号2']
#             course3 = row['コース番号3']
#             car = row['社用車']
#             tanka = int(row['単価'])
#             sonota = row['その他']
#             memo = row['メモ']
# print(memo)
