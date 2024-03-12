def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 파이썬에서 두 변수의 값을 서로 바꾸려고 할 때는 다음과 같이 간단하게
                # 구현할 수 있습니다.
                # a, b = b, a (코드 1-11의 파이썬 버전은 생략합니다.)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

a = [10, 2, 6, 4, 5, 3, 2, 8]
print('원래 순서 : ', end = '')
print(a)
bubble_sort(a)
print('정렬 결과 : ', end = '')
print(a)