# c03.csvからデータを辞書に入れて計算をするクラスを作成
#csvを読み込んで出力する
import csv
file_path = "コース別商品売上管理表.csv"


# csvを辞書に変換して計算をするクラスを作成
class itaku_sum:
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
                    if num_course == self.name and num_product < 55:
                        kekka += int(row['売上数量'])
                except:
                    pass
        return kekka


# # コース番号を引数にしてそれぞれをインスタンス化して結果を出力
# jumonji = itaku_sum('2')
# print(jumonji.sum())
