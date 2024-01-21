dictionary = {
    "name": "긴토키",
    "age": 27,
    "sex": "남성",
    "family": ["신파치", "카구라"]
}

print("이름 : " + dictionary["name"])
print("나이 :", dictionary["age"])
print("성별 : " + dictionary["sex"])
print("해결사 구성원 :", dictionary["family"])

print()

dictionary["family"].append("사다하루")
print("해결사 구성원 :", dictionary["family"])