# Enter your code here. Read input from STDIN. Print output to STDOUT
import random
seed = int(input())
ln = int(input())
key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
'x','y','z','0','1','2','3','4','5','6','7','8','9']
st =""
random.seed(seed)
for i in range(ln):
    st = st + key[random.randint(0,35)]

print(st)