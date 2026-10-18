1
L = int(input(""))
2
n = 1
3
while True:
4
    if 2**n < L:
5
        n = n + 1
6
        continue
7
    if 2**n == L:
8
        print(n)
9
        break
10
    if 2**n > L:
11
        print(n-1)
12
        break
13
​