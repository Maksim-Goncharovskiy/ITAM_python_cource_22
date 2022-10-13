def summation(a, b):
    start = min(a, b)
    end = max(a, b)
    S = 0 #Сумма
    for i in range(start, end + 1):
        S += i
    return S
print(summation(int(input()), int(input())))
