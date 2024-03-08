# 양쪽 문자열 각각에서 첫 번째 글자를 재외한 인터리빙 목록을 만든 후(재귀 호출), 첫 번째 글자를 붙인 다음
# 두 목록을 합칩니다.
# 이 함수는 메모이제이션이 불가능합니다. 재귀호출하는 패턴이 이전에 존재할 수 없기 때문입니다.
def make_interleavings(A, B):
    if len(A) == 0:
        return [B]
    if len(B) == 0:
        return [A]
    result = []
    for following_interleaving in make_interleavings(A[1:], B):
        result.append(A[0] + following_interleaving)
    for following_interleaving in make_interleavings(A, B[1:]):
        result.append(B[0] + following_interleaving)
    return result

a = 'AB'
b = 'XY'
print(make_interleavings(a, b))