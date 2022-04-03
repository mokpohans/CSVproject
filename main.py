# CSV파일 선택하기
import os
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pandastable import Table

def file_rode():
    root.withdraw()                              #파일 목록 담을 리스트 생성
    file_path = filedialog.askopenfilename(parent=root,
                                           initialdir="/",
                                           title='Please select a directory')
    print(file_path)
    return file_path

class Csv_class():
    def creatv_csv(self):
        column : str = Column.get()
        index : str = Index.get()
        __tcsv = pd.DataFrame(pd.read_csv(file_rode()))
        __tcsv = __tcsv.drop(['Time'], axis=1)
        __Tcsv = __tcsv.loc[0:199]
        E = 399
        F = 200
        for _ in range(0, int(column)):
            a = __tcsv.loc[F:E]
            __Tcsv = pd.concat([__Tcsv, a.reset_index(drop=True)],axis=1)
            E = E + int(index)
            F = F + int(index)
        return __Tcsv
    def save_csv(csv_file):
        __Tcsv = Csv_class.creatv_csv()
        pd.to_csv(file_rode(), index = False, mode = 'w')

class Start_page(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Main_page)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()



class Main_page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        lbl1 = tk.Label(self, text="열",  width=10)
        lbl2 = tk.Label(self, text="행",  width=10)
        lbl1.grid(row=0, column=0)
        lbl2.grid(row=1, column=0)
        Column = IntVar()
        Index = IntVar()
        Column_Entry = tk.Entry(self,  width=15, textvariable=Column)
        Index_Entry = tk.Entry(self,  width=15, textvariable=Index)
        Column_Entry.grid(row=0, column=1)
        Index_Entry.grid(row=1, column=1)
        btn_save = tk.Button(self, text="저 장", width=15, command=lambda :Csv_class.save_csv())
        btn_save.grid(row=2, column=1)
        btn_view = tk.Button(self, text = "미리보기", width = 15, command=lambda: master.switch_frame(View_csv))
        btn_view.grid(row=2, column=0)

class View_csv(tk.Frame):
    def __init__(self, master):
        __Tcsv = Csv_class.creatv_csv(self)
        tk.Frame.__init__(self, master)
        view = Table(self, dataframe=__Tcsv)
        view.grid(row=0, column=0)
        btn = tk.Button(self, text="뒤로가기", command=lambda: master.switch_frame(Main_page))
        btn.grid(row=1, column=0)


if __name__ == "__main__":
    root = Start_page()
    root.mainloop()