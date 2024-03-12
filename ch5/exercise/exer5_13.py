# 참고로 각 금액마다 메모를 제공해야 하는 이 예제는 메모 사용이 제한적일 수
# 있습니다. 예를 들어서 (가능성은 낮지만) 1억 원에 대해서 계산을 해야 하면 
# 1억 개의 원소를 가진 리스트 크기만큼의 메모리가 필요합니다.

# 아래 함수에서 동전 셋을 만들 때 고려해야 할 사항은 최소 동전의 개수의
# 동전 구성 하나만이 아니라 모두를 찾아야 한다는 점 입니다.
# 이를 위해서 최소 동전 개수가 동일한 경우는 이전 경우를 덮어 쓰지 않고
# 추가하는 방식으로 구현해야 합니다.
def min_coins(coin, N, S):
    # resultArray[i]에는 i원을 거슬러줄 때 필요한 최소 동전의 
    # 개수를 저장합니다. 마지막에 resultArray[S]를 반환합니다.
    # 최솟값을 구하기 위해서 충분히 큰 값으로 초기화하면 되는데
    # 동전의 개수는 구하려는 금액(S)보다 클 수 없으므로 S의 값으로
    # 초기화합니다.    
    result_array = [S + 1] * (S + 1)

    # 최적의 동전 조합을 나타내는 딕셔너리를 금액별로 저장합니다. 
    # 처음에는 0원의 조합(아무 동전도 선택하지 않음)으로 초기화합니다.
    result_coinsets = {0: [[]]}
    
    # S = 0일 때. 
    result_array[0] = 0

    # 1원부터 계산해 올라갑니다.
    for i in range(1, S + 1):
        for j in range(0, N):
            # 현재 구하려는 금액보다 작은 액면가의 동전에 대해서만 검사
            if coin[j] <= i:
                temp = result_array[i - coin[j]]
                # 만약 현재의 조건이 최소 개수의 동전에 해당한다면
                if temp + 1 <= result_array[i]:
                    new_coinsets = []
                    # 추가할 동전 조합을 업데이트 합니다.
                    for result_coinset in result_coinsets[i - coin[j]]:
                        # 동전 조합이 중복되기 때문에 정렬한 후 중복 여부를 확인
                        new_coinset = sorted(result_coinset + [coin[j]])
                        if new_coinset not in new_coinsets:
                            new_coinsets.append(new_coinset)
                    # 최소 동전 개수가 바뀔 때는 동전 조합을 변경
                    if temp + 1 < result_array[i]:
                        result_array[i] = temp + 1
                        result_coinsets[i] = new_coinsets
                    # 최소 동전 개수가 같을 때는 동전 조합을 추가
                    else:
                        # 동전 조합이 중복될 수 있기 때문에 중복 여부를 확인하고 추가
                        for new_coinset in new_coinsets:
                            if new_coinset not in result_coinsets[i]:
                                result_coinsets[i].append(new_coinset)
    return result_array[S], result_coinsets[S]

# 아래 코드는 만약 구조를 금액 -> 동전 구조가 아닌 동전 -> 금액 구조로 구현하는 경우입니다.
# 참고가 되기 바랍니다.
def min_coins2(coins, S):
    # 충분히 큰 값으로 초기화 할 때 파이썬에서는 float('inf')를 사용하면 됩니다.
    result_array = [float('inf')] * (S + 1)
    result_coinsets = {}
    result_array[0] = 0
    result_coinsets[0] = []
    
    for coin in coins:
        for value in range(coin, S + 1):
            if result_array[value] > result_array[value - coin] + 1:
                result_array[value] = result_array[value - coin] + 1
                result_coinsets[value] = result_coinsets[value - coin] + [coin]
    if result_array[S] == float('inf'):
        return -1, {}
    result_coin_dict = {}
    for coin in result_coinsets[S]:
        if coin not in result_coin_dict:
            result_coin_dict[coin] = 1
        else:
            result_coin_dict[coin] += 1
    return result_array[S], result_coin_dict    

coin = [1, 5, 6, 9]
N = len(coin)
for S in range(0, 20):
    min_coin_count, result_coin_sets = min_coins(coin, N, S)
    print('%d원을 지불할 때 최소 동전의 개수는 %d개입니다.' % (S, min_coin_count))
    print('동전 구성 방법 -', result_coin_sets)
    print()