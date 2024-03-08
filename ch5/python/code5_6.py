def is_interleaving(A, B, C):
    # A, B, C 세 문자열의 길이를 구합니다.
    M = len(A)
    N = len(B)
    length_c = len(C)

    # A와 B 문자열의 길이의 합이 C 문자열의 길이와 다를 때
    if length_c != M + N:
        return False

    # 인터리빙 여부를 저장하는 2차원 배열
    il_matrix = [[True] * (N + 1) for i in range(0, M + 1)]

    # 첫번째 열을 채웁니다.
    for i in range(1, M + 1):
        if A[i - 1] != C[i - 1]:
            il_matrix[i][0] = False
        else:
            il_matrix[i][0] = il_matrix[i - 1][0]

    # 첫번째 행을 채웁니다.
    for j in range(1, N + 1):
        if B[j - 1] != C[j - 1]:
            il_matrix[0][j] = False
        else:
            il_matrix[0][j] = il_matrix[0][j - 1]
      
    # 나머지 셀을 채웁니다.
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            currant_a = A[i - 1]
            current_b = B[j - 1]
            current_c = C[i + j - 1]
            # C의 글자가 A의 글자와 같고 B의 글자와 다를 때
            if (currant_a == current_c) and (current_b != current_c):
                il_matrix[i][j] = il_matrix[i - 1][j]
            # C의 글자가 B의 글자와 같고 A의 글자와 다를 때
            elif (currant_a != current_c) and (current_b == current_c):
                il_matrix[i][j] = il_matrix[i][j - 1]
            # A, B, C 글자 모두가 같을 때
            elif (currant_a == current_c) and (current_b == current_c):
                il_matrix[i][j] = il_matrix[i - 1][j] or il_matrix[i][j - 1]
            else:
                il_matrix[i][j] = False

    # 완성된 행렬을 출력합니다.
    for i in range(0, M + 1):
        for j in range(0, N + 1):
            print('%s' % 'T ' if il_matrix[i][j] else 'F ', end = '')
        print()

    return il_matrix[M][N]  

a = 'bcc'
b = 'bbca'
c = 'bbcbcac'
check = is_interleaving(a, b, c)
print('%s는 %s와 %s의 인터리빙' % (c, a, b), end = '')
if check:
    print('입니다.')
else:
    print('이 아닙니다.')