# csvからデータをとりこんで、コース番号を入力するとそのコースの特定の商品の合計値の１０％を計算。
#csvを読み込んで出力する
import csv
file_path = "コース別商品売上管理表.csv"


class itaku_bonus:
    def __init__(self,course):
        self.name = course

    def course_num(self):
        return self.name

    def sum(self):
        with open(file_path, newline='', encoding='cp932') as csvfile:
            kekka = 0
            # csvの最初の三行を飛ばすための処理
            next(csvfile)
            next(csvfile)
            next(csvfile)
            reader = csv.DictReader(csvfile)
            for row in reader:
                course_name = row['コース名']
                num_course = row['コース']
                # nonetypeエラーが出るのでエラーを無視するコード
                try:
                    num_product = int(row['商品コード'])
                    # 商品コードが５５以下の数量をすべて足す
                    if num_course == self.name and num_product > 55:
                        kekka += int(row['総売上金額'])
                except:
                    pass
        return kekka / 10
course_num = input('計算したいコース番号を半角数字で入力')
course_120 = itaku_bonus(course_num)
print(course_120.sum())
