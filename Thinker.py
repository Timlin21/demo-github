import tkinter as tk
import random
window = tk.Tk()
window.title('威力彩')
window.geometry('800x600')
window.configure(background='white')

header_label = tk.Label(window, text='威力彩號碼')
header_label.pack()

def lotto_number():
 num_1=int(random.uniform(1,8))
 num_2=[] 
 while len(num_2)<6:
    random.seed()
    a=int(random.choice(range(38)))
    for x in num_2:
        if x==a:
            break
    num_2.append(a)
 result = ('威力彩第ㄧ區數字:',num_2,'威力彩第二區數字:',num_1)
 result_label.configure(text=result)
  
result_label = tk.Label(window)
result_label.pack()

lotto_btn = tk.Button(window, text='馬上選數字', command=lotto_number)
lotto_btn.pack()

window.mainloop()#   d e m o - g i t h u b  
 