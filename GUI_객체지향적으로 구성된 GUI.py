import tkinter as tk
from tkinter import ttk

# 클래스 정의부
class SayHelloWin:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('버튼 위젯 예')
        self.__buildGUI()

    def __buildGUI(self):
        self.text_label = ttk.Label(self.win, text = '안녕하세요')

        self.name = tk.StringVar()
        input_entry = ttk.Entry(self.win, textvariable=self.name)

        input_btn = ttk.Button(self.win, text='입력', command=self.__input_btn_handler)
        out_btn = ttk.Button(self.win, text='종료', command=self.win.destroy)

        self.text_label.pack()
        input_entry.pack()
        input_btn.pack()
        out_btn.pack()

    def __input_btn_handler(self):
        self.text_label.configure(text='반가워요 '+ self.name.get())
        self.name.set('')

# main
hello = SayHelloWin()
hello.win.mainloop()
