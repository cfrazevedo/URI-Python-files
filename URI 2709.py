def primo(num):
    if num <= 1:
        return False
    for d in range(2, num):
        if num % d == 0:
            return False
    return True

while True:
    try:
        m = int(input())
        v = [int(input()) for _ in range(m)]
        n = int(input()) * -1
        s = p = 0
        for c in range(len(v) - 1, -1, n):
            s += v[c]
        if primo(s):
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except EOFError:
        break