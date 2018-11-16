import numpy
import tensorflow
import random

def func(x, y):
    result = (x - y)^2 + (x - 3)^2 + (y - 2)^2
    return result

def get_dict(res_dict):
    for i in range(1,4):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        result = func(x, y)
        loc = [x, y]
        res_dict[loc] = result

def get_max(res_dict):
    flag = 0
    max_value = res_dict.keys()[1]
    for r in res_dict:
        if res_dict[r] >= max_value:
            max_value = res_dict[r]
            index = flag
            flag += 1
        else:
            flag += 1
    return index
