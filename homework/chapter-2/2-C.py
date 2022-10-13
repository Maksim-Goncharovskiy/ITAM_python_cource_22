def perevod(value, base):
    s = ''
    A = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while value > 0:
        s = A[value % base] + s
        value = value // base
    return s
a, b = map(int, input().split())
print(perevod(a, b))
