def ite_power(number, power):
    total = 1
    if power == 0:
        return 1
    while power > 1:
        total *= number
        power -=1
    return total


# print(ite_power(10,3))

