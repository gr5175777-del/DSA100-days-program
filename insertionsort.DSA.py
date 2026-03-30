def insert_sorted(arr, x):
    arr.append(0)  # create space
    i = len(arr) - 2

    while i >= 0 and arr[i] > x:
        arr[i + 1] = arr[i]
        i -= 1

    arr[i + 1] = x
    return arr

# Example
arr = [1, 3, 5, 7]
x = 4
print(insert_sorted(arr, x))
