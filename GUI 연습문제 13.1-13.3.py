import tkinter as tk
from tkinter import ttk

# 섭씨를 화씨로 변환하는 함수
def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 1.8) + 32
        entry_fahrenheit.delete(0, tk.END)  # 기존 값 삭제
        entry_fahrenheit.insert(0, fahrenheit)  # 새로운 값 삽입
    except ValueError:
        pass

# 화씨를 섭씨로 변환하는 함수
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) / 1.8
        entry_celsius.delete(0, tk.END)  # 기존 값 삭제
        entry_celsius.insert(0, celsius)  # 새로운 값 삽입
    except ValueError:
        pass

# 필드 초기화 함수
def clear_fields():
    entry_celsius.delete(0, tk.END)
    entry_fahrenheit.delete(0, tk.END)

# GUI 생성 함수
def build_gui():
    global entry_celsius, entry_fahrenheit
    
    # 메인 윈도우
    win = tk.Tk()
    win.title('온도 변환기')
    
    # 프레임 생성
    frame = ttk.Frame(win, padding="10")
    frame.grid(row=0, column=0, padx=10, pady=10)
    
    # 섭씨 입력 필드와 라벨
    lbl_celsius = ttk.Label(frame, text='섭씨 온도:')
    lbl_celsius.grid(row=0, column=0, padx=5, pady=5)
    entry_celsius = ttk.Entry(frame, width=10)
    entry_celsius.grid(row=0, column=1, padx=5, pady=5)
    
    # 화씨 입력 필드와 라벨
    lbl_fahrenheit = ttk.Label(frame, text='화씨 온도:')
    lbl_fahrenheit.grid(row=1, column=0, padx=5, pady=5)
    entry_fahrenheit = ttk.Entry(frame, width=10)
    entry_fahrenheit.grid(row=1, column=1, padx=5, pady=5)
    
    # 섭씨 -> 화씨 변환 버튼
    btn_c_to_f = ttk.Button(frame, text='섭씨 -> 화씨', command=celsius_to_fahrenheit)
    btn_c_to_f.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    # 화씨 -> 섭씨 변환 버튼
    btn_f_to_c = ttk.Button(frame, text='화씨 -> 섭씨', command=fahrenheit_to_celsius)
    btn_f_to_c.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    # 초기화 버튼
    btn_clear = ttk.Button(frame, text='초기화', command=clear_fields)
    btn_clear.grid(row=4, column=0, padx=5, pady=5)
    
    # 종료 버튼
    btn_exit = ttk.Button(frame, text='종료', command=win.destroy)
    btn_exit.grid(row=4, column=1, padx=5, pady=5)
    
    # 메인 루프 시작
    win.mainloop()

# GUI 생성 함수 호출
build_gui()
