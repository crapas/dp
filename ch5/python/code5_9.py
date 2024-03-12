def lcs_length(X, Y, m, n):
    # 종료 조건은 두 문자열 중 하나가 빈 문자열일 때이며,
    # 이때의 LCS_LENGTH는 0입니다.
    if (m == 0) or (n == 0):
        return 0

    # 문자열의 마지막 글자를 비교해 조건에 따라 재귀 호출합니다.
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs_length(X, Y, m - 1, n - 1)
    else:
        return max(lcs_length(X, Y, m, n - 1),\
                   lcs_length(X, Y, m - 1, n))  

# 다음 Test Case는 매우 오래 걸리는 Test Case입니다.
# 같은 테스트 케이스로 메모 전략 사용 버전과 다이나믹 프로그래밍 사용 버전의
# 실행 시간을 비교 체험해봅시다.
#X = 'AAACCGTGAGTTATTCGTTCTAGAA'
#Y = 'CACCCCTAAGGTACCTTTGGTTC'
X = 'ABCD'
Y = 'AEBD'
print('[%s]와 [%s]의 LCS_LENGTH의 값은 %d입니다.' % \
       (X, Y, lcs_length(X, Y, len(X), len(Y)))) 