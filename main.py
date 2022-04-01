# CSV파일 선택하기

import os
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

def file_rode():
    list_file = []                                          #파일 목록 담을 리스트 생성
    files = filedialog.askopenfilenames(initialdir="/",title = "파일을 선택 해 주세요",filetypes = (("*.csv","*csv"), ("*.xlsx","*xlsx"), ("*.xls","*xls")))
    #files 변수에 선택 파일 경로 넣기

    if files == '':
        messagebox.showwarning("경고", "파일을 추가 하세요")    #파일 선택 안했을 때 메세지 출력
    return files
__tcsv = pd.read_csv(file_rode())
print(__tcsv)