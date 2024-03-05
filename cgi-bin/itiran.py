#!/usr/bin/env python3
# ↑↑↑↑↑必ず一行目に記述する：pythonプログラムを実行するという意味: 。
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
    <title>単語一覧ページ</title>
    <link rel="stylesheet" href="../css/destyle.css">
    <link rel="stylesheet" href="../css/header.css">
    <link rel="stylesheet" href="../css/itiran.css">
</head>

<body>
    <script src="../js/itiran.js" defer></script>

    <header>
        <p><a href="#"><img id="logo" src="../images/logo.png" alt="単語帳のロゴ"></a></p>
        <nav>
            <ul class="menu">
                <li><a href="../title.html">タイトル</a></li>
                <li><a href="../index.html">単語追加</a></li>
                <li><a href="itiran.py">単語一覧</a></li>
                <li><a href="../test.html">テスト</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>単語帳</h1>
        <div id="function">

            <form method="post" action="/cgi-bin/itiran.py">

                <p><input type="text" value="random" class="visuallyhidden" name="random"></P>

                <p><input id="button" type="submit" class="btn btn-radius-solid" value="ランダム"></p>
            </form>



            <form method="post" action="/cgi-bin/itiran.py">
                <p><input type="text" value="normal" class="visuallyhidden" name="normal"></p>
                <p><input id="button" type="submit" class="btn btn-radius-solid" value="昇順"></p>
            </form>

            <form method="post" action="/cgi-bin/itiran.py">
                <p><input type="text" value="reverse" class="visuallyhidden" name="reverse"></p>
                <p><input id="button" type="submit" class="btn btn-radius-solid" value="降順"></p>
            </form>



            <p><button id="button" class="hiddenbtn">非表示</button></p>


        </div>


        <form id="searchbutton" method="post" action="/cgi-bin/itiran.py">
            <p><input type="text" id="search_box" name="search"></p>
            <p><input id="button" type="submit" class="btn btn-radius-solid" value="検索"></p>
        </form>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <div class="pagetop">Top</div>
"""


html_bodyend = """
</main>
<footer>
    <p><small>&copy; 2024 hew</small></p>
</footer>

</body>

</html>
"""

print(html_body)
import csv
import os
import random
import pandas as pd


# ===============================================
# 重複なしランダム発生の関数やで
def randomnum(a, b, k):
    ns = []
    while len(ns) < k:
        n = random.randint(a, b)
        if not n in ns:
            ns.append(n)
    return ns


# ====================================================


# ===================================================-
# 検索機能
# フォームの値を受け取る
form = cgi.FieldStorage()
search = form.getvalue("search")
# 検索欄に文字入力されたとき
if search != None:
    l = []  # 検索単語を入れる配列
    with open("date.csv") as f:  # ファイルオープン
        reader = csv.reader(f)
        print("<h2>検索結果</h2>")
        print("<p id='search'>検索文字", search, "</p><dl>")
        for row in reader:
            for x in row:
                if search in x:  # 部分一致検索
                    l.append(x)
                    print("<div id='tag_title'><p>単語</p><p>意味</p><p>メモ</p></div>")
                    print("<div class='word'><dt>", row[0], "</dt>")
                    print("<dd>", row[1], "</dd>")
                    memo = row[2].replace("|", "</br>")
                    memo = memo.replace("~", "\n")
                    print("<dd>", memo, "</dd></div>")
        print("</dl>")
    # 検索単語がcsvになかった場合
    if not l:
        print("<p id=none>単語がありません</p>")
# ===========================================================


# ======================================================
# 単語一覧表示機能
print("<h2>単語一覧</h2>")
normal = form.getvalue("normal")
sort = form.getvalue("random")
resort = form.getvalue("reverse")
if normal == "normal":  # 昇順ボタンが押されたとき
    print("<section id='itiran'><dl>")
    # csvファイルを読み込む
    filepath = "date.csv"
    ret = os.path.isfile(filepath)
    if ret == False:
        print("<p>", "単語が登録されていません", "</p>")
    file = open(filepath, "r", encoding="SHIFT_JIS")
    rows = csv.reader(file)
    for row in rows:
        print("<div id='tag_title'><p>単語</p><p>意味</p><p>メモ</p></div>")
        print("<div class='word'><dt>", row[0], "</dt>")
        print("<dd>", row[1], "</dd>")
        memo = row[2].replace("|", "</br>")
        memo = memo.replace("~", "\n")
        print("<dd>", memo, "</dd></div>")
    file.close()
    print("</dl></section>")
elif normal == None and sort == None and resort == None:  # 一番最初の時
    print("<section id='itiran'><dl>")
    # csvファイルを読み込む
    filepath = "date.csv"
    ret = os.path.isfile(filepath)
    if ret == False:
        print("<p>", "単語が登録されていません", "</p>")
    file = open(filepath, "r", encoding="SHIFT_JIS")
    rows = csv.reader(file)
    for row in rows:
        print("<div id='tag_title'><p>単語</p><p>意味</p><p>メモ</p></div>")
        print("<div class='word'><dt>", row[0], "</dt>")
        print("<dd>", row[1], "</dd>")
        memo = row[2].replace("|", "</br>")
        memo = memo.replace("~", "\n")
        print("<dd id='memo'>", memo, "</dd></div>")
    file.close()
    print("</dl></section>")

# =================================================


# ====================================================================
# ランダム表示機能作る
# フォームの値を受け取る
sort = form.getvalue("random")
cnt = 0
prenum = []  # ひとつ前のランダム数を入れる配列

# csvファイルの行数(登録単語数)を調べる
if sort == "random":  # ランダムボタンが押されたとき
    with open("date.csv", "r") as file:
        lines = file.readlines()
        wordnum = len(lines)  # 登録単語数
    num = randomnum(0, wordnum - 1, wordnum)  # ランダムの重複なし数字配列numができる
    while num == prenum:  # 奇跡的にランダムで同じ順の数が出た時対策
        num = randomnum(0, wordnum - 1, wordnum)
    print("<p id='sort'>並び替えました</p><section id='itiran'><dl>")
    while cnt < wordnum:  # ランダム数配列の数字にそって読み込んでいくよ
        target_line = lines[num[cnt]]  # 指定のランダム行を読み込み
        target_line = target_line.split(",")  # 読み込んだ配列を,で区切る
        print("<div id='tag_title'><p>単語</p><p>意味</p><p>メモ</p></div>")
        print("<div class='word'><dt>", target_line[0], "</dt>")
        print("<dd>", target_line[1], "</dd>")
        memo = target_line[2].replace("|", "</br>")
        memo = memo.replace("~", "\n")
        print("<dd>", memo, "</dd></div>")
        cnt = cnt + 1
    file.close()
    print("</dl></section>")
    prenum = num  # でたランダム数を入れておく
# =========================================================================


# =============================================
# 降順ソート機能作る
resort = form.getvalue("reverse")
cnt = 0
if resort == "reverse":
    print("<section id='itiran'><dl>")
    with open("date.csv", "r") as file:
        lines = file.readlines()
        wordnum = len(lines)
    while wordnum != 0:
        target_line = lines[wordnum - 1]
        target_line = target_line.split(",")
        print("<div id='tag_title'><p>単語</p><p>意味</p><p>メモ</p></div>")
        print("<div class='word'><dt>", target_line[0], "</dt>")
        print("<dd>", target_line[1], "</dd>")
        memo = target_line[2].replace("|", "</br>")
        memo = memo.replace("~", "\n")
        print("<dd>", memo, "</dd></div>")
        wordnum = wordnum - 1
    file.close()
    print("</dl></section>")
# ====================================================
