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
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ==========
# ブラウザ表示時の文字化け対策（文字コード設定）
# ==========
# ↓↓↓↓↓ブラウザ表示時の文字化け対策（エンコーディングutf-8指定）
print("Content-Type: text/html; charset=utf-8\n")
print()


#==========
# HTMLにpythonの処理結果を埋め込む
#==========
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
"""


html_bodyend = """
</body>
</html>
"""

# ==========
# htmlファイルのform内の値を受け取る
# ==========
print( html_body )
form = cgi.FieldStorage() # フォームデータを取得する
name = form.getvalue( "name" )
text3 = form.getvalue("age3")
text5 = form.getvalue("age5")
text7 = form.getvalue("age7")

print("名前  = ", name , "<BR>" )
print("text3 = ", text3, "<BR>" )
print("text5 = ", text5, "<BR>" )
print("text7 = ", text7, "<BR>" )

int3 = int( text3 )
int5 = int( text5 )
int7 = int( text7 )
# 文字列結合
textsum = text3 + text5 + text7 + "<BR>"
intsum  = int3 + int5 + int7

print( textsum )
print( intsum, "<BR>" )
print( html_bodyend )

