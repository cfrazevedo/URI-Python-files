from datetime import datetime, timedelta
from math import ceil

n = int(input())
di = datetime(2020, 12, 21)
ano_sat = 29.6 * n
ano_jup = 11.9 * n
dia_sat = int(ano_sat * 365)
dia_jup = int(ano_jup * 365)
for c in range(2021, 2022 + ceil(ano_sat)):
    if c % 4 == 0:
        dia_sat += 1
for c in range(2021, 2022 + ceil(ano_jup)):
    if c % 4 == 0:
        dia_jup += 1
afs = (di + timedelta(dia_sat)).year
afj = (di + timedelta(dia_jup)).year
mfs = (di + timedelta(dia_sat)).month
mfj = (di + timedelta(dia_jup)).month
if mfs <= 3 and ((afs % 4 == 0 and afs % 100 != 0) or afs % 400 == 0):
    dia_sat -= 1
if mfj <= 3 and ((afj % 4 == 0 and afj % 100 != 0) or afj % 400 == 0):
    dia_jup -= 1
ds = di + timedelta(dia_sat)
dj = di + timedelta(dia_jup)
print(f'Dias terrestres para Jupiter = {dia_jup}')
print(f'Data terrestre para Jupiter: {dj.date()}')
print(f'Dias terrestres para Saturno = {dia_sat}')
print(f'Data terrestre para Saturno: {ds.date()}')