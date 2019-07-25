
def rec_fct(index):
    if index == 0:
        return 1
    else:
        return index * rec_fct(index-1)


# print(rec_fct(0))

