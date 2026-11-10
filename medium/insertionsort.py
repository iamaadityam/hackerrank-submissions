n = int(input())
lst = list(map(int, input().split()))
x = int(input())

def insertionsort(lst, x):
    for i in range(len(lst)):
        if x < lst[i]:
            lst.insert(i, x)
            print(*lst)
            return True
        i = i + 1
    lst.append(x)
    print(*lst)
    
insertionsort(lst, x)
