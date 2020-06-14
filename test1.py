import requests as req
from bs4 import BeautifulSoup
import re
import datetime
import time




line_access_token = 'hlGm1bP3PRTu1wyyZgM99zbanw1QfX8oWA71vHG4hki'






line_headers = {'Authorization': 'Bearer ' + line_access_token}
line_url = "https://notify-api.line.me/api/notify"
#Linenotifyで引数のメッセージを送信する関数
def sendmessage(message):
    payload = {'message': message}
    r = req.post(line_url, headers=line_headers, params=payload,)

#URLで指定した楽天booksのサイトが示す商品の在庫があるかないか　返り値:Bool
def Can_buy(url):
    r = req.get(url)
    soup = BeautifulSoup(r.content , "html.parser")
    if re.findall("在庫あり",str(soup.find_all(class_ = "status")))==["在庫あり"]:
        return True
    if re.findall("ご注文できない商品",str(soup.find_all(class_ = "status")))==["ご注文できない商品"]:
        return False

#ほしいものリスト
pro_con = "https://books.rakuten.co.jp/rb/14647228/?l-id=search-c-item-text-02"
big = "https://books.rakuten.co.jp/rb/16033028/?bkts=1&l-id=search-c-item-text-01"
gray = "https://books.rakuten.co.jp/rb/16039045/?bkts=1&l-id=search-c-item-text-01"
yello = "https://books.rakuten.co.jp/rb/16039044/?bkts=1&l-id=search-c-item-text-23"
blue = "https://books.rakuten.co.jp/rb/16039046/?bkts=1&l-id=search-c-item-text-03"
pink = "https://books.rakuten.co.jp/rb/16247998/?bkts=1&l-id=search-c-item-text-11"

#リストにまとめる
products = [big,gray,yello,blue,pink]
#products = [pro_con,gray,yello,blue,pink]
products_name = ["Nintendo Swich 本体","Nintendo Swich lite(グレー)","Nintendo Swich lite(イエロー)","Nintendo Swich lite(グレー)","Nintendo Swich lite(ブルー)","Nintendo Swich lite(ピンク)"]

#無間ループ スクレイピングの規約に違反するかわからないけど、結構処理に時間かかって1分置きくらいにしかスクレイピングできないからまあ、許してほしい
while True:
    print(str(datetime.datetime.now())+"\n"+"ｳｺﾞｲﾃﾙﾖ!\n")

    try:
        arumono = []
        for a in products:
            if Can_buy(a):
                arumono.append(True)
            else:
                arumono.append(False)

        message = []
        dore = 0
        for b in arumono:
            if b:
                message.append(products_name[dore]+"の在庫があります URL:"+products[dore])
                dore += 1

        message_str = "\n"
        for c in message:
            message_str += c
            message_str += "\n"
        sendmessage(message_str[:-1])
    #無間ループ内中、動てるかわからないのでその時の時間と一緒に出力するようにした


    #エラーが出た場合の処理を記載
    except Exception as e:
        sendmessage("ｴﾗｰｶﾞﾃﾞﾀﾖ!ｴﾗｰﾅｲﾖｳ↓")
        sendmessage(e)
        sendmessage("1分待って再チャレンジします")
        time.sleep(60)