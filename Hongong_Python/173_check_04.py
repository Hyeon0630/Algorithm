character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) == type([]):
        for i in character[key]:
            print(key, ":", i)
    elif type(character[key]) == type({}):
        for j in character[key]:
            print(j, ":", character[key][j])
    else:
        print(key, ":", character[key])

# 답지 답안

""" for key in character:
    if type(character[key]) is list:
        for i in character[key]:
            print(key, ":", i)
    elif type(character[key]) is dict:
        for j in character[key]:
            print(j, ":", character[key][j])
    else:
        print(key, ":", character[key]) """