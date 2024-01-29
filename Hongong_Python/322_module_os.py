import os

print("현재 운영체:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더의 내부 주소:", os.listdir())

# 폴더를 만들고 제거(폴더가 비어있을 때만 제거 가능)
os.mkdir("322_module_os_folder")
os.rmdir("322_module_os_folder")

# 파일 생성 후 파일명 변경
with open("./txt/322_module_os.txt", "w") as file:
    file.write("hello")
os.rename("./txt/322_module_os.txt", "./txt/322_module_os_new.txt")

# 파일 제거
os.remove("./txt/322_module_os_new.txt")

# 시스템 명령어 실행
os.system("dir")