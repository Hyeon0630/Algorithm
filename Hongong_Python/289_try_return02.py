def file(path, text):
    try:
        file = open("./txt/289_try_return02.txt", "w")
        # return
        file.write(text)
        return
    except Exception as e: 
        print(e)
    finally:
        file.close()

file("./txt/289_try_return02.txt", "안녕하세요")