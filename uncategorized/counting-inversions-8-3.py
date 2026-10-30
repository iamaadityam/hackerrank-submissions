# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = input()
lst = list(map(int, lst.split()))
def msort(lst):
    if len(lst) <= 1:
        return lst, 0
        
    m = len(lst) // 2
    left, inv_left = msort(lst[:m])
    right, inv_right = msort(lst[m:])
    final = []
    i = 0
    j = 0
    inv = inv_left + inv_right
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
            inv += len(left) - i
    final.extend(left[i:])
    final.extend(right[j:])
    return final, inv
    
sorted_arr, k = msort(lst)
print(k)
​