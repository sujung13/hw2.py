import os
import pickle

# 저장할 파일 경로
file_path = 'score.bin'

# 점수 저장 함수
def save_scores(scores):
    with open(file_path, 'wb') as file:
        pickle.dump(scores, file)

# 점수 로드 함수
def load_scores():
    scores = []
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            scores = pickle.load(file)
            print("[파일 읽기]")
    return scores

# 점수 입력 함수
def input_scores():
    scores = []
    while True:
        score_str = input("점수를 입력하세요 (음수를 입력하면 종료): ")
        try:
            score = int(score_str)
            if score < 0:
                break
            scores.append(score)
        except ValueError:
            print("올바른 숫자를 입력하세요.")
    return scores

# 점수 출력 함수
def print_scores(scores):
    if not scores:
        print("저장된 점수가 없습니다.")
        return

    print("[점수 출력]")
    print("개인점수:", ' '.join(map(str, scores)))
    average = sum(scores) / len(scores)
    print(f"평균: {average:.1f}")

# 메인 함수
def main():
    scores = load_scores()
    if not scores:
        print("[점수 입력]")
        scores = input_scores()
        save_scores(scores)

    print_scores(scores)

if __name__ == "__main__":
    main()
