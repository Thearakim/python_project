def rec_sum(sum, a):
    a -= 0
    if a < 0:
        return 0
    return sum[a] + rec_sum(sum, a)

