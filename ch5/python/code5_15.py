# value[i]는 길이 i인 철근의 가격입니다.
def max_value(value, N):
    # 종료 조건 : 남은 철근이 없을 때
    if N <= 0:
        return 0

    # 최대 이익. 파이썬에서 충분히 작은 값은 -float('inf')를 사용하면 됩니다.
    price = -float('inf')

    for i in range(1, N + 1):
        price = max(price, \
                      value[i] + max_value(value, N - i))
    
    return price

value = [0, 1, 5, 8, 9, 10, 17, 17, 20]
N = 8
print('길이 %d인 철근을 잘라서 팔 때 최대 %d의 이익을 얻을 수 있습니다.' % \
       (N, max_value(value, N)))
  