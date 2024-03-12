from random import randint

# 공간 복잡도가 O(1)이라는 말의 의미는 문자열의 길이가 아무리 길어지더라도
# 이 알고리즘이 사용하는 메모리는 문자열의 길이에 따라 증가하지 않는다는 의미입니다.

# 아래 구현한 알고리즘은 다음과 같습니다.
# 바깥쪽 루프는 전제 문자열을 대상으로 숫자와 숫자 사이의 모든 틈새에 대해서 루프를 구성합니다.
# 문자열의 길이가 n일 때 n - 1번 반복합니다.
# 안쪽 루프는 각 틈새부터 문자열의 처음 또는 끝 까지 먼저 도달할 때 까지 한 글자씩 차례로 
# 추가하면서 합을 계산해 나갑니다. 이 과정에서 합이 같은 경우 지금까지 찾은 가장 긴 
# 조건에 맞는 부분 문자열과 길이를 비교해서, 더 긴 경우 이 값을 갱신해서 전체 문자열에
# 대해서 조건에 맞는 가장 길이가 긴 부분 문자열을 찾습니다.

# 아래 구현은 이 조건에 맞는 부분 문자열도 찾아서 반환하도록 구현되어 있습니다.
# 루프는 모두 n에 비례하는 2중 루프이고, 추가적인 루프는 없으므로 시간 복잡도 n^2 함수에 
# 해당됩니다. 공간 복잡도의 경우는 문자열의 길이가 증가해도 
# 추가적으로 공간이 늘어나지 않기 때문에 O(1)의 알고리즘에 해당됩니다.

# 일부 구현 방식은 경우는 2중 루프와 sum 함수를 사용하는데, 리스트에서 sum 함수 자체가
# 최악의 경우 O(n)이 되기 때문에 엄밀한 의미로 O(n^2) 알고리즘이라고 할 수 없습니다.
# 참고로 아래 구현에서 result가 리스트인 이유는 1111541111과 같이 길이 4인 조건에 맞는
# 문자열이 두 개 존재할 수 있기 때문입니다.

def max_substring_length(str):
    length = len(str)
    max_length = 0
    result_idx = []

    for i in range(1, length):
        front_sum = 0
        back_sum = 0
        k = 0
        while i - k > 0 and i + k < length:
            front_sum += int(str[i - 1 - k])
            back_sum += int(str[i + k])
            if front_sum == back_sum:
                if (k + 1) * 2 > max_length:
                    result_idx = [(i - 1 - k, i + k)]
                    max_length = (k + 1) * 2
                elif (k + 1) * 2 == max_length:
                    result_idx.append((i - 1 - k, i + k))
                max_length = max(max_length, (k + 1) * 2)
            k += 1
    
    result = []
    for (start_idx, end_idx) in result_idx:
        result.append(str[start_idx:end_idx + 1])
    
    return max_length, result


n = int(input('생성할 숫자열의 길이를 입력하세요 : '))

# 길이 n의 무작위 난수 숫자열을 만듭니다.
numstr = str(randint(1, 9))
for x in range(1, n):
    numstr += str(randint(0, 9))

print('생성된 숫자열 : %s' % numstr)

max_length, result = max_substring_length(numstr)

print('결과 : %d' % max_length)
print('결과에 해당하는 부분 문자열 :', result)