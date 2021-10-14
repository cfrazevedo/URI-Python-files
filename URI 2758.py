import struct

a, b = [float(x) for x in input().split()]
a = struct.unpack('f', struct.pack('f', a))[0]
b = struct.unpack('f', struct.pack('f', b))[0]
a, b = float(a), float(b)
c, d = [float(x) for x in input().split()]
print(f'A = {a:.6f}, B = {b:.6f}')
print(f'C = {c:.6f}, D = {d:.6f}')
print(f'A = {a:.1f}, B = {b:.1f}')
print(f'C = {c:.1f}, D = {d:.1f}')
print(f'A = {a:.2f}, B = {b:.2f}')
print(f'C = {c:.2f}, D = {d:.2f}')
print(f'A = {a:.3f}, B = {b:.3f}')
print(f'C = {c:.3f}, D = {d:.3f}')
print(f'A = {a:.3E}, B = {b:.3E}')
print(f'C = {c:.3E}, D = {d:.3E}')
print(f'A = {a:.0f}, B = {b:.0f}')
print(f'C = {c:.0f}, D = {d:.0f}')