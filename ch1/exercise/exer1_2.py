# 재귀의 초기 값이 고정된 경우 아래와 같이 기본 파라미터를 사용할 수 있습니다.
# 파이썬 리스트는 mutable 객체로서, 함수 호출 전 후에 변형된 내용이 그대로 유지되는
# 특성이 있기 때문에 아래와 같이 리스트를 반환하지 않고 구현할 수 있습니다.

def cumulative_sum(arr, n = 0):
    if len(arr) <= n + 1:
        return    
    arr[n + 1] += arr[n]
    cumulative_sum(arr, n + 1)

arr = [1, 2, 3, 4, 5, 6]
cumulative_sum(arr)
print(arr)