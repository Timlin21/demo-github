import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
     
app = tk.Tk() 
app.title('匯率轉換器')
app.geometry('800x600')
app.configure(background='white')


labelTop = tk.Label(app,text = "選擇想轉換的貨幣")
labelTop.pack()
labelTop.grid(column=2, row=0)


exchange_frame = tk.Frame(app)
exchange = ttk.Combobox(app,values=['美金','日幣','澳幣','歐元','人民幣'])
exchange.grid(column=0, row=1)
exchange.current(0)

labelNTD = tk.Label(app,text = "新台幣")
labelNTD.grid(column=0, row=2, sticky=tk.W)
NTDString = tk.StringVar()
entryNTD = tk.Entry(app, width=20, textvariable=NTDString)
entryNTD.grid(column=0, row=3, padx=10)

def function():
     if exchange.current()== 0:
       NTD = int(entryNTD.get())
       current = int(NTD/num_0)
       result=('匯率換算結果:',current)
       result_label.configure(text=result)       
     elif exchange.current()== 1:
       NTD = int(entryNTD.get())
       current = int(NTD/num_1)
       result=('匯率換算結果:',current)
       result_label.configure(text=result)
     elif exchange.current()== 2:
       NTD = int(entryNTD.get())
       current = int(NTD/num_2)
       result=('匯率換算結果:',current)
       result_label.configure(text=result)
     elif exchange.current()== 3:
       NTD = int(entryNTD.get())
       current = int(NTD/num_3)
       result=('匯率換算結果:',current)
       result_label.configure(text=result)
     elif exchange.current()== 4:
       NTD = int(entryNTD.get())
       current = int(NTD/num_4)
       result=('匯率換算結果:',current)
       result_label.configure(text=result)

clickButton = tk.Button(app, text = '匯率換算',command=function)
clickButton.grid(column=0, row=4, pady=10, sticky=tk.W)
clickString=tk.StringVar()
clickLabel = tk.Label(app, textvariable=clickString)
clickLabel.grid(column=0, row=6, padx=10, sticky=tk.W)

result_label = tk.Label(app) 
result_label.grid(column=0, row=7, sticky=tk.W)

url='https://rate.bot.com.tw/xrt?Lang=zh-TW'

responce=requests.get(url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'})

responce.encoding='utf-8'
raw_html=responce.text

soup=BeautifulSoup(raw_html,'html.parser')
  

num_0=float(soup.select('td:nth-child(3)')[0].text)
num_1=float(soup.select('td:nth-child(3)')[7].text)
num_2=float(soup.select('td:nth-child(3)')[3].text)
num_3=float(soup.select('td:nth-child(3)')[14].text)
num_4=float(soup.select('td:nth-child(3)')[18].text)

app.mainloop()