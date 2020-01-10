#from math import ceil



def myFn(x):
    return ceil(x)

def ceil(x):
    # only works for +
    print("this is my ceil")
    if x - int(x) == 0:
        return x
    elif x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

