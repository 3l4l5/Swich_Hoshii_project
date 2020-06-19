import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from bs4 import BeautifulSoup


options = Options()
# ヘッドレスモードで実行する場合
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://books.rakuten.co.jp/rb/16033028/?bkts=1&l-id=search-c-item-text-01")
    # 簡易的にJSが評価されるまで秒数で待つ
    time.sleep(5)
    # ハッシュタグのデータを含むタグを取得
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    print(soup.find_all(class_ = "status"))
except:
    traceback.print_exc()
finally:
    # エラーが起きても起きなくてもブラウザを閉じる
    driver.quit()
