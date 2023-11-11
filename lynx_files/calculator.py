import math

class Calculator:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
    def Result(self, result):
        return f"Your desired answer is {result}."

class Core4(Calculator):
    def AddFunc(self):
        return super().Result(self.num1 + self.num2)
    def SubtractFunc(self):
        return super().Result(self.num1 - self.num2)
    def DivideFunc(self):
        return super().Result(self.num1 / self.num2)
    def MultiplyFunc(self):
        return super().Result(self.num1 * self.num2)

class AdditionalOps(Calculator):
    def ModuloFunc(self):
        return super().Result(self.num1 % self.num2)
    def FloorDivisionFunc(self):
        return super().Result(self.num1 // self.num2)
    def SquareRoot(self):
        return super().Result(math.sqrt(self.num1))
    def CubeRoot(self):
        if self.num1 < 0:
            return super().Result(pow((abs(self.num1)), 1/3) * (-1))
        else:
            return super().Result(pow(self.num1, 1/3))

# Test
# print(Core4(1, 2).AddFunc())
# print(AdditionalOps(8, 0).CubeRoot())