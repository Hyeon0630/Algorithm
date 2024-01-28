def call(func):
    for i in range(10):
        func()

def func():
    print("HI")

call(func)