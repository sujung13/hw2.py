# 사용자로부터 입력된 금액을 동전으로 교환하고자 할 때, 각 동전별 교환 개수를 출력
# 동전의 총 개수가 최소가 될 수 있도록,
# 500원 -> 100원 -> 50원 -> 10원의 우선순위로 교환

def exchange(n):
    m500 = n // 500
    n %= 500
    m100 = n // 100
    n %= 100
    m50 = n // 50
    n %= 50
    m10 = n // 10
    print('500원 동전의 개수:', m500)
    print('100원 동전의 개수:', m100)
    print('50원 동전의 개수:', m50)
    print('10원 동전의 개수:', m10)

def get_integer(prompt):
    return int(input(prompt))
    
money = get_integer('동전으로 교환하고자 하는 금액은?: ')
exchange(money)
