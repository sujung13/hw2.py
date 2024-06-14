import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# 파일에서 단어장 불러오기
def load_words():
    if os.path.exists('words.txt'):
        with open('words.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            if data:
                return eval(data)  # 문자열을 딕셔너리로 변환하여 반환
    return {}

# 단어장 저장하기
def save_words(words_dict):
    with open('words.txt', 'w', encoding='utf-8') as file:
        file.write(str(words_dict))  # 딕셔너리를 문자열로 변환하여 저장

# 단어 추가 함수
def add_word():
    word = entry_word.get().strip()
    meaning = entry_meaning.get().strip()
    if not word or not meaning:
        messagebox.showwarning('경고', '단어와 뜻을 모두 입력하세요.')
        return
    
    if word in words:
        messagebox.showerror('오류', '이미 존재하는 단어입니다.')
    else:
        words[word] = meaning
        listbox_words.insert(tk.END, word)
        save_words(words)
        messagebox.showinfo('성공', '단어가 추가되었습니다.')
    
    entry_word.delete(0, tk.END)
    entry_meaning.delete(0, tk.END)

# 단어 검색 함수
def search_word():
    word = entry_word.get().strip()
    if not word:
        messagebox.showwarning('경고', '단어를 입력하세요.')
        return
    
    if word in words:
        meaning = words[word]
        messagebox.showinfo(word, f'뜻: {meaning}')
    else:
        messagebox.showerror('오류', '단어장에 존재하지 않는 단어입니다.')
    
    entry_word.delete(0, tk.END)

# 초기화 함수
def clear_fields():
    entry_word.delete(0, tk.END)
    entry_meaning.delete(0, tk.END)

# GUI 생성 함수
def build_gui():
    global entry_word, entry_meaning, listbox_words, words
    
    words = load_words()  # 단어장 파일에서 불러오기
    
    win = tk.Tk()
    win.title('단어장')
    
    frame = ttk.Frame(win, padding="10")
    frame.grid(row=0, column=0, padx=10, pady=10)
    
    lbl_word = ttk.Label(frame, text='단어:')
    lbl_word.grid(row=0, column=0, padx=5, pady=5)
    entry_word = ttk.Entry(frame, width=20)
    entry_word.grid(row=0, column=1, padx=5, pady=5)
    
    lbl_meaning = ttk.Label(frame, text='뜻:')
    lbl_meaning.grid(row=1, column=0, padx=5, pady=5)
    entry_meaning = ttk.Entry(frame, width=20)
    entry_meaning.grid(row=1, column=1, padx=5, pady=5)
    
    btn_add = ttk.Button(frame, text='추가', command=add_word)
    btn_add.grid(row=2, column=0, padx=5, pady=5)
    
    btn_search = ttk.Button(frame, text='검색', command=search_word)
    btn_search.grid(row=2, column=1, padx=5, pady=5)
    
    btn_clear = ttk.Button(frame, text='초기화', command=clear_fields)
    btn_clear.grid(row=2, column=2, padx=5, pady=5)
    
    btn_exit = ttk.Button(frame, text='종료', command=win.quit)
    btn_exit.grid(row=2, column=3, padx=5, pady=5)
    
    listbox_words = tk.Listbox(frame, selectmode=tk.SINGLE, width=30, height=10)
    listbox_words.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
    
    # 단어장 초기화
    for word in sorted(words.keys()):
        listbox_words.insert(tk.END, word)
    
    win.protocol("WM_DELETE_WINDOW", lambda: (save_words(words), win.quit()))
    win.mainloop()

# GUI 생성 함수 호출
build_gui()
