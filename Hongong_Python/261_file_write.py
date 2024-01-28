import random

hanguls = list("가나다라마바사아자차카타파하")

with open("261_file_write_basic.txt", "w") as file:
    for i in range(100):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))
