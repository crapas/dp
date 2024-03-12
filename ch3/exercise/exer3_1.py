#  1 1  형태의 이차원 행렬 X를 생각해 봅시다. 
#  1 0

# 어떤 2X2 행렬 A에 대해서 X * A 행렬곱의 결과는 다음과 같습니다.
#  a b  X  1 1   = a + b  a
#  c d     1 0     c + d  c

#  이때 a = F(n + 1), b = c = F(n), d = F(n - 1)이라고 하면 결과는 다음과 같습니다.
#  여기서 F(n)은 피보나치 수열의 일반항 입니다.
#  F(n + 1) + F(n)   F(n + 1)  = F(n + 2) F(n + 1)
#  F(n) + F(n - 1)   F(n)        F(n + 1) F(n)

# 이 관계로부터 다음을 유추할 수 있습니다. 참고로 X의 각 원소는 F(2), F(1), F(0)와 같습니다.
# F(n + 1) F(n)         = X^n
# F(n)     F(n - 1) 

# 즉 X를 n - 1번 거듭제곱한 첫 번째 원소가 n 번째 피보나치 수열의 일반항의 값이 됩니다.

# 그러면, 행렬의 거듭 제곱을 log n 시간에 할 수 있다면 피보나치 수열의 일반항을 log n 시간에
# 구할 수 있다는 결론이 나옵니다.
# 행렬의 곱셈은 결합법칙이 성립하며, 거듭 제곱의 경우는 한 번 계산한 결과를 계속해서 
# 사용할 수 있으므로 분할 정복 방법을 사용해서 시간을 줄일 수 있습니다.

# 다음은 이를 활용해서 log n 시간에 피보나치 수열의 일반항을 구하는 함수입니다.
# 아래 함수의 matrix_multiply 함수는 O(1) 함수이며,
# matrix_power는 분할 정복 방식으로 한 번 재귀 호출할 때마다 문제의 크기가 절반씩 줄어듭니다.
# 그러므로 log n 시간 복잡도로 동작하는 알고리즘이 되겠습니다.

def fib(n):
    if n == 0:
        return 0
    F = [[1, 1],
         [1, 0]]
    return matrix_power(F, n-1)[0][0]

def matrix_power(F, n):
    if n == 0 or n == 1:
        return F
    M = [[1, 1],
         [1, 0]]
    F = matrix_power(F, n // 2)
    F = matrix_multiply(F, F)
    
    if n % 2 != 0:
        F = matrix_multiply(F, M)
    return F

def matrix_multiply(A, B):
    result = [[0, 0],
              [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result

print(fib(10))
