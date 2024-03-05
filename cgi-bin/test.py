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
</head>
<body>
<header>
        <a href="#"><img id="logo" src="../images/image (1).png" alt="単語帳のロゴ"></a>
        <nav>
            <ul>
                <li><a href="title.html">タイトル</a></li>
                <li><a href="#">使い方</a></li>
                <li><a href="/cgi-bin/itiran.py">単語一覧</a></li>
                <li><a href="test.html">テスト</a></li>
            </ul>
        </nav>
    </header>

"""


html_bodyend = """
</body>
</html>
"""

# ==========
# htmlファイルのform内の値を受け取る
# ==========
import csv
import random






#===============================================
# 重複なしランダム発生の関数やで
def randomnum(a, b, k):
    ns = []
    while len(ns) < k:
        n = random.randint(a, b)
        if not n in ns:
            ns.append(n)
    return ns
#====================================================




print(html_body)
form = cgi.FieldStorage()  # フォームデータを取得する
quenum = form.getvalue("quenum")
cnt=0
box=[]
#csvファイルを読み込み2次元配列に格納
with open('date.csv', newline='') as f:
    reader = csv.reader(f)
    row_list = [row for row in reader]
#登録単語数を調べる
with open('date.csv', 'r') as file:
    lines = file.readlines()
    wordnum=len(lines) 
cnt=0
qno=1   #問題番号
quenum = int( quenum )
#wordnum = int( wordnum)
if wordnum < quenum:
    quenum=wordnum

num=randomnum(0,wordnum,quenum)   #正解の問題の配列
print(num)
print(wordnum)
print("問題",qno,row_list[num[cnt]][0])     #問題の単語を出力
correctans=row_list[num[cnt]][1]            #正解の意味
incorrectnum=randomnum(0,wordnum-1,15)

ans1=row_list[incorrectnum[0]][1]
ans2=row_list[incorrectnum[1]][1]
ans3=row_list[incorrectnum[2]][1]  
print(ans1,ans2,ans3,correctans)  

