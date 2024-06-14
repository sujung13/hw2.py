import os
from datetime import datetime
import pickle

class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

# 현재 시각을 반환하는 함수
def get_current_time():
    now = datetime.now()
    return Time(now.hour, now.minute)

# 현재 시각을 last.dat 파일에 저장하는 함수
def save_time(time):
    with open('last.dat', 'wb') as file:
        pickle.dump(time, file)

# last.dat 파일에서 시간을 읽어오는 함수
def load_time():
    if os.path.exists('last.dat'):
        with open('last.dat', 'rb') as file:
            time = pickle.load(file)
            return time
    else:
        return None

def main():
    current_time = get_current_time()
    last_time = load_time()

    if last_time is None:
        print("안녕하세요, 처음 실행되었습니다.")
    else:
        print(f"안녕하세요, 마지막으로 {last_time}에 실행되었습니다.")

    print(f"지금은 {current_time} 입니다.")

    save_time(current_time)

if __name__ == "__main__":
    main()
