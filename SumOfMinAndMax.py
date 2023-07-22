def sum_of_max_and_min(A):
    if not A:
        return None 

    max_val = float('-inf')
    min_val = float('inf')

    for num in A:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val + min_val

A=list(map(int,input().split()))
print(sum_of_max_and_min(A))
