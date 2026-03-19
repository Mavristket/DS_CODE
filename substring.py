def subset(s, current, i):
    if i == len(s):
        print(current)
        return
    
    # take
    subset(s, current + s[i], i+1)
    
    # skip
    subset(s, current, i+1)

subset("abc", "", 0)