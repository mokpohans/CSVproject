import pandas as pd
import tkinter as tk
import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.title("csv파일 생성")
def file_rode():

    root.withdraw() #파일 목록 담을 리스트 생성
    file_path = filedialog.askopenfilename(parent=root, initialdir="/", title='CSV파일 선택', filetypes=(("csv", '*.csv'),))
    return file_path

def creatv_csv():
    F = 600
    E = F + Column.get()-1
    __tcsv = pd.DataFrame(pd.read_csv(file_rode()))
    __tcsv = __tcsv.drop(['Time'], axis=1)
    __Tcsv = __tcsv.loc[400:400+Column.get()-1]
    __Tcsv.index = __Tcsv.index-400

    for i in range(1, Index.get()):
        a = __tcsv.loc[F:E]
        __Tcsv = pd.concat([__Tcsv, a.reset_index(drop=True)], axis=1)
        E = E + Column.get()
        F = F + Column.get()
    __Tcsv=__Tcsv.T
    __Tcsv=__Tcsv.reset_index(drop=True)
    name =pd.DataFrame({'201':[user_list.get() for _ in range(0, Index.get(), 1)]})
    __Tcsv = pd.concat([__Tcsv, name.reset_index(drop=True)], axis=1)
    return __Tcsv

def save_csv():
    __Csv = creatv_csv()
    save_file = filedialog.asksaveasfilename(initialdir="/", title="CSV파일 저장", defaultextension='*.csv', filetypes=(("csv", '*.csv'),))
    __Csv.to_csv(save_file, index=None, header=None)
    messagebox.showinfo("저장 성공", "정상적으로 파일을 생성했습니다")
    root.destroy()

def check_choice():
    if user_list.get() == "선 택":
        messagebox.showerror("선택오류", "사용자를 선택하지 않았습니다\n 다시 선택해주세요")
    else:
        save_csv()

values = ["H", "K", "C"]

lbl1 = tk.Label(root, text="열",  width=10)
lbl1.grid(row=0, column=0)

lbl2 = tk.Label(root, text="행",  width=10)
lbl2.grid(row=1, column=0)

Index = IntVar()
Index_Entry = tk.Entry(root,  width=15, textvariable=Index)
Index_Entry.delete(0,"end")
Index_Entry.grid(row=1, column=1)

Column = IntVar()
Column_Entry = tk.Entry(root,  width=15, textvariable=Column)
Column_Entry.delete(0,"end")
Column_Entry.grid(row=0, column=1)

user_list=tk.ttk.Combobox(root, width=15, justify='center', state="readonly", values=values)
user_list.grid(row=2, column=1)
user_list.set("선 택")

btn_save = tk.Button(root, text="저 장", width=15, command=check_choice)
btn_save.grid(row=2, column=0)

root.mainloop()
