import numpy as np

name = 'Grigorii Zagumenny'
name_str = "_".join(name)
print('with _ :', name_str)

print('upper reg:', name_str.upper())

name_up = name_str.upper()

print('ASCII:')

for symbol in name_up:
    a = (ord(symbol))
    print(a)

name_up_codes = [ord(symbol) for symbol in name_up]
print(name_up_codes)

name = name.lower()

print('ASCII:')

for symbol in name:
    b = (ord(symbol))
    print(b)

name_codes = [ord(symbol) for symbol in name]
print(name_codes)

a = min(name_up_codes)
b = min(name_codes)
listmin = [a, b]
print('min:', min(listmin))

a = max(name_up_codes)
b = max(name_codes)
listmax = [a, b]
print('max:', max(listmax))



