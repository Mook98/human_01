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