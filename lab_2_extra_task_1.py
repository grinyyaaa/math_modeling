a = int(input('введите первый член а квадратного уравнения'))
b = int(input('введите второй член б квадратного уравнения'))
c = int(input('введите третий член ц квадратного уравнения'))
d = b**2 - 4*a*c
if d < 0:
    print('net korney')
else:
     x_1 = (-b + d**0.5)/2*a
     x_2 = (-b - d**0.5)/2*a
     print(x_1)
     print(x_2)
if d == 0:
    x = -b/2*a
    print(x)
    

