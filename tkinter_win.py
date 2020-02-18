import tkinter
from tkinter import Listbox

# root = tkinter.Tk() # 创建窗口对象的背景色
# # 创建两个列表
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# for item in li:  # 第一个小部件插入数据
#     listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()  # 进入消息循环

import tkinter as tk
from tkinter import *
from tkinter import ttk
root = Tk()
root.wm_title("Manage")

frame = ttk.Frame(root)
frame.pack()

tree=ttk.Treeview(frame)

style = ttk.Style()
style.configure(".", font = ("Helvetica", 14))
style.configure("Treeview.Heading", font = ("Helvetica", 16) )

tree["columns"] = ("one", "two", "three", "four")
tree.column("one", width=170)
tree.column("two", width=255)
tree.column("three", width=510)
tree.column("four", width=85)

tree.heading('#0', text = "Type")
tree.heading("one", text = "Category")
tree.heading("two", text = "Display Name")
tree.heading("three", text = "GUID")
tree.heading("four", text = "Delete")

tree.insert("" , 0,    text = "Line 1", values = ("1A","1b"), tag = "orow")

id2 = tree.insert("", 1, "dir2", text = "Dir 2", tag = "erow")
tree.insert(id2, "end", "dir 2", text = "sub dir 2", values = ("2A","2B"))

tree.tag_configure('orow', background = '#EEEEEE')
tree.tag_configure('erow', background = '#CACBCB')

tree.pack()
root.mainloop()