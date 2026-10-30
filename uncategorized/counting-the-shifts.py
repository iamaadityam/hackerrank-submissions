# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = input()
lst = list(map(int, lst.split()))
shifts = 0
​
for i in range(1, n):
    k = lst[i]
    j = i-1
    while lst[j] >k and j >= 0:
        lst[j+1] = lst[j]
        shifts = shifts + 1
        j = j - 1
    lst[j+1] = k
​
print(*lst)
print(shifts)
​