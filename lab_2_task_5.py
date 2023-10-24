a = int(input())
b = int(input())
d = a % b
if a % b == 0:
    print('делится')
else:
    print(f'не делится, остаток: {d}' )