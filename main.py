list = []


def input_num():
    x = float(input())
    if x % 1 == 0:
        if x > 1:
            collatz(x)
        else:
            input_num()
    else:
        input_num()


def x2(x):
    pass


def x3_1(x):
    pass


def collatz(x):
    pass


input_num()
