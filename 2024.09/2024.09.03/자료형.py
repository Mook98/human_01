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