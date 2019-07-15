#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/5/29
import tkinter
import os


class Lyric(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack(side=tkinter.TOP, fill=tkinter.Y)

        self.label = tkinter.Label(frame,
                                   text="歌词写真",
                                   bg="blue",
                                   fg="white",
                                   font=("华文琥珀", 15))
        self.label.pack(fill=tkinter.X)
        self.txt = tkinter.Text(frame,
                                width=100,
                                height=34,
                                bg="light blue",
                                fg="white")
        self.txt.pack(side=tkinter.TOP, fill=tkinter.Y)

    def vis(self):
        str = "\n\n\n\n\n\n\n\t\t\t\t正在搜索歌词……"
        self.txt.insert(tkinter.INSERT, str)

if __name__ == '__main__':
    pass