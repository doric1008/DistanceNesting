from Common import *


class Item_a1:
    #list_a1为输入的角度的列表
    #输入 [15, 30, 45, 60, 90]
    #self.angle_a1 ： [(15, 30), (30, 45), (45, 60), (60, 90)]

    def __init__(self, list_a1):
        self.angle_a1 = Common.split_list(list_a1)
        self.data_dictionary = {}
        self.distance = 0

    def input_a1(self, list_distance):

        #此时输出的结果为角度元组加距离的字典
        #{(60, 90): 60, (15, 30): 15, (45, 60): 45, (30, 45): 30}

        for i, list_a1_sub in enumerate(self.angle_a1):
            self.data_dictionary[list_a1_sub] = list_distance[i]
        return self.data_dictionary

    # a1是输入的角度
    # 返回距离
    def get_distance(self, test_a1):
        for key, value in self.data_dictionary.items():
            if test_a1 == 90:
                if key[1] == 90:
                    self.distance = value
                    return self.distance
            if (key[0] <= test_a1 and test_a1 < key[1]):
                self.distance = value
                return self.distance


a = [0, 15, 30, 45, 60, 90]
t = [10, 12, 45, 60, 80]
test = Item_a1(a)
test.input_a1(t)
print(test.get_distance(90))



