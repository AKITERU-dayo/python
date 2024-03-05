#!/usr/bin/env python3
# ↑↑↑↑↑必ず一行目に記述する：pythonプログラムを実行するという意味。
# -*- coding: utf-8 -*-
# ↑↑↑↑↑文字化け対策（文字コードをutf-8設定）

# ==========
# ブラウザでプログラムを動作させるための処理
# ==========
import cgi

# ↑↑↑↑↑プログラムをcgiで実行するためのモジュール（プログラム）を読み込む。
import io
import sys

# ↑↑↑↑↑プログラムを正しく実行するためのモジュールを読み込む。

# ==========
# ブラウザで表示する際の文字化け対策（文字コード設定）
# ==========
# ↓↓↓↓↓文字化け対策コード
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ==========
# ブラウザ表示時の文字化け対策（文字コード設定）
# ==========
# ↓↓↓↓↓ブラウザ表示時の文字化け対策（エンコーディングutf-8指定）
print("Content-Type: text/html; charset=utf-8\n")
print()


# ==========
# HTMLにpythonの処理結果を埋め込む
# ==========
html_body = """
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PY11</title>
    <link rel="stylesheet" href="../css/style.css">
    <meta http-equiv="refresh" content="1;url=http://localhost:8000/index.html">
</head>
<body>

"""


html_bodyend = """
</body>
</html>
"""

# ==========
# htmlファイルのform内の値を受け取る
# ==========
print(html_body)

form = cgi.FieldStorage()  # フォームデータを取得する
word = form.getvalue("word")
mean = form.getvalue("mean")
memo = form.getvalue("memo")


cnt = 0
import os
import sys




# ファイルアクセス
file = "date.csv"
stream = open(file, "a", encoding="SHIFT_JIS", errors="ignore")
#なにも入力されてなかったときは書き込まずにページを戻す
if word==None or mean==None:
    sys.exit()
else:
    stream.write(word + ",")
    stream.write(mean + ",")
if memo==None:
    stream.write( "なし" + "\n" )
else:
    newmemo=memo.replace('\r\n', '|')
    stream.write(newmemo.replace(' ', '~') + "\n")
stream.close()

