a = int(input('Введите первый член прогрессии: '))
print(a)
b = int(input('Введите знаминатель прогрессии: '))
print(b)
c = range(0, int(input('Введите количество членов прогрессии: ')), 1)
print(c)
for i in c:
    while i != c:
     print(a**b, end=' ')
     i = (a**b)*i

    

    




