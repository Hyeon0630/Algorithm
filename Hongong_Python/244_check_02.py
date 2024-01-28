MIN = 2
MAX = 10
p = 100

memo = {}

def Q(no, yes): # 98 2 10 90
    count = 0
    key = str([no, yes])

    if key in memo:
        return memo[key]
    if no < 0:
        return count
    if no == 0:
        return count
    
    # 재귀 처리
        for i in range(yes, no + 1): # i = 2~100
            if no > MAX:
                yes += i # 4
                no -= i # 96
                Q(no, yes)
            else:

    # 메모화 처리
        memo[key] = count
    # 종료
        return count
    
print(Q(p-MIN, MIN))