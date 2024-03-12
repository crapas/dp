def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input('숫자를 하나 입력하세요 : '))
print('1에서 %d까지의 합 : %d' % (n, sum(n)))