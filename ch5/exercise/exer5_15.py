def LPS_length(string):
    n = len(string)
    # 빈 문자열일 때
    if (string is None) or (n == 0):
        return 0

    # LPSL_table[i][j]는 str[i]에서 str[j]까지의 길이 j - i + 1 문자열의
    # 최장 회문 부분 수열의 길이를 저장합니다.
    LPSL_table = [[0] * n for i in range(0, n)]
    # LPS는 str[i]에서 str[j]까지 길이 j - i + 1 문자열에 포함된 
    # 최장 회문 부분 수열 중 하나를 저장합니다. 같은 길이의 회문이 있는 경우
    # 모두 다 찾을 수 있도록 각자 수정해 보는 것도 좋은 연습이 될 것 같습니다.
    LPS = [['' for _ in range(n)] for _ in range(n)]

    # 길이가 1인 문자열은 그 자체로 회문이므로 LPSL의 값은 1입니다.
    # 길이가 1인 문자열의 회문도 저장합니다.
    for i in range(0, n):
        LPSL_table[i][i] = 1
        LPS[i][i] = string[i]
    
    # 길이가 2인 문자열의 LPSL부터 차례로 채워나갑니다.
    for k in range(2, n + 1):
        for i in range(0, n - k + 1):
            j = i + k - 1
            # 길이가 2이며 두 글자가 모두 같으면 LPSL은 2입니다.
            # 길이가 2인 회문도 저장합니다.
            if (string[i] == string[j]) and (k == 2):
                LPSL_table[i][j] = 2
                LPS[i][j] = string[i] + string[j]
            # 앞뒤 글자가 같으면 두 글자를 제외한 문자열의 
            # LPS(LPSL_table[i + 1][j - 1])에 두 글자를 추가합니다.
            # 이 경우의 최장 회문은 LPS[i + 1][j - 1]에 같은 두 글자를 앞 뒤에
            # 추가한 경우입니다.
            elif string[i] == string[j]:
                LPSL_table[i][j] = LPSL_table[i + 1][j - 1] + 2
                LPS[i][j] = string[i] + LPS[i + 1][j - 1] + string[j]
            # 앞뒤 글자가 다른 경우 LPS가 바뀌지 않으므로
            # 앞 글자를 제외한 문자열의 LPSL과
            # 뒤 글자를 제외한 문자열의 LPSL 중 큰 값을 가져오면 됩니다.
            # 최장 회문 또한 큰 쪽의 회문을 그대로 유지합니다.
            else:
                a = LPSL_table[i][j - 1]
                b = LPSL_table[i + 1][j]
                if a > b:
                    LPSL_table[i][j] = a
                    LPS[i][j] = LPS[i][j - 1]
                else:
                    LPSL_table[i][j] = b
                    LPS[i][j] = LPS[i + 1][j]
    
    # 완성된 LPSL_table을 출력해봅니다.
    for i in range(0, n):
        for j in range(0, n):
            if i > j:
                print('  -', end = '')
            else:
                print('%3d' % LPSL_table[i][j], end = '')
        print()
    
    return LPSL_table[0][n - 1], LPS[0][n - 1]

string = 'BBABCBCAB'
start = 0
end = len(string) - 1
LPSL, LPS = LPS_length(string)
print('%s의 최장 회문 부분 수열의 길이는 %d이며, 최장 회문 부분 수열은 %s입니다.' % \
    (string, LPSL, LPS))