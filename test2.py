from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://books.rakuten.co.jp/rb/16033028/?bkts=1&l-id=search-c-item-text-01')
r.html.render()
for t in r.html.find('.stasus'):
    print(t.text)