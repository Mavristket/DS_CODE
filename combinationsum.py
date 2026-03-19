def comb(arr, target, i, current):
    if target == 0:
        print(current)
        return
    
    if target < 0 or i == len(arr):
        return
    
    # take
    comb(arr, target - arr[i], i, current + [arr[i]])
    
    # skip
    comb(arr, target, i+1, current)

comb([2,3], 4, 0, [])