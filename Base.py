import Common
from Item_a2 import *
from Item_a1 import *


class Base:
    def __init__(self, list_a2):
        self.list_a2 = list_a2
        self.angle_a2 = Common.split_list(list_a2)
        self.zone = 0  # "01" 表示第一行第二列
        self.block_num = 0  # 有几行几列a2的值
        self.list_block = []  # 包含Item_a2类的列表
        self.list_block_dict = []  # 包含Item_a2类里面的字典的列表，这个不用
        self.data_a2_dictionary = {}
        self.data_a2_dictionary_who_use = {}

    def input_a2(self, dict_a2_value):

        # 此时输出的结果为角度元组加距离的字典
        # {(60, 90): 60, (15, 30): 15, (45, 60): 45, (30, 45): 30}

        for i, list_a1_sub in enumerate(self.angle_a2):
            self.data_a2_dictionary[list_a1_sub] = dict_a2_value[i]
        return self.data_a2_dictionary

    def create_a2(self):

        for i, list_a1_sub in enumerate(self.angle_a2):
            temp = Item_a2(list_a1_sub)
            temp.input_a2(self.data_a2_dictionary.get(list_a1_sub))
            #temp.input_a2(dic.get('dic' + str(i)))
            self.list_block.append(temp)
            self.list_block_dict.append(temp.data_a2_dictionary)

    def get_a2(self, test_a2):
        for key, value in self.data_a2_dictionary.items():
            if test_a2 == 90:
                if key[1] == 90:
                    self.data_a2_dictionary_who_use = value
                    return self.data_a2_dictionary_who_use
            if (key[0] <= test_a2 and test_a2 < key[1]):
                self.data_a2_dictionary_who_use = value
                return self.data_a2_dictionary_who_use



#此列可以想象成每个a2单元的矩阵，因为层高取值为2组，所以组合共4种情况
#d值为a1的取值范围，因为a1有两个范围，所有d有两个取值
dic0 = {"a00": [0, 45, 90], "d00": [35, 35],
        "a01": [0, 45, 90], "d01": [35, 35],
        "a02": [0, 45, 90], "d02": [13, 13],
        "a10": [0, 45, 90], "d10": [35, 35],
        "a11": [0, 45, 90], "d11": [35, 35],
        "a12": [0, 45, 90], "d12": [18, 18],
        "a20": [0, 45, 90], "d20": [24, 13],
        "a21": [0, 45, 90], "d21": [24, 18],
        "a22": [0, 45, 90], "d22": [30, 30]}

dic1 = {"a00": [0, 45, 90], "d00": [28, 28],
        "a01": [0, 45, 90], "d01": [28, 28],
        "a02": [0, 45, 90], "d02": [10.4, 10.4],
        "a10": [0, 45, 90], "d10": [28, 28],
        "a11": [0, 45, 90], "d11": [28, 28],
        "a12": [0, 45, 90], "d12": [14.4,14.1],
        "a20": [0, 45, 90], "d20": [0, 0],
        "a21": [0, 45, 90], "d21": [0, 0],
        "a22": [0, 45, 90], "d22": [24, 24]}

dic2 = {"a00": [0, 45, 90], "d00": [6, 6],
        "a01": [0, 45, 90], "d01": [8, 8],
        "a02": [0, 45, 90], "d02": [13, 13],
        "a10": [0, 45, 90], "d10": [8, 8],
        "a11": [0, 45, 90], "d11": [10, 10],
        "a12": [0, 45, 90], "d12": [13,13],
        "a20": [0, 45, 90], "d20": [13,13],
        "a21": [0, 45, 90], "d21": [13, 13],
        "a22": [0, 45, 90], "d22": [24, 24]}
#因为a2的取值范围为两个，所以dic有两个值
dic = [dic0, dic1,dic2]

#a2的取值范围
c = [0, 30, 90]
#a1的取值范围
a = [0, 45, 90]
#层高的取值范围
b = [1, 4, 10, 1000]
test3 = Base(c)
print(test3.input_a2(dic))

#选择适当的a2角度
test3.get_a2(50)

test2 = Item_a2(c)
test2.floor_corresponding(b)

test2.data_a2_dictionary = test3.data_a2_dictionary_who_use

print(test2.data_a2_dictionary)

test2.create_a1(test2.data_a2_dictionary)

print(test2.list_block_dict)

#选择对应的层数
print(test2.get_zone(15, 15))
tt = test2.zone_to_a1()
print(tt.data_dictionary)

#选择a1的度数
print("所选择的建筑高度为：" + str(tt.get_distance(45)))

#print(test3.list_block_dict)
#最终的字典形式，综合a1,a2,f
#print(test3.data_a2_dictionary)





