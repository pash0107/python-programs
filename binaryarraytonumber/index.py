def binary_array_to_number(arr):
    i = 0
    n = len(arr)-1
    num = 0
    while n >= 0:
        num += arr[n]*pow(2, i)
        i += 1
        n -= 1
    return num