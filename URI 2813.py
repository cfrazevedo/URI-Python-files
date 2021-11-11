n = int(input())
s = []
c = t = cm = tm = 0
for _ in range(n):
    s.extend(input().split())
for d in range(len(s)):
    if s[d] == 'chuva':
        if d % 2 == 0:
            if c == 0:
                cm += 1
                c += 1
            c -= 1
            t += 1
        else:
            if t == 0:
                tm += 1
                t += 1
            t -= 1
            c += 1
print(cm, tm)