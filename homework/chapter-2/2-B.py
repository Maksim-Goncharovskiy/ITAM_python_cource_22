def key_difference(dict1, dict2):
    ans = {}
    for i in dict1.keys():
        if (i in dict2.keys()):
            if (dict1[i] == dict2[i]):
                ans[i] = "equal"
            else:
                ans[i] = "changed"
        else:
            ans[i] = "deleted"
    for j in dict2.keys():
        if not(j in dict1.keys()):
            ans[j] = "added"
    return ans

# Формат входных данных:
# Две строки. На первой строке элементы первого словаря, на второй - второго.
# В каждой строке ключ и значение указываются через пробел. Элементы разделяются запятой и пробелом.
# Пример: 1 2, 3 4, 5 6
a = [x.split() for x in input().split(', ')]
dict1 = {x[0]:x[1] for x in a}
a = [x.split() for x in input().split(', ')]
dict2 = {x[0]:x[1] for x in a}
print(key_difference(dict1, dict2))
