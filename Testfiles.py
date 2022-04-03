import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog



def file_rode():
    root = tk.Tk()
    root.withdraw()                              #파일 목록 담을 리스트 생성
    file_path = filedialog.askopenfilename(parent=root,
                                           initialdir="/",
                                           title='Please select a directory')
    return file_path

__tcsv = pd.DataFrame(pd.read_csv(file_rode()))
__tcsv = __tcsv.drop(['Time'], axis=1)
__Tcsv = __tcsv.loc[400:599]

E = 799
F = 600

for i in range(0, 200):
    a = __tcsv.loc[F:E]
    __Tcsv = pd.concat([__Tcsv, a.reset_index(drop=True)],axis=1)
    E = E + i
    F = F + i

__Tcsv.to_csv(file_rode(), index = False, mode = 'w')