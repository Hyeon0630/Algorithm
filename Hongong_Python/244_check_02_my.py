def sit(rest, sitted) : 
    count = 0
    if rest == 2:
        count += 1
        return count
    elif rest == 1:
        return count
    elif 2 < rest <= 100:
        for i in (2, 11):
            rest -= i
            sitted += i
            return sit(rest, sitted)

print(sit(4, 2))