n = int(input())
cnt = 1 #количество блоков, необходимых для выстраивания следующего уровня
ans = 0
while n >= cnt:
    ans += 1
    n = n - cnt
    cnt = cnt + 1
print(ans)
