# CSV파일 선택하기
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def file_rode():
    root.withdraw()                              #파일 목록 담을 리스트 생성
    file_path = filedialog.askopenfilename(parent=root,
                                           initialdir="/",
                                           title='Please select a directory')
    print(file_path)
    return file_path


def creatv_csv():
    __tcsv = pd.DataFrame(pd.read_csv('C:/Users/zeunj/Downloads/PrefixA1.rawwave.csv'))
    __tcsv = __tcsv.drop(['Time'], axis=1)
    _Tcsv = __tcsv.loc[0:199]
    E = 399
    F = 200
    for _ in range(0, 5):
        a = __tcsv.loc[F:E]
        _Tcsv = pd.concat([_Tcsv, a.reset_index(drop=True)],axis=1)
        E = E + 200
        F = F + 200
    print(_Tcsv)

root = tk.Tk()

lbl1 = tk.Label(root, text="행",  width=10)
lbl2 = tk.Label(root, text="열",  width=10)
lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
txt1 = tk.Entry(root)
txt2 = tk.Entry(root)
txt1.grid(row=0, column=1)
txt2.grid(row=1, column=1)
btn = tk.Button(root, text="OK", width=15)
btn.grid(row=2, column=1)

root.mainloop()
