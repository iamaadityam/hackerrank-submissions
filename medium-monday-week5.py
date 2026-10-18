1
N = int(input(""))
2
if N < 2:
3
    print("Not Prime")
4
elif N == 3 or N == 2:
5
    print("Prime")
6
else:
7
    for i in range(2,N) :
8
        if N % i == 0:
9
            print("Not Prime")
10
            break
11
        else:
12
            i = i + 1
13
    if i == N:
14
        print("Prime")
15
​