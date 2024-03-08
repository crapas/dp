# 다음은 다이나믹 프로그래밍을 사용하지 않고,
# O(n log n)의 시간 복잡도, O(1)의 공간 복잡도를 가지는 알고리즘입니다.
# 우선 주어진 리스트를 정렬합니다.
# 참고로 파이썬의 sort, sorted 함수는 팀소트(Timsort)라는 알고리즘을 사용합니다.
# 이 알고리즘의 시간 복잡도는 O(n log n)입니다.
# 다만 팀소트 알고리즘의 공간 복잡도는 O(n)이므로, 대신 공간 복잡도가 O(1)인 힙 정렬 알고리즘을 사용합니다.
# 그 다음, 리스트의 첫 번째 원소와 마지막 원소를 가리키는 포인터를 두고,
# 합이 목표값보다 크면 마지막 원소 (가장 큰 원소) 포인터를 한 칸 앞으로 이동하고,
# 합이 목표값보다 작으면 첫 원소 (가장 작은 원소) 포인터를 한 칸 뒤로 이동합니다.
# 가리키는 두 원소의 합이 목표값과 같으면 쌍에 추가한 후, 두 포인터를 각각 앞 뒤로 한 칸씩 이동합니다.
# 이 과정을 두 포인터가 만날 때까지 반복합니다.
# 이 과정은 최악의 경우에도 루프의 반복 회수가 n - 1회이므로 O(n)입니다.
# 두 과정이 병렬적으로 수행되므로, 두 과정 중 시간 복잡도가 큰 정렬을 기준으로 알고리즘의 시간 복잡도가 결정됩니다.
# 공간 복잡도는 힙 정렬을 사용하여 O(1)의 공간 복잡도를 가집니다. (단 결과를 저장하는 리스트는 제외합니다.)
# 배열에 같은 값이 중복되는 경우, 같은 쌍이 여러 번 나올 수 있습니다. 
# 중복된 쌍이 포함되지 않도록 구현한 예시입니다.

def heapify(arr, n, i):
    most = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[most] < arr[left]:
        most = left
    if right < n and arr[most] < arr[right]:
        most = right
    if most != i:
        arr[i], arr[most] = arr[most], arr[i]
        heapify(arr, n, most)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def find_pair(arr, X):
    # 정렬합니다. - O(n log n)
    heap_sort(arr)
    n = len(arr)
    i, j = 0, n - 1
    result = []
    # 루프의 최대 반복 회수는 n - 1회입니다. - O(n)
    while i < j:
        if arr[i] + arr[j] == X:
            if (arr[i], arr[j]) not in result:
                result.append((arr[i], arr[j]))
            i += 1
            j -= 1
        elif arr[i] + arr[j] > X:
            j -= 1
        else:
            i += 1
    return result

arr = [0, 6, 11, 8, 17, 3, 9]
print(find_pair(arr, 17))
print(find_pair(arr, 14))
print(find_pair(arr, 13))
arr = [1, 1, 1, 2, 2]
print(find_pair(arr, 3))