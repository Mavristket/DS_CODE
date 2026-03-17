def subsets(arr):
    result = []

    def solve(index, current):
        if index == len(arr):
            result.append(current)
            return
        
        # include element
        solve(index + 1, current + [arr[index]])
        
        # exclude element
        solve(index + 1, current)

    solve(0, [])
    return result


# Example
print(subsets([1, 2, 3]))
