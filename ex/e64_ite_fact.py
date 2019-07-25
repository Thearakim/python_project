def ite_fact(index):
    total = 1
    if index >= 0:
        for i in range(1, index+1):
            total *= i
        return total
    else:
        return 0


# print(ite_fact(0))


