class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for n in self.my_list:
            for i in n:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

n = Matrix([[31, 22, -12], [37, 43, -23], [51, 86, -21], [3, 5, 8]])
new_m = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8], [8, 3, 7]])
print(n.__add__(new_m))