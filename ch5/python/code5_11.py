def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    LCSTable = [[0] * (n + 1) for i in range(0, m + 1)]

    # 첫번째 열을 0으로 채웁니다.
    for i in range(0, m + 1):
        LCSTable[i][0] = 0

    # 첫번째 행을 0으로 채웁니다.
    for j in range(0, n + 1):
        LCSTable[0][j] = 0
    
    # 배열의 나머지 셀을 채웁니다.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                LCSTable[i][j] = LCSTable[i - 1][j - 1] + 1
            else:
                LCSTable[i][j] = max(LCSTable[i - 1][j], LCSTable[i][j - 1])

    # LCSTable을 출력해봅니다.
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            print('%3d' % LCSTable[i][j], end='')
        print()

    return LCSTable[m][n]

# 다음 Test Case는 매우 오래 걸리는 Test Case입니다.
# 같은 테스트 케이스로 메모 전략 사용 버전과 다이나믹 프로그래밍 사용 버전의
# 실행 시간을 비교 체험해봅시다.
#X = 'AAACCGTGAGTTATTCGTTCTAGAA'
#Y = 'CACCCCTAAGGTACCTTTGGTTC'
X = 'ABCD'
Y = 'AEBD'
print('[%s]와 [%s]의 LCS_LENGTH의 값은 %d입니다.' % \
       (X, Y, lcs_length(X, Y))) 