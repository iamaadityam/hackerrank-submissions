# Enter your code here. Read input from STDIN. Print output to STDOUT
menu = {'chai': 10, 'samosa': 15, 'maggi': 30, 'poha':20}
qu = input()
if qu in menu:
    print(menu[qu])
else:
    print("Not available")