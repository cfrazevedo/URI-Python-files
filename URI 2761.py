import struct

d = input()
a = d[:d.find(' ')]
d = d[d.find(' ') + 1:]
b = d[:d.find(' ')]
b = float(b)
b = struct.unpack('f', struct.pack('f', b))[0]
b = f'{b:10.6f}'.replace(' ', '')
d = d[d.find(' ') + 1:]
c = d[:d.find(' ')]
d = d[d.find(' ') + 1:]
print(f'{a}{b}{c}{d}')
print(f'{a}\t{b}\t{c}\t{d}')
print(f'{a:>10}{b:>10}{c:>10}{d:>10}')
