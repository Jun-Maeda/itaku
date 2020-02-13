# これが実行ファイル

#pdfをテンプレートから読み込んで追記して別ファイルに保存
import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from itaku_data import itaku_master
from itaku_class import itaku_sum
from course_class import course_info



# 委託コードを引数にインスタンス化するとその人の給与が印刷される
class Itaku_pdf:
    def __init__(self,itaku_num):
        self.name = itaku_num

    def pdf_print(self):
        # PDFを日本語で使えるように登録
        pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))

        packet = io.BytesIO()

        # 書き込む準備
        can = canvas.Canvas(packet, pagesize=letter)


        # 今日を取得
        today = datetime.datetime.today()
        # 当月1日の値を出す
        thismonth = datetime.datetime(today.year, today.month, 1)
        # 前月末日の値を出す
        lastmonth = thismonth + datetime.timedelta(days=-1)
        # フォーマットを指定して、年月だけ拾う
        month = lastmonth.strftime("%Y年%m月度")
        info = itaku_master(self.name)
        itaku_name = info.itaku_name()
        itaku_memo = info.memo()
        # コースごとの合計本数
        course1 = itaku_sum(info.course1()).sum()
        course2 = itaku_sum(info.course2()).sum()
        course3 = itaku_sum(info.course3()).sum()
        # コースの情報取得
        course_name1 = course_info(info.course1())
        course_name2 = course_info(info.course2())
        course_name3 = course_info(info.course3())

        # 委託者の情報反映
        car = info.car()
        tanka = info.tanka()
        sonota = int(info.sonota())
        information = info.information()

        if car == "あり":
            car_cost = carcost
        else:
            car_cost = 0


        # 書き込む内容を記載
        can.setFont("HeiseiMin-W3", 11)
        # 委託番号
        can.drawString(240, 740, self.name)
        # 名前
        can.drawString(273, 740, itaku_name)
        # 対象月
        can.drawString(360, 740, month)
        #その他金額
        can.drawString(475, 235, str(sonota) + "円")
        #その他内容
        can.setFont("HeiseiMin-W3", 10)
        itaku_memos = itaku_memo.split('¥n')
        # メモの改行位置変更のためのy変数
        y = 253
        for i in itaku_memos:
            can.drawString(80, y, i)
            y = y - 10

        #連絡事項内容
        infos = information.split('¥n')
        # 連絡事項内容のy変数
        y2 = 155
        for i in infos:
            can.drawString(80, y2, i)
            y2 = y2 - 10



        can.setFont("HeiseiMin-W3", 14)
        # コース1名
        can.drawString(90, 670, course_name1.course_name())

        can.setFont("HeiseiMin-W3", 11)
        # 単価表示
        can.drawString(120, 630, str(tanka) + "円／本")
        # コース１の合計本数
        can.drawString(220, 630, str(course1) + "本")
        # コース１の距離
        can.drawString(283, 630, course_name1.course_kyori() + "km")
        # コース１の配達料
        haitatsu_cost = tanka * course1
        can.drawString(325, 670, str(haitatsu_cost) + "円")

        # 車両費単価
        can.drawString(400, 630, str(car_cost)+"円／km")

        car_total = car_cost * int(course_name1.course_kyori())
        #コース1の配達回数今だけ指定
        course_time1 = course_name1.course_week()
        time1 = weeks[course_time1]
        #コース1の車両費トータル
        can.drawString(400, 670, str(car_total * time1) + "円")


        # コース１の配達委託料
        course1_total = haitatsu_cost + (car_total * time1)
        can.drawString(470, 670, str(course1_total) + "円")

        #コース１の配達回数を出力
        can.drawString(350, 630, str(time1) + "回")




        can.setFont("HeiseiMin-W3", 14)
        # コース2名
        can.drawString(90, 575, course_name2.course_name())

        can.setFont("HeiseiMin-W3", 11)
        # 単価表示
        can.drawString(120, 538, str(tanka) + "円／本")
        # コース2の合計本数
        can.drawString(220, 538, str(course2) + "本")
        # コース2の距離
        can.drawString(283, 538, course_name2.course_kyori() + "km")
        # コース2の配達料
        haitatsu_cost2 = tanka * course2
        can.drawString(325, 575, str(haitatsu_cost2) + "円")

        # 車両費単価
        can.drawString(400, 538, str(car_cost)+"円／km")

        car_total2 = car_cost * int(course_name2.course_kyori())
        #コース2の配達回数今だけ指定
        course_time2 = course_name2.course_week()
        time2 = weeks[course_time2]
        #コース２の車両費トータル
        can.drawString(400, 575, str(car_total2 * time2) + "円")


        # コース2の配達委託料
        course2_total = haitatsu_cost + (car_total2 * time2)
        can.drawString(470, 575, str(course2_total) + "円")

        #コース2の配達回数を出力
        can.drawString(350, 538, str(time2) + "回")




        can.setFont("HeiseiMin-W3", 14)
        # コース3名
        can.drawString(90, 484, course_name3.course_name())

        can.setFont("HeiseiMin-W3", 11)
        # 単価表示
        can.drawString(120, 444, str(tanka) + "円／本")
        # コース3の合計本数
        can.drawString(220, 444, str(course3) + "本")
        # コース3の距離
        can.drawString(283, 444, course_name3.course_kyori() + "km")
        # コース3の配達料
        haitatsu_cost3 = tanka * course3
        can.drawString(325, 484, str(haitatsu_cost3) + "円")

        # 車両費単価
        can.drawString(400, 444, str(car_cost)+"円／km")

        car_total3 = car_cost * int(course_name3.course_kyori())
        #コース3の配達回数今だけ指定
        course_time3 = course_name3.course_week()
        time3 = weeks[course_time3]
        #コース3の車両費トータル
        can.drawString(400, 484, str(car_total3 * time3) + "円")


        # コース2の配達委託料
        course3_total = haitatsu_cost + (car_total3 * time3)
        can.drawString(470, 484, str(course3_total) + "円")

        #コース3の配達回数を出力
        can.drawString(350, 444, str(time3) + "回")


        #全ての合計を出力
        kyuyo_total = course1_total + course2_total + course3_total + sonota
        can.drawString(460, 740, str(kyuyo_total) + "円")

        can.save()

        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # テンプレートのPDFを読み込む
        existing_pdf = PdfFileReader(open("templete.pdf", "rb"))

        output = PdfFileWriter()
        page = existing_pdf.getPage(0)
        page2 = new_pdf.getPage(0)
        page.mergePage(page2)
        output.addPage(page)
        pdf_name = self.name + "kyuyo.pdf"
        outputStream = open(pdf_name, "wb")
        output.write(outputStream)
        outputStream.close()


    # 合計値の値のみを出力する
    def total_data(self):

        info = itaku_master(self.name)
        itaku_name = info.itaku_name()
        # コースごとの合計本数
        course1 = itaku_sum(info.course1()).sum()
        course2 = itaku_sum(info.course2()).sum()
        course3 = itaku_sum(info.course3()).sum()
        # コースの情報取得
        course_name1 = course_info(info.course1())
        course_name2 = course_info(info.course2())
        course_name3 = course_info(info.course3())

        # 委託者の情報反映
        car = info.car()
        tanka = info.tanka()
        sonota = int(info.sonota())


        # コース１の配達料
        haitatsu_cost = tanka * course1

        car_total = car_cost * int(course_name1.course_kyori())
        #コース1の配達回数今だけ指定
        course_time1 = course_name1.course_week()
        time1 = weeks[course_time1]


        # コース１の配達委託料
        course1_total = haitatsu_cost + (car_total * time1)



        # コース2の配達料
        haitatsu_cost2 = tanka * course2



        car_total2 = car_cost * int(course_name2.course_kyori())
        #コース2の配達回数今だけ指定
        course_time2 = course_name2.course_week()
        time2 = weeks[course_time2]

        # コース2の配達委託料
        course2_total = haitatsu_cost + (car_total2 * time2)

        # コース3の配達料
        haitatsu_cost3 = tanka * course3


        car_total3 = car_cost * int(course_name3.course_kyori())
        #コース3の配達回数今だけ指定
        course_time3 = course_name3.course_week()
        time3 = weeks[course_time3]


        # コース3の配達委託料
        course3_total = haitatsu_cost + (car_total3 * time3)


        #全ての合計を出力
        kyuyo_total = course1_total + course2_total + course3_total + sonota
        sums = {itaku_name:kyuyo_total}
        # total_sum{itaku_name} = kyuyo_total
        total_sum.update(sums)



total_sum = {}

carcost = int(input("車両費を半角数字で入力"))
getsumoku = int(input('月木の回数を入力'))
kakin = int(input('火金の回数を入力'))
getsu = int(input('月の回数を入力'))
ka = int(input('火の回数を入力'))
moku = int(input('木の回数を入力'))
kin = int(input('金の回数を入力'))
weeks = {"月木":getsumoku,"火金":kakin,"月":getsu,"火":ka,"木":moku,"金":kin}

# 委託番号を入力して委託の給与明細を出力
hiroshi = Itaku_pdf("458")

hiroshi.pdf_print()


# # 委託の人すべての合計値を出力
# hiroshi.total_data()
#
# for k, v in total_sum.items():
#     print(k + "さん")
#     print(str(v) + "円")
