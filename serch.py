#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser
import urllib.parse
import sys
import tkinter
import tkinter as tk
from tkinter import messagebox
import numpy as np


root = tkinter.Tk()

root.title(u"検索くん1号")
# ウインドウサイズ
root.geometry("530x50")

# チェックボックス初期値
root.attributes("-topmost", True)

browser = tk.BooleanVar()
youtube = tk.BooleanVar()
twitter = tk.BooleanVar()
qiita = tk.BooleanVar()

youtube.set(False)
browser.set(False)
twitter.set(False)
qiita.set(False)

# 検索押したときのやつ


def serchEntry(event):
    # エンコード
    serchText = urllib.parse.quote(Entry1.get())
    print(serchText)
    checklist = [browser.get(), youtube.get(), twitter.get(), qiita.get()]

    if browser.get() == True and youtube.get() == False and twitter.get() == False and qiita.get() == False:
        webbrowser.open('https://www.google.com/search?q=' + serchText)
    elif youtube.get() == True and browser.get() == False and twitter.get() == False and qiita.get() == False:
        webbrowser.open(
            'https://www.youtube.com/results?search_query=' + serchText)
    elif twitter.get() == True and browser.get() == False and youtube.get() == False and qiita.get() == False:
        webbrowser.open('https://twitter.com/search?q=' + serchText)
    elif qiita.get() == True and browser.get() == False and youtube.get() == False and twitter.get() == False:
        webbrowser.open('https://qiita.com/search?q=' + serchText)
    elif np.count_nonzero(checklist) >= 2:
        messagebox.showerror('エラー', '1つにして！！')
    else:
        webbrowser.open('https://www.google.com/search?q=' + serchText)

    Entry1.delete(0, tk.END)


# テキストボックス
Entry1 = tk.Entry(width=70)
Entry1.pack()

# ボタン
Button1 = tk.Button(text=u'検索')
Button1.bind("<Button-1>", serchEntry)
Button1.pack(fill='x', padx=20, side='right')

# チェックボックス
CheckBox1 = tk.Checkbutton(text=u"ブラウザ", variable=browser)
CheckBox1.pack(fill='x', padx=20, side='left')

CheckBox2 = tk.Checkbutton(text=u"youtube", variable=youtube)
CheckBox2.pack(fill='x', padx=20, side='left')

CheckBox3 = tk.Checkbutton(text=u"twitter", variable=twitter)
CheckBox3.pack(fill='x', padx=20, side='left')

CheckBox4 = tk.Checkbutton(text=u"qiita", variable=qiita)
CheckBox4.pack(fill='x', padx=20, side='left')


root.mainloop()
