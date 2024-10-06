def palind(str):
    str1 = list(str)
    x = 1
    y = 1
    c = 0
    while x < int(len(str1) / 1.5):
        if str1[x - 1] == str1[-x]:
            c += 1
        else:
            c -= 1
        x += 1
    if c == int(len(str1) / 2):
        return True
    else:
        return False
    
print(palind('level'))
print(palind('levew'))