MIN = 2
MAX = 10
p = 100

memo = {}

def Q(no, yes):
    key = str([no, yes])

    if key in memo:
        return memo[key]
    if no < 0:
        return 0
    if no == 0:
        return 1
    
    # 재귀 처리
        count = 0
        for i in range(yes, MAX + 1):
            count += Q(no - 1, i)
    # 메모화 처리
        memo[key] = count
    # 종료
        return count
    
print(Q(p, MIN))