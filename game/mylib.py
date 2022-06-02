def sum(num1, num2):
    hap = num1 + num2
    return hap

def info(weight, height, **kwargs):
    print("키 : ", height)
    print("몸무게 : ", weight)
    print("기타 : ", kwargs)
    
COMPANY = "파이썬 주식회사"


class Calculator:
    first = 0
    second = 0

    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

    def setData(self, first=None, second=None):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def div(self):
        return self.first / self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second