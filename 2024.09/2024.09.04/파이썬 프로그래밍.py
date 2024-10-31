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
