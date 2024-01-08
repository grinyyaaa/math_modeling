фио = 'Загуменный_Григорий_Игоревич'
фио = фио.upper()
a = [ord(hehhe) for hehhe in фио]
print(a)
фио = фио.lower()
b = [ord(hehhe) for hehhe in фио]
print(b)

m = (sum(a))
n = (sum(b))

print(f'sum: {m + n}')