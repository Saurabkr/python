a = 1011
b = 1011

print(f'{a} is greater') if a>b else print(f'{b} is greater')

print(f'{a} is greater') if a>b else print(f'{b} is greater') if b>a else print(f'{a}={b}')