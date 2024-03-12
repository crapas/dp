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

    # LCS를 출력합니다.
    LCSLength = LCSTable[m][n]
    print('LCS_LENGTH : %d' % LCSLength)
    LCS = ''

    i = m
    j = n

    while (i > 0) and (j > 0):
        if X[i - 1] == Y[j - 1]:
            LCS = X[i - 1] + LCS
            i -= 1
            j -= 1
        elif LCSTable[i - 1][j] > LCSTable[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    print('LCS는 %s입니다.' % LCS)

    return LCSTable[m][n]

X = 'AAACCGTGAGTTATTCGTTCTAGAA'
Y = 'CACCCCTAAGGTACCTTTGGTTC'
print('[%s]와 [%s]의 LCS_LENGTH의 값은 %d입니다.' % \
       (X, Y, lcs_length(X, Y))) 