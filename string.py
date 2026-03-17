def subsequences(s):
    result = []

    def solve(index, current):
        # base case
        if index == len(s):
            result.append(current)
            return
        
        # include current character
        solve(index + 1, current + s[index])
        
        # exclude current character
        solve(index + 1, current)

    solve(0, "")
    return result


# Example
print(subsequences("abc"))
