#!/usr/bin/env python3
# ↑↑↑↑↑必ず一行目に記述する：pythonプログラムを実行するという意味。
# -*- coding: utf-8 -*-
# ↑↑↑↑↑文字化け対策（文字コードをutf-8設定）

# ==========
# ブラウザ表示時の文字化け対策（文字コード設定）
# ==========
import cgi
# ↑↑↑↑↑プログラムをcgiで実行するためのモジュール（プログラム）を読み込む。
import io
import sys
# ↑↑↑↑↑プログラムを正しく実行するためのモジュールを読み込む。

# ==========
# ブラウザで表示する際の文字化け対策（文字コード設定）
# ==========
#文字化け対策コード
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ==========
# ブラウザ表示時の文字化け対策（文字コード設定）
# ==========
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
    <h1>Hello</h1>
    <p>メッセージ：</p>
    <p><img src="../image/python-logo.png"></p>
</body>
</html>
"""