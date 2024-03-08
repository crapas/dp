def edit_distance(str1, str2, m, n):
    edit_distances = [[0] * (n + 1) for i in range(0, m + 1)]

    for j in range(0, n + 1):   # 제일 위 행
        edit_distances[0][j] = j
    
    for i in range(0, m + 1):   # 제일 왼쪽 열
        edit_distances[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 두 글자가 같다면
            if str1[i - 1] == str2[j - 1]:
                edit_distances[i][j] = edit_distances[i - 1][j - 1]
            # 두 글자가 다르다면
            else:
                edit_distances[i][j] = min(edit_distances[i][j - 1], \
                                            edit_distances[i - 1][j], \
                                            edit_distances[i - 1][j - 1]) + 1

    # 완성된 EditD 행렬을 출력해봅니다.
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            print('%2d' % edit_distances[i][j], end = '')
        print()
    
    return edit_distances[m][n]

str1, str2 = input('두 단어를 입력하세요 : ').split()
print('두 단어 [%s] [%s] 사이의 최소 교정 비용은 %d입니다.' % \
    (str1, str2, edit_distance(str1, str2, len(str1), len(str2))))