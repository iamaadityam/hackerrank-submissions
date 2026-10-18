L = int(input(""))
n = 1
while True:
    if 2**n < L:
        n = n + 1
        continue
    if 2**n == L:
        print(n)
        break
    if 2**n > L:
        print(n-1)
        break
​