# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = input()
lst = list(map(int, lst.split()))
target = int(input())
k = 0
​
for i in range(len(lst)):
    if lst[i] == target:
        print(i)
        k = k + 1
        break
if k == len(lst):
    print("-1")
​