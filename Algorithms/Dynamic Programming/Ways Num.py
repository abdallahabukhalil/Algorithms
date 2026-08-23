def WaysNum(total, options: list, ways: dict = {0: 1}): 
    if total in ways: return ways[total]

    elif total < 0: return 0

    else:
        ways[total] = 0

        for option in options:
            ways[total] += WaysNum(total - option, options, ways)

        return ways[total]
    
print(WaysNum(4,[1,2]))