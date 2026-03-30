def count_sum(arr):
    total = 0
    for num in arr:
        total += num  
    return total
arr = [1,2,3,4,5]
print("sum: ",count_sum(arr))