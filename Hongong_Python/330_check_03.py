import os



def read_folder(path):
    # 현재 폴더의 파일/폴더를 출력
    output = os.listdir(path)

    # 현재 폴더의 파일/폴더를 구분
    for p in output:
        if os.path.isdir(p):
            print("폴더:", p)
            read_folder("./" + p)
        else:
            print("파일:", p)

read_folder(".")