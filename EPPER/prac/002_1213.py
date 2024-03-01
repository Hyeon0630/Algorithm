import sys
input = sys.stdin.readline

name = list(input())
name.pop()

def solution(name):
    dict = {}
    cnt = 0
    c = 0

    for i in name:
        if i not in dict:
            dict[i] = 1
        else:
            cnt = int(dict[i])
            cnt += 1
            dict[i] = cnt

    for i in dict.values():
        if i % 2 == 1:
            c += 1

    if c > 1:
        answer = "I'm Sorry Hansoo"
    elif  c == 1:
        a = [k for k, v in dict.items() if v % 2 == 1]
        d = {k:(v//2) for k, v in dict.items()}
        b = list()
        for i in d.keys():
            for j in range(d[i]):
                b.append(i)
        b.sort()
        answer = "".join(b)+"".join(a)+"".join(reversed(b))
    else:
        d = {k:(v//2) for k, v in dict.items()}
        a = list()
        for i in d.keys():
            for j in range(d[i]):
                a.append(i)
        a.sort()
        answer = "".join(a)+"".join(reversed(a))
    return answer

ans = solution(name)
print(ans)