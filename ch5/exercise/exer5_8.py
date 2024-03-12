# 완전탐색법 + 백트래킹 해법으로 구현해 보겠습니다.
def subset_for_sum1(arr, X, current = 0, before_subset = None):
    if before_subset == None:
        before_subset = []
    # 종료조건 1 - 더 이상 남은 원소가 없을 때
    if current == len(arr):
        return None
    before_sum = sum(before_subset)
    # 종료조건 2 - 이전에 만들어진 부분 집합의 합이 목표값 X를 초과했을 때 (백트래킹 - 더 이상 탐색할 필요가 없음)
    if before_sum > X:
        return None
    result = []
    # 이미 만들어진 이전 단계의 부분 집합에 현재 원소를 더했을 때 목표값이 되면
    # 현재 원소를 더한 부분 집합을 결과 목록에 추가
    current_sum = before_sum + arr[current]
    if current_sum == X:
        result.append(before_subset + [arr[current]])
    # 현재 원소를 부분 집합에 추가한 후 재귀 호출
    following_result_with_current = subset_for_sum1(arr, X, current + 1, before_subset + [arr[current]])
    if following_result_with_current != None:
        result += following_result_with_current
    
    # 현재 원소를 부분 집합에 추가하지 않고 재귀 호출
    following_result_without_current = subset_for_sum1(arr, X, current + 1, before_subset)
    if following_result_without_current != None:
        result += following_result_without_current
    return result

arr = [0, 6, 11, 8, 17, 3, 9]
print(subset_for_sum1(arr, 14))
    
