S = input()
T = [input()]

ans = 0

while T:
    t = T.pop(0) # (1) (4) (6) (8) (9) (12)
    if t == S:
        ans = 1 # (13)
        break
    elif len(t) < len(S):
        break

    if t[0] == "B": # (2) (7) (10)
        T.append(t[1:][::-1])

    if t[-1] == "A": # (3) (5) (11)
        T.append(t[:-1])

print(ans)