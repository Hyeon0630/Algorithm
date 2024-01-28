memo = {}

def graph(p, upper):
    count = 0
    key = (p, upper)
    if key in memo:
        return memo[key]
    if p == 0:
        count += 1
    for i in range(max(2, upper), min(p, 10)+1):
        count += graph(p-i, i)
    memo[key] = count    
    return count

print(graph(100, 0))