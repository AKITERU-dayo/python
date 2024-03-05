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
#文字化け対策コード
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ==========
# ブラウザ表示時の文字化け対策（文字コード設定）
# ==========
print("Content-Type: text/html; charset=utf-8\n")
print()


#==========
# pythonの基本処理
#==========
