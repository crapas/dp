import time

def combination(n, m, memo = None):
    if memo == None:
        memo = {}
    if n == 0 or m == 0 or n == m:
        return 1
    elif (n, m) in memo:
        return memo[(n, m)]
    else:
        memo[(n, m)] = combination(n - 1, m, memo) + combination(n - 1, m - 1, memo)
        return memo[(n, m)]

n, m = input('두 수 n, m을 입력하세요. (n >= m) : ').split()
n = int(n)
m = int(m)
start_time = int(round(time.time() * 1000))
print('C(%d, %d) = %d' %(n, m, combination(n, m)))
end_time = int(round(time.time() * 1000))
print('combination 함수의 실행 시간 : %d(ms)' % (end_time - start_time))