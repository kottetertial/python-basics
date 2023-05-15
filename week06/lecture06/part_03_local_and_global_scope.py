def func():
    print(a)


a = 10
func()


def another_func():
    b = 10


def yet_another_func():
    global b
    b = 10


b = 15
another_func()
print(b)
yet_another_func()
print(b)
