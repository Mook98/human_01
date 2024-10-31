#클래스
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#클래스 구조 만들기
class Fourcal():
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = Fourcal()
type(a)
a.setdata(4, 2)
a.first
a.second

a = Fourcal()
b = Fourcal()

a.setdata(4, 2)
a.first

b.setdata(3, 7)
b.first

#더하기 기능 만들기
class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
        
a = FourCal()
a.setdata(4, 2)
a.add()

#곱하기, 나누기, 빼기
class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
a.add()
a.sub()
a.mul()
a.div()
b.add()
b.sub()
b.mul()
b.div()

#생성자
class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

a = FourCal()
a = FourCal(4, 2)
a.add()

#상속
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
a.add()
a.sub()
a.mul()
a.div()

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
a.pow()

#메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
a.div()

#클래스 변수
class Family:
    lastname = "김"

Family.lastname

a = Family()
b = Family()
a.lastname
b.lastname

Family.lastname = "박"
a.lastname
b.lastname
