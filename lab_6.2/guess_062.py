def find():
    g = 5
    low = bottom
    high = top
    while low < high:
        mid = (low + high) // 2
        g = guess(mid)
        if g == 0:
            return mid
        if g == -1:
            low = mid + 1
        else:
            high = mid
    return low