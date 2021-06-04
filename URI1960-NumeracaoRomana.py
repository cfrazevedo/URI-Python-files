def intPorStr(num, i, s):
    while num >= i:
        print(s, end='')
        num -= i
    return num

n = int(input())
n = intPorStr(n, 900, 'CM')
n = intPorStr(n, 500, 'D')
n = intPorStr(n, 400, 'CD')
n = intPorStr(n, 100, 'C')
n = intPorStr(n, 90, 'XC')
n = intPorStr(n, 50, 'L')
n = intPorStr(n, 40, 'XL')
n = intPorStr(n, 10, 'X')
n = intPorStr(n, 9, 'IX')
n = intPorStr(n, 5, 'V')
n = intPorStr(n, 4, 'IV')
n = intPorStr(n, 1, 'I')
print()