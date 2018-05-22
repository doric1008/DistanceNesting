import types

class Common:

    @classmethod
    def split_list(self,a):
        #[1,7,3,4,5]  input
        #[(1, 7), (7, 3), (3, 4), (4, 5)]  output
        return [(a[i], a[i + 1]) for i, _ in enumerate(a) if i < len(a) - 1]

    def convert_string(string):
        if isinstance(string, str):
            return eval(string)
        else:
            return string




a = 3*15 +34 *0.8
b = Common.convert_string(a)
print(b)
