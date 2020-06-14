# Name　Swich_Hoshii_Project

Swichが欲しいので楽天ブックのスイッチのページをスクレピングして在庫があるのかないのかを見てもらうものをつくりました　

# Requirement

必要なライブラリ

* beautifulsoup

# Installation

上記ライブラリは以下のようにしてインストールできます

```bash
pip install bs4
```

# Usage

Line notify APIを用いていますので、以下ページからアクセストークンを各自発行し、ソースコードのはじめの


```bash
line_access_token = '自分のアクセストークン'
```
に各自張り付けてから実行してください。

主な使い方は以下のURLを参考にしました
https://qiita.com/yoshi_san/items/7879b3117d298a143101


# Note

勝手に作っただけなので、使用は自己責任で

# Author

作成情報を列挙する

* 作成者 Ryusei Ohkura
* E-mail csru20003@g.nihon-u.ac.jp

# UPDATE情報
* 2020/06/14　例外処理が発生した場合、エラーメッセージをLine に送り1分後に再チャレンジするようにしました。
