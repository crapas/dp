# i = 1부터 1씩 증가하면서 재귀호출합니다.
# i를 기본 파라미터 1의 값으로 지정해서 외부에서 호출할 때는
# i를 지정하지 않고 호출할 수 있도록 구현합니다.
def print_table(n, i = 1):
    # 종료 조건
    if i == 11:
        return
    # 출력 후
    print("%d * %d = %d" % (n, i, (n * i)))
    # 재귀 호출
    print_table(n, i + 1)

print_table(5)