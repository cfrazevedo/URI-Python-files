d = int(input())
a = d // 365
d -= a * 365
m = d // 30
d -= m * 30
print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{d} dia(s)')