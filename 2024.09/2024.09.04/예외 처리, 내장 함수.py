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