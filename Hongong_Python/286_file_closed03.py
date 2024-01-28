try:
    file = open("./txt/286_file_closed03.txt", "w")
    예외.발생해라()
except Exception as e: 
    print(e)
finally:
    file.close()

print("파일이 닫혔는지 확인")
print(file.closed)