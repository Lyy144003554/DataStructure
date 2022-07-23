# -*- coding=utf-8 -*-
# name: nan chen
# date: 2021/3/25 15:03
import os


# 统计代码行数
def count_codes(path):
    # 返回指定的文件夹包含的文件/文件夹的名字的列表
    file_list = os.listdir(path)
    # 改变当前工作路径
    os.chdir(path)
    nn = ("'''", '"""')
    totalcodes, totalnulls, totalnotes = 0, 0, 0
    for file in file_list:
        if file.endswith('.py'):
            total, codes, nulls, notes = 0, 0, 0, 0
            # 标记多行注释
            isMutinotes = False
            lines = open(file, encoding='utf-8').readlines()
            for line1 in lines:
                line = line1.strip()
                if line.startswith('#'):
                    notes += 1
                elif line.startswith(nn):
                    if line.endswith(nn) and len(line) > 3:
                        notes += 1
                        isMutinotes = False
                        continue
                    if not isMutinotes:
                        isMutinotes = True
                        notes += 1
                    elif isMutinotes:
                        isMutinotes = False
                        notes += 1
                elif isMutinotes:
                    notes += 1
                elif not isMutinotes and len(line) == 0:
                    nulls += 1
                else:
                    codes += 1
            total = nulls + codes + notes
            totalcodes = totalcodes + total  # 代码行数
            totalnulls = totalnulls + nulls
            totalnotes = totalnotes + notes
            # print("%s 有代码%d行 空行%d行 注释%d行" % (file, total, nulls, notes))
    print("%s目录下python程序文件共有代码%d行 空行%d行 注释%d行" % (path, totalcodes, totalnulls, totalnotes))
    return totalcodes


if __name__ == '__main__':
    # count_codes("D:\computerVision")
    t1 = count_codes("C:/Users/lyy14/PycharmProjects/pythonProject/DatastructureHomework")
    t2 = count_codes("C:/Users/lyy14/PycharmProjects/pythonProject/DatastructureHomework/ASFunction")
    t3 = count_codes("C:/Users/lyy14/PycharmProjects/pythonProject/DatastructureHomework/ImageCutFounction")
    t4 = count_codes("C:/Users/lyy14/PycharmProjects/pythonProject/DatastructureHomework/GUIFunction")
    print("DataStructure Homework共有{0}行代码".format(t1+t2+t3+t4))

