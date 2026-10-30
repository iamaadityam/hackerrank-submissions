# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = input()
k = int(input())
lst = list(map(int, lst.split()))
def lins(lst, k):
    for i in range(n):
        if k == lst[i]:
            print(i)
            return True
    print("-1")
    return False
lins(lst, k)
​