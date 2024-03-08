# 예제 코드를 일부 수정합니다. 책에는 0으로 되어 있습니다만
# 초기 위치와 도착 위치가 동일한 경우 경로의 수는 가만히 있는 1 입니다.
# 오류를 사과드립니다.
# 책의 예제에는 메모이제이션 예제가 아닙니다만, 메모이제이션 예제로 수정해서 보여 드립니다.

# 메모이제이션 + 하향식 코드
def num_of_paths(m, n, memo = None):
    if memo is None:
        memo = {}
    if (m == 0) or (n == 0):
        return 1
    if (m, n) in memo:
        return memo[(m, n)]
    memo[(m, n)] = num_of_paths(m - 1, n, memo) + \
                   num_of_paths(m, n - 1, memo)
    return memo[(m, n)]

M, N = input('방의 구조를 입력하세요 : ').split()
M = int(M)
N = int(N)
print('총 경로의 수는 %d개입니다.' % num_of_paths(M - 1, N - 1))
