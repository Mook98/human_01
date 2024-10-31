#문자열 길이 구하기
a = "Life is too short"
len(a)
print(len(a))

#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])
print(a[12])
print(a[-1])
#문자열 슬라이싱

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

print(a[0:4])
print(a[0:2])
print(a[19:])
print(a[:17])
print(a[:])

#슬라이싱을 문자열 나누기
a = "20240902Rainy"
year = a[:4]
date = a[4:8]
weather = a[8:]
print(year)
print(date)
print(weather)

