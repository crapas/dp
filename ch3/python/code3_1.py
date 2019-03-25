def fibonacci(n):
  # arr[] : 피보나치 수를 저장하는 배열
  arr = [0]
  # fibonacci(1), fibonaci(2)
  arr.append(1)
  arr.append(1)

  for i in range(3, n + 1):
    # 피보나치 수열의 i번째 항을 계산하고 이를 저장
    arr.append(arr[i - 1] + arr[i - 2])
  return arr[n]

n = int(input('숫자를 입력하세요 : '))
print('피보나치 수열의 %d번째 항은 %d입니다.' % (n, fibonacci(n)))