#모듈 만들기(mod1.py파일로 저장)
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

#mod1.py 모듈 불러오기
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

#모듈이름 붙이지 않고 해당 모듈의 함수 사용 방법
from mod1 import add
add(3, 4)

from mod1 import add, sub
from mod1 import *

#클래스나 변수 등을 포함한 모듈
#mod2.py로 저장
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a + b

#mod2.py 모듈 실행
import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))

#다른 파일에서 모듈 불러오기
import sys
sys.path
sys.path.append("C:/Work")
sys.path

#다른 디렉토리에서 python 접속 후 모듈 실행
import mod2

#패키지 만들기
#다음과 같은 디렉토리에 .py파일 생성
#C:/Work/game/__init__.py
#C:/Work/game/sound/__init__.py
#C:/Work/game/sound/echo.py
#C:/Work/game/graphic/__init__.py
#C:/Work/game/grapgic/render.py

#echo.py 내용
def echo_test():
    print("echo")

#render.py 내용
def render_test():
    print("render")

#PYTONPATH 환경 변수 추가(CMD에서 실행)
#set PYTHONPATH=C:/Work/game

#echo 모듈 import하여 실행
import game.sound.echo
game.sound.echo.echo_test()

#from ... import로 echo 모듈 실행
#exit() #오류 발생할 수 있기 때문에 인터프리터 종료 후 다시 실행
#python
from game.sound import echo
echo.echo_test()

#echo 모듈 echo_test 함수 직접 import
from game.sound.echo import echo_test
echo_test()

#패키지 변수 및 함수 정의
#C:/Work/game/__init__.py 파일에 공동 변수나 함수 정의
VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

#실행
import game
print(game.VERSION)
game.print_version_info()

#C:/Work/game/__init__.py 파일에 다른 모듈 import 하여 사용
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

#실행
import game
game.render_test()

#패키지 초기화
#C:/Work/game/__init__.py 파일에 처음 불러올 때 실행되어야 하는 코드 작성
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

print("Initializing game")

#실행
import game
#하위 모듈 함수 불러올 때도 실행된다
from game.graphic.render import render_test

#__all__
#모듈을 *를 사용하여 import 할 때에는 init파일에 all 변수 설정
#C:/Work/game/sound/__init__.py 파일에 작성
__all__ = ['echo']

#실행
from game.sound import *
echo.echo_test()

#relative 패키지
#render 모듈에서 echo 모듈 사용하기(relative 이용)
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

#실행
from game.sound.echo import echo_test
render_test()

#예외처리
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

#try-finally문
try:
    f = open('foo.txt', 'w')
    #

finally:
    f.close() #중간에 오류가 있더라도 무조건 실행

#여러 개의 오류 처리
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다")

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

#괄호로 묶어서 처리할 수 도 있음
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

#try-else 문
try:
    age = int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

#오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:  #파일이 없더라도 오류가 발생하지 않고 통과
    pass

#오류 일부러 발생
class Bird:
    def fly(self):
        raise NotImplementedError

#NotImplementedError 발생
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

#NotImplementedError 발생X
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

#예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

#MyError 발생 예외
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

#오류 메시지 출력X
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

#__str__ 메서드 구현 후 다시 실행하면 오류 메시지O
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

#내장함수
#abs 절댓값 리턴
abs(3)
abs(-3)
abs(-1.2)

#all 반복가능한 데이터 x를 입력값으로 받으며 
#x의 요소가 모두 참이면 True, 하나라도 거짓이면 Fasle
all([1, 2 ,3])
all([1, 2, 3, 0])
all([])

#any 반복가능한 데이터 x를 입력값으로 받으며 
#x의 요소가 하나라도 참이면 True, 모두 거짓이면 Fasle
any([1, 2, 3, 0])
any([0, ""])
any([])

#chr 유니코드 숫자 값 입력받아 해당하는 문자 리턴
chr(97)
chr(44032)

#dir 객체가 지닌 변수나 함수를 보여주는 함수
dir([1, 2, 3])
dir({'1':'a'})

#divmod 2개 숫자 입력 받고 a를 b로 나눈 몫과 나머지를 튜플로 리턴
divmod(7, 3)
7 // 3
7 % 3

#enumerate 순서대로 번호
for i, name in enumerate(['baby', 'foo', 'bar']):
    print(i, name)

#eval 
eval('1+2')
eval("'hi' + 'a'")
eval('divmod(4, 3)')

#fitter
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))

#hex
hex(234)
hex(3)

#id
a = 3
id(3)
id(a)
b = a
id(b)
id(4)

#input
a = input()
#hi 입력
a
b = input("Enter: ")
b

#int
int('3')
int(3.4)
int('11', 2)
int('1A', 16)

