def flatten(data):
    result = []
    for i in data:
        if (type(i) is list):
            result += flatten(i)
        else:
            result.append(i)
    return result
    
example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))