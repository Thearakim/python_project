def rec_power(number, power):
    total = 1
    if power == 0:
        return 1
    else:
        total = number ** power
    return total


# print(rec_power(10, 3))