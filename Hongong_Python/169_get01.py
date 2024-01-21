dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

value_a = dictionary.get("존재하지 않는 키")
value_b = dictionary.get("존재하지 않는 키2", 1)
value_c = dictionary.get("name")

print("value_a의 값 :", value_a)
print("value_b의 값 :", value_b)
print("value_c의 값 :", value_c)

if value_a == None:
    print("존재하지 않는 키에 접근했습니다.")

if value_b == 1:
    print("존재하지 않는 키2에 접근했습니다.")