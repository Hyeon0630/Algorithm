S = input()
T = [input()]

ans = 0

while T:
    t = T.pop(0)
    if t == S:
        ans = 1
    elif len(t) < len(S):
        break

    if t[0] == "B":
        T.append(t[1:][::-1])

    if t[-1] == "A":
        T.append(t[:-1])

print(ans)