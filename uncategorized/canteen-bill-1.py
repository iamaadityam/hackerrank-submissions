# Enter your code here. Read input from STDIN. Print output to STDOUT
menu = {'chai':10, 'samosa':15, 'maggi':30, 'poha':20, 'juice': 25}
n = int(input())
order = []
amt = 0
rej = 0
for i in range(0,n):
    a,b = input().split()
    if a in menu:
        amt = amt + (int(b)*(menu[a]))
    else:
        rej = rej+ 1
print(amt, rej)
​