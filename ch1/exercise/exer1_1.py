# 재귀를 사용하는 경우
def factorial_recursive(n):    
    if n == 1 or n == 0:
        return 1
    else:
        return factorial_recursive(n - 1) * n

# 재귀를 사용하지 않는 경우
def factorial_loop(n):
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result *= i + 1
    return result


# 재귀 종료 조건을 재귀 함수에서 다 확인하기 힘들 때도 있습니다.
# 다음의 경우는 양의 정수가 아닌 경우 함수 자체를 호출하지 
# 않도록 관리하는 형태로 구현한 예제입니다.
try:
    n = int(input('음수가 아닌 정수를 하나 입력하세요 : '))
    if n < 0:
        print("입력한 수는 음의 정수입니다.")
    else:
        factorial = factorial_recursive(n)
        print('(재귀 호출 사용) %d! = %d' % (n, factorial))
        factorial = factorial_loop(n)
        print('(재귀 호출 미사용) %d! = %d' % (n, factorial))

except ValueError:  # 정수로 변형할 수 없는 입력을 한 경우
    print("정수를 입력해주세요.")