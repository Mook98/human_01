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