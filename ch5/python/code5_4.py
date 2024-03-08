# 예제 코드를 일부 수정합니다. 출발 지점과 도착 지점이 같은 경우는 1이기 때문입니다.
# 오류를 사과 드립니다.

def num_of_paths(m, n):
    cache = [[0] * n for i in range(0, m)]
    for i in range(0, m):
        for j in range(0, n):
            if (i == 0) or (j == 0):
                cache[i][j] = 1
            else:
                cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    return cache[m - 1][n - 1]

M, N = input('방의 구조를 입력하세요 : ').split()
M = int(M)
N = int(N)
print('총 경로의 수는 %d개입니다.' % num_of_paths(M, N))
