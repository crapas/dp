def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('숫자를 입력하세요 : '))
print('피보나치 수열의 %d번째 항은 %d입니다.' % (n, fibonacci(n)))