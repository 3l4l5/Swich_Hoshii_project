import requests as req
from bs4 import BeautifulSoup
import re
import datetime
import time
from requests_html import HTMLSession

pro_con = "https://books.rakuten.co.jp/rb/14647228/?l-id=search-c-item-text-02"
url = pro_con

r = req.get(url)
soup = BeautifulSoup(r.content , "html.parser")
print(soup.find_all(class_ = "status"))
print(r.content)