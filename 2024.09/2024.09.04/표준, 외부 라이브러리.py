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

#외부 라이브러리
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