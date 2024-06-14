import tkinter as tk
from tkinter import ttk

# 전역 변수로 hobbies 리스트 정의
hobbies = ['영화시청', '음악감상', '사진찍기', '운동']

# 입력 버튼을 눌렀을 때 실행되는 함수
def submit():
    global hobbies  # 전역 변수로 선언
    
    # Entry 위젯에서 이름을 가져옵니다.
    name = entry_name.get()
    
    # 라디오 버튼에서 선택된 학년을 가져옵니다.
    grade = grade_var.get()
    
    # 체크박스에서 선택된 취미들의 인덱스를 가져옵니다.
    selected_hobbies_indices = [i for i, var in enumerate(hobbies_vars) if var.get() == 1]
    
    # 선택된 취미들의 이름을 가져와서 리스트에 저장합니다.
    selected_hobbies = [hobbies[i] for i in selected_hobbies_indices]
    
    # 콘솔에 결과 출력
    print(name)
    print(grade)
    for hobby in selected_hobbies:
        print(hobby)
    print()

# GUI 생성 함수
def build_gui():
    global entry_name, grade_var, hobbies_vars
    
    # 메인 윈도우 생성
    win = tk.Tk()
    win.title('사용자 정보 입력')
    
    # 프레임 생성
    frame = ttk.Frame(win, padding="10")
    frame.grid(row=0, column=0, padx=10, pady=10)
    
    # 이름 입력 라벨과 필드
    lbl_name = ttk.Label(frame, text='이름:')
    lbl_name.grid(row=0, column=0, padx=5, pady=5)
    entry_name = ttk.Entry(frame, width=20)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    
    # 학년 선택 라벨과 라디오 버튼
    lbl_grade = ttk.Label(frame, text='학년:')
    lbl_grade.grid(row=1, column=0, padx=5, pady=5)
    grade_var = tk.IntVar()
    grades = [('1학년', 1), ('2학년', 2), ('3학년', 3), ('4학년', 4)]
    for i, (text, value) in enumerate(grades):
        ttk.Radiobutton(frame, text=text, variable=grade_var, value=value).grid(row=1, column=i+1, padx=5, pady=5)
    
    # 취미 선택 체크 박스
    lbl_hobbies = ttk.Label(frame, text='취미:')
    lbl_hobbies.grid(row=2, column=0, padx=5, pady=5)
    hobbies_vars = []
    for i, hobby in enumerate(hobbies):
        var = tk.IntVar()
        ttk.Checkbutton(frame, text=hobby, variable=var).grid(row=2, column=i+1, padx=5, pady=5)
        hobbies_vars.append(var)
    
    # 입력 버튼
    btn_submit = ttk.Button(frame, text='입력', command=submit)
    btn_submit.grid(row=3, column=0, padx=5, pady=5)
    
    # 종료 버튼
    btn_exit = ttk.Button(frame, text='종료', command=win.destroy)
    btn_exit.grid(row=3, column=1, padx=5, pady=5)
    
    # 메인 루프 시작
    win.mainloop()

# GUI 생성 함수 호출
build_gui()
