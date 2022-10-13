def summation(a):
    S = 0
    for i in range(len(a)):
        if a[i] < 0:
            a[i] = a[i] * (-2)
    maxim = max(a)
    for j in range(len(a)):
        S += a[j]/maxim
    return S

a = [int(x) for x in input().split()]
print(summation(a))