#isinstance
class Person: pass
a = Person()
isinstance(a, Person)

b = 3
isinstance(b, Person)

#len
len("python")
len([1, 2, 3])
len((1, 'a'))

#list
list("python")
list((1, 2, 3))
a = [1, 2, 3]
b = list(a)
b

#map 사용X
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

#map 사용
def two_times(x):
    return x * 2

list(map(two_times, [1, 2, 3, 4]))

list(map(lambda a: a * 2, [1, 2, 3, 4]))

#max
max([1, 2, 3])
max("python")

#min
min(1, 2, 3)
min("python")

#oct
oct(34)
oct(12345)

#ord
ord('a')
ord('가')

#pow
pow(2, 4)
pow(3, 3)

#range
list(range(5))
list(range(5, 10))
list(range(1, 10, 2))
list(range(0, -10, -1))

#round
round(4.6)
round(4.2)
round(5.678, 2)

#sorted
sorted([3, 1, 2])
sorted(['a', 'c', 'b'])
sorted("zero")
sorted((3, 2, 1))

#str
str(3)
str('hi')

#sum
sum([1, 2, 3])
sum([4, 5, 6])

#tuple
tuple("abc")
tuple([1, 2, 3])
tuple((1, 2, 3))

#type
type("abc")
type([])
type(open("test", 'w'))

#zip
list(zip([1, 2, 3], [4, 5, 6]))
list(zip([1, 2, 3], [4, 5, 6],[7, 8, 9]))
list(zip("abc", "def"))

#datetime.date
import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

diff = day2 - day1
diff.days

day = datetime.date(2021, 12, 14)
day.weekday()

day.isoweekday()

#time
import time
time.time()

time.localtime(time.time())

time.asctime(time.localtime(time.time()))

time.ctime()

time.strftime('%x', time.localtime(time.time()))
time.strftime('%c', time.localtime(time.time()))

for i in range(10):
    print(i)
    time.sleep(1)

#math.gcd
import math
math.gcd(60, 100, 80)
60/20, 100/20, 80/20

#math.lcm
import math
math.lcm(15,25)

#random
import random
random.random()

random.randint(1, 10)
random.randint(1, 55)

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

def random_pop(data):
    number = random.chice(data)
    data.remove(number)
    return number

data = [1, 2, 3, 4, 5]
random.sample(data, len(data))

#itertolls.zip_longest
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

result = zip(students, snacks)
print(list(result))

#itertools 사용
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue = '새우깡')
print(list(result))

#itertools.permutation
import itertools
list(itertools.permutations(['1', '2', '3'], 2))
for a, b in itertools.permutations(['1', '2', '3'], 2):
    print(a + b)

#itertools.combination
import itertools
it = itertools.combinations(range(1, 46), 6)
for num in it:
    print(num)

len(list(itertools.combinations(range(1, 46), 6)))

#functools.reduce
import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)

#operator.itemgetter
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(1))
print(result)

#
from operator import itemgetter
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)

#attrgetter
from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student("jane", 22, 'A'),
    Student("dave", 32, 'B'),
    Student("sally", 17, 'B'),
]

result = sorted(students, key = attrgetter('age'))

#traceback
def a():
    return 1 / 0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생하였습니다")

main()

#오류 원인 판단
import traceback

def a():
    return 1 / 0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생하였습니다")
        print(traceback.format_exc())

main()

#cmd창에서 pip install Faker
from faker import Faker
fake = Faker()
fake.name()

fake = Faker('ko-KR')
fake.name()

fake.address()

test_data = [(fake.name(), fake.address()) for i in range(30)]
test_data

#cmd창에서 pip install sympy
from fractions import Fraction
import sympy

x = sympy.symbols("x")

x, y =sympy.symbols('x, y')

f = sympy.Eq(x*Fraction('2/5'), 1760)

result = sympy.solve(f)
result

remains = result[0] - 1760
remains

#sympy 정리
from fractions import Fraction
import sympy
x = sympy.symbols("x")

f = sympy.Eq(x*Fraction('2/5'), 1760)

result = sympy.solve(f)

remains = result[0] - 1760

print('남은 돈은 {}원 입니다.'.format(remains))

#sympy 활용
#x**2 = 1과 같은 2차 방정식의 해를 구하기
import sympy
x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
sympy.solve(f)

import sympy
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x + y, 10)
f2 = sympy.Eq(x - y, 4)
sympy.solve([f1, f2])

#구구단 2단
def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result
print(gugu(2))

#1000미만의 자연수에서 3과 5의 배수의 총합
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)

#게시판 페이징
def get_total_page(m, n):
    if m % n == 0:
        return m //n
    else:
        return m //n + 1
print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))
