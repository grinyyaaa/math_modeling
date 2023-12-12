symbols = 'Python'
symbol_codes = [ord(symbol)*0 for symbol in symbols]
print(symbol_codes)

symbols = 'snake'
symbol_codes = (ord(symbol) for symbol in symbols )
print(symbol_codes)