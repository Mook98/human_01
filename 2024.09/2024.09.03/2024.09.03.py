#문자열 포매팅

a = "I eat %d apple." %3
print(a)

b = "I eat %s apples." %"five"
print(b)

number = 3
c = "I eat %d apples." %number
print(c)

number = 10
day = "three"
d = "ate %d apples. so I was sick for %s days" %(number, day)
print(d)

e = "I have %s apples" %3
print(e)

#포맷 코드와 숫자 사용
a = "%10s" %"hi"
print(a)

b = "%-10sjane." %"hi"
print(b)

c = "%0.4f" %3.42134234
print(c)

d = "%10.4f" %3.42134234
print(d)

#format 함수를 사용한 포매팅
a = "I eat {0} apples." .format(3)
print(a)

b = "I eat {0} apples." .format("five")
print(b)

number = 3
c = "I eat {0} apples." .format(number)
print(c)

number = 10
day = "three"
d = "I ate {0} apples. so I was sick for {1} days" .format(number, day)
print(d)

e = "I ate {number} apples. so I was sick for {day} days." .format(number = 10, day = 3)
print(e)

f = "I ate {0} apples. so I was sick for {day} days." .format(10, day=3)
print(f)

a = "{0:<10}" .format("hi")
b = "{0:>10}" .format("hi")
c = "{0:^10}" .format("hi")
d = "{0:=^10}" .format("hi")
print(a)
print(b)
print(c)
print(d)

y = 3.4213234
e = "{0:0.4f}" .format(y)
print(e)

f = "{0:10.4f}" .format(y)
print(f)

#f문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')

age = 30
print(f'나는 내년이면 {age + 1}살이 된다')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')

#문자열 함수
a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

a = "Life is too short"
print(a.index('t'))
print(a.index('h'))

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

a = "hi"
print(a.upper())

a = "HI"
print(a.lower())

a = " hi "
print(a.lstrip())

a = " hi "
print(a.rstrip())

a = " hi "
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))

#리스트 인덱싱 슬라이싱
odd = [1, 3, 5, 7, 9]
print(odd)

a = []
b = [1, 2, 3]
c = ['Life', "is", "too", "short"]
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(a)
print(b)
print(c)
print(d)
print(e)

a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])

a = [1, 2,3 , ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

a = [1, 2, 3, 4, 5]
print(a[0:2])
a = "12345"
print(a[0:2])

b = a[:2]
c = a[2:]
print(b)
print(c)

#리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a))
print(str(a[2]) + "hi")

#리스트 수정 삭제
a = [1, 2, 3]
a[2] = 4
print(a)

a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a  = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))
print(a.index(1))

a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)

a = [1, 2, 3, 1]
print(a.count(1))

a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6,7]
a.extend(b)
print(a)

#튜플 다루기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
t4 = t2 * 3
print(t1[0])
print(t1[3])
print(t1[1:])
print(t3)
print(t4)
print(len(t1))

#딕셔너리  쌍 추가, 삭제
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)

#딕셔너리 사용 방법
grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

dic = {'name':'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

a = {1:'a', 1:'b'}
print(a)

#딕셔너리 관련 함수
a = dic = {'name':'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))
print(a.values())
print(a.items())
print(a.clear())

a = dic = {'name':'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('nokey', 'foo'))

a = dic = {'name':'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print('name' in a)
print('email' in a)

#집합 자료형 특징
s1 = set([1, 2, 3])
l1 = list(s1) # 리스트로 변환
print(l1)
print(l1[0])

t1 = tuple(s1) #튜플로 변환
print(t1)
print(t1[0])

#교집합, 합집합. 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 & s2)
# print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

#집합 자료형 관련 함수
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

s1 = set([1, 2, 3])
s1.remove(2)
print(s1)

#불 자료형
a = True
b = False

print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)

#불 연산
print(bool('python'))
print(bool(''))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(0))
print(bool(3))

#if 문
money = True
if money:
    print('택시를 타고 가라')
else:
    print("걸어가라")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 2000
card =True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#elif문
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

pocket = ['papaer', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#while문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

#while문
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:
"""
number = 0
while number != 4:
    print(prompt)
    number = int(input())

#while문 빠져나오기
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요"))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다" % (money - 300))
    else:
        print("돈을 다시 돌려 주고 커피를 주지 않습니다")
        print("남은 커피의 양은 %d개입니다" %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#for문
marks = [90, 25 , 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다" %number)
    else:
        print("%d번 학생은 불합격입니다" %number)

#for문, continue문
marks = [90, 25 , 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다" %number)

#range 함수
marks = [90, 25 , 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다."%(number + 1))

#구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print(' ')

#리스트 컴프리헨션 사용
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)

#리스트 컴프리헨션 사용 구구단
result = [x*y for x in range(2, 10)
              for y in range(1, 10)]

print(result)

#파이썬 함수의 구조
def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

#일반적인 함수
def add(a, b):
    result = a + b
    return result
a = add(3, 4)
print(a)

#입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

#리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a + b))

add(3, 4)
a = add(3, 4)
print(a)

#입력값도 리턴값도 없는 함수
def say():
    print('Hi')
say()

#매개변수 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)
result = sub(b=5, a=3)
print(result)

#여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

#
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

#키워드 매개변수
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='foo', age =3)

#함수 리턴값은 하나
def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result)

#두번째 리턴은 실행되지 않음
def add_and_mul(a, b):
    return a+b
    return a*b

result = add_and_mul(2, 3)
print(result)

#매개변수 초깃값 미리 설정
def say_myself(name, age, man = True):
    print("나의 이름은 %s입니다"%name)
    print("나이는 %d살입니다."%age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

#함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

#함수 안에서 함수 밖의 변수를 변경하는 방법
a=1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

#사용자 입출력
a = input() #사용자가 문장을 입력
print(a)

number = input("숫자를 입력하세요: ")
print(number)

#한줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')

#파일 생성
f = open("새파일.txt", 'w')
f.close()

#파일 쓰기모드로 열어 내용 쓰기
f = open("새 파일.txt", 'w')
for i in range(1, 11):
    data =  "%d번째 줄입니다.|n" %i
    f.write(data)
f.close

#sys 모듈 사용
import sys

args = sys.argv[1:]
for i in args:
    print(i)

args = sys.argv[1:]
for i in args:
    print(i.upper(), end = ' ')

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