# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = input()
lst = list(map(int, lst.split()))
s = 0
for i in range(len(lst)):
    for j in range(1, len(lst)):
        if lst[j-1]>lst[j]:
            lst[j-1], lst[j] = lst[j], lst[j-1]
            s = s + 1
print(*lst)
print(s)
​