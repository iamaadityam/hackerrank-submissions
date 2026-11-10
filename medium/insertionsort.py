n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.append(x)

i = n - 1

while i >= 0 and lst[i] > x:
    lst[i+1] = lst[i]
    i -= 1

lst[i+1] = x

print(*lst)
