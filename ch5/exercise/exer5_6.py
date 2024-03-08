# 두 문자열에 겹치는 글자가 없는 경우, 확인하고자 하는 문자열의 첫 번째 글자가
# 두 문자열 중 하나의 첫 번째 글자가 같은 경우에만 인터리빙이 가능합니다.
# 겹치는 글자를 양쪽에서 떼어내고, 모든 글자가 확인될 때 까지 반복합니다.
# 이 때, 한쪽 글자가 빈 문자열이 되면, 남은 쪽의 문자열과 남은 확인 문자열이 동일해야 인터리빙이 가능합니다.
# 이 알고리즘은 추가로 사용하는 추가 공간이 길이와 무관하게 정해져 있으며 (O(1))
# 실행 시간은 두 문자열의 길이에 비례합니다. (O(m + n))
def is_interleaving(A, B, C):
    # C가 빈 문자열이 아닐 때
    while C:
        # A, B가 빈 문자열이면 실패
        if not A and not B:
            return False
        # B가 빈 문자열일 때 A와 C가 같아야 함
        if not B:
            return True if A == C else False
        # A가 빈 문자열일 때 B와 C가 같아야 함
        if not A:
            return True if B == C else False
        # A, B가 둘 다 빈 문자열이 아닐 때
        # A의 첫 글자와 C의 첫 글자가 같으면 양 쪽에서 첫 글자를 떼어내고 반복
        if A[0] == C[0]:
            A = A[1:]
            C = C[1:]
        # B의 첫 글자와 C의 첫 글자가 같으면 양 쪽에서 첫 글자를 떼어내고 반복
        elif B[0] == C[0]:
            B = B[1:]
            C = C[1:]
        # 양쪽 첫 글자 중 어느 쪽도 C의 첫 글자와 일치하지 않으면 실패
        else:
            return False
    return True

a = 'abc'
b = 'defg'
c = 'dabefcg'
check = is_interleaving(a, b, c)
print('%s는 %s와 %s의 인터리빙' % (c, a, b), end = '')
if check:
    print('입니다.')
else:
    print('이 아닙니다.')

a = 'abc'
b = 'defg'
c = 'daxefcg'
check = is_interleaving(a, b, c)
print('%s는 %s와 %s의 인터리빙' % (c, a, b), end = '')
if check:
    print('입니다.')
else:
    print('이 아닙니다.')
