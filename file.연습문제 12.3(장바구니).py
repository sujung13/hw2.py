import os

# 장바구니 파일 경로
filepath = 'shoppingbag.txt'

# 장바구니 로드 함수
def load_shopping_bag():
    shopping_bag = []
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                item = line.strip()
                if item:  # 빈 문자열이 아니면 장바구니에 추가
                    shopping_bag.append(item)
        print("[파일 읽기]")
    return shopping_bag

# 장바구니 저장 함수
def save_shopping_bag(shopping_bag):
    with open(filepath, 'w', encoding='utf-8') as file:
        for item in shopping_bag:
            file.write(f"{item}\n")

# 장바구니 프로그램 시작
def main():
    shopping_bag = load_shopping_bag()
    print(f">>> 장바구니 보기: {shopping_bag}")

    while True:
        print("\n[구입]")
        item = input("상품명? ")
        if item == "":
            break
        shopping_bag.append(item)
        print(f"장바구니에 {item}가(이) 담겼습니다.")
    
    print(f">>> 장바구니 보기: {shopping_bag}")
    save_shopping_bag(shopping_bag)

if __name__ == "__main__":
    main()
