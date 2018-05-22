from Common import *
from Item_a1 import *


class Item_a2:
    # list_a2为输入的层数的列表
    # 输入 [1， 4， 7, 10]
    # self.angle_a2 ： [(15, 30), (30, 45), (45, 60), (60, 90)]
    def __init__(self, list_a2):
        self.angle_a2 = Common.split_list(list_a2)
        self.data_a2_dictionary = {}
        self.data_a2_dictionary_who_use ={}
        self.list_floor = []
        self.floor = {}
        self.zone = 0      # "01" 表示第一行第二列
        self.block_num = 0  #有几行几列a1的值
        self.list_block = []  #包含Item_a1类的列表
        self.list_block_dict = []  # 包含Item_a1类里面的字典的列表，这个不用

    def input_a2(self, dict_a2_value):

        # 此时输出的结果为角度元组加距离的字典
        # {(60, 90): 60, (15, 30): 15, (45, 60): 45, (30, 45): 30}

        for i, list_a1_sub in enumerate(self.angle_a2):
            self.data_a2_dictionary[list_a1_sub] = dict_a2_value.get(list_a1_sub)
        return self.data_a2_dictionary

    def get_a2(self, test_a2):
        for key, value in self.data_a2_dictionary.items():
            if test_a2 == 90:
                if key[1] == 90:
                    self.data_a2_dictionary_who_use = value
                    return self.data_a2_dictionary_who_use
            if (key[0] <= test_a2 and test_a2 < key[1]):
                self.data_a2_dictionary_who_use = value
                return self.data_a2_dictionary_who_use

    def floor_corresponding(self, list_floor_complete):
        self.list_floor = Common.split_list(list_floor_complete)
        self.block_num = len(self.list_floor)
        for i in self.list_floor:
            self.floor[i] = {}
        for j, list_floor_sub in enumerate(self.list_floor):
            for k, list_floor_sub_sub in enumerate(self.list_floor):
                self.floor[list_floor_sub][list_floor_sub_sub] = 10*j+k
        return self.floor

    def get_zone(self, floor_1, floor_2):
        for key, value in self.floor.items():
            #如果正好等于最后一个楼层，if没有写
            if (key[0] <= floor_1 and floor_1 < key[1]):
                for key1, value1 in value.items():
                    if (key1[0] <= floor_2 and floor_2 < key1[1]):
                        self.zone = value1
                        return self.zone

    def zone_to_a1(self):
        return self.list_block[int(self.zone / 10)][self.zone % 10]

    def create_a1(self, dic):
        for i in range(self.block_num):
            self.list_block.append([])
            self.list_block_dict.append([])
            for j in range(self.block_num):
                temp = Item_a1(dic.get('a' + str(i) + str(j)))
                temp.input_a1(dic.get('d' + str(i) + str(j)))
                self.list_block[i].append(temp)
                self.list_block_dict[i].append(temp.data_dictionary)


dic0 = {"a00": [0, 45, 90], "d00": [10, 50],
        "a01": [0, 45, 90], "d01": [11, 51],
        "a10": [0, 45, 90], "d10": [12, 52],
        "a11": [0, 45, 90], "d11": [13, 53]}

dic1 = {"a00": [0, 45, 90], "d00": [10, 50],
        "a01": [0, 45, 90], "d01": [11, 51],
        "a10": [0, 45, 90], "d10": [12, 52],
        "a11": [0, 45, 90], "d11": [13, 53]}

dic = [dic0, dic1]

a00 = [0, 45, 90]
d00 = [10, 50]

a01 = [0, 45, 90]
d01 = [11, 51]

a10 = [0, 45, 90]
d10 = [12, 52]

a11 = [0, 45, 90]
a12 = [13, 53]





temp = Item_a1(dic0.get('a00'))
temp.input_a1(dic0.get('d00'))
print(temp.data_dictionary)

c = [0, 30, 90]
b = [1, 4, 10]
test2 = Item_a2(c)
test2.floor_corresponding(b)

test2.create_a1(dic0)

print(test2.list_block_dict)

print(test2.get_zone(4, 7))
tt = test2.zone_to_a1()
print(tt.data_dictionary)
print(tt.get_distance(45))




