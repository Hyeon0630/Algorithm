file01 = open('./txt/257_file_open_basic01.txt', "w")

file01.write("HI")

file01.close()

with open('./txt/257_file_open_basic02.txt', "w") as file02:
    file02.write("Hello")