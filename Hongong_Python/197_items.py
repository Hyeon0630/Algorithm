dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

print(dictionary.items())

for key, element in dictionary.items():
    print("dictionary[{}] = {}".format(key, element))