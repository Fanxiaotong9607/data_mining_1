import random
import math

def func(x, y):#目标函数
    result = math.pow(x - y, 2) + math.pow(x - 2, 2) + math.pow(y - 3, 4)
    return result

def get_dict(res_dict):#获取坐标：值的dict
    for i in range(4):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        result = func(x, y)
        loc = (x, y)
        res_dict[loc] = result
    return res_dict

def get_max(res_dict):#获取最大函数值在dict中的index
    flag = 0
    value_list = res_dict.values()
    for value in value_list:
        max_value = value
        break
    for r in res_dict:
        if res_dict[r] >= max_value:
            max_value = res_dict[r]
            index = flag
            flag += 1
        else:
            flag += 1
    return index

def get_min(res_dict):#获取最小函数值在dict中的index
    flag = 0
    value_list = res_dict.values()
    for value in value_list:
        min_value = value
        break
    for r in res_dict:
        if res_dict[r] <= min_value:
            min_value = res_dict[r]
            index = flag
            flag += 1
        else:
            flag += 1
    return index

def get_mid(res_dict):#获取中间坐标）
    x = 0
    y = 0
    for res in res_dict:
        x += res[0]
        y += res[1]
    mean_x = x/len(res_dict)
    mean_y = y/len(res_dict)
    mean = [mean_x, mean_y]
    return mean

def get_z1(index, mean, res_dict):
    flag = 0
    for res in res_dict:
        if flag == index:
            cord = res
            break
        else:
            flag += 1
        #cord是（x,y）
    new_cord_x = mean[0] - (cord[0] - mean[0])
    new_cord_y = mean[1] - (cord[1] - mean[1])
    cord_z1 = [new_cord_x, new_cord_y]
    z1 = func(new_cord_x, new_cord_y)
    result = [cord_z1, z1]
    return result

def get_z2(index, mean, res_dict):
    flag = 0
    for res in res_dict:
        if flag == index:
            cord = res
            break
        else:
            flag += 1
    new_cord_x = mean[0] - 2*(cord[0] - mean[0])
    new_cord_y = mean[1] - 2*(cord[1] - mean[1])
    cord_z2 = [new_cord_x, new_cord_y]
    z2 = func(new_cord_x, new_cord_y)
    result = [cord_z2, z2]
    return result

def get_z3(index, mean, res_dict):
    flag = 0
    for res in res_dict:
        if flag == index:
            cord = res
            break
        else:
            flag += 1
    new_cord_x = cord[0] - 0.5*(cord[0] - mean[0])
    new_cord_y = cord[1] - 0.5*(cord[1] - mean[1])
    cord_z3 = [new_cord_x, new_cord_y]
    z3 = func(new_cord_x, new_cord_y)
    result = [cord_z3, z3]
    return result

def get_z4(index_min, index_max, mean, res_dict):
    flag = 0
    for res in res_dict:
        if flag == index_min:
            cord_min = res
            break
        else:
            flag += 1
    flag = 0
    for res in res_dict:
        if flag == index_max:
            cord_max = res
            break
        else:
            flag += 1
    new_cord_x = cord_max[0] - 0.5*(cord_max[0] - cord_min[0])
    new_cord_y = cord_max[1] - 0.5*(cord_max[1] - cord_min[1])
    cord_z4 = [new_cord_x, new_cord_y]
    z4 = func(new_cord_x, new_cord_y)
    result = [cord_z4, z4]
    return result

if __name__ == '__main__':
    res_dict = {}
    res_dict = get_dict(res_dict)#获取随机生成的四个坐标和计算所得的函数值
    tol = 0.0000001
    while(True):
        index_max = get_max(res_dict)
        index_min = get_min(res_dict)
        flag_res = 0
        tag = 0
        for res in res_dict:#获取index对应的value函数值
            if flag_res == index_max:
                max_value = res_dict[res]
                tag += 1
                flag_res += 1
            elif flag_res == index_min:
                min_value = res_dict[res]
                tag += 1
                flag_res += 1
            else:
                if tag == 2:
                    break
                else:
                    flag_res += 1
        if abs(max_value - min_value) <= tol:#满足最优解条件时
            print(res_dict)
            break
        else:
            mean = get_mid(res_dict)
            result_list = []#分析四种分散方法对应的z函数值
            result_list.append(get_z1(index_max, mean, res_dict))
            result_list.append(get_z2(index_max, mean, res_dict))
            result_list.append(get_z3(index_max, mean, res_dict))
            result_list.append(get_z4(index_max, index_min, mean, res_dict))
            index = 0
            flag = 0
            min = result_list[0][1]#得到最小的函数值
            for r in result_list:#获取最小的z值对应的坐标进行替换
                if result_list[flag][1] <= min:
                    min = result_list[index][1]
                    index = flag
                    flag += 1
                else:
                    flag += 1
            z = result_list[index][1]
            z_cord = tuple(result_list[index][0])#(x,y)
            tmp = 0
            for res in res_dict:#去掉最大的点
                if tmp == index_max:
                    res_dict.pop(res)
                    break
                else:
                    tmp += 1
            res_dict[z_cord] = z#更新dict
