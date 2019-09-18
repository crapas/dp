# 이 베열의 k번째 원소에 fibonacci(k)의 결과를 저장합니다.
# 적당한 크기(우리가 구하고자 하는 최대의 피보나치 수)만큼 메모 배열을 
# 0의 값으로 초기화합니다. 즉 계산되지 않은 원소의 값은 0입니다.
memo = [0] * 100

def fibonacci(n):
  # 만약 fibonacci(n)을 이미 계산했다면 다시 계산하지 않습니다.
  if memo[n] != 0:
    return memo[n]

  # fibonacci(n)을 계산해 이 값을 memo[n]에 저장합니다.
  if (n == 1) or (n == 2):
    memo[n] = 1
  else:
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
  
  return memo[n]

n = int(input('숫자를 입력하세요 : '))
print('피보나치 수열의 %d번째 항은 %d입니다.' % (n, fibonacci(n)))