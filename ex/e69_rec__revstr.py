def rec_revstr(revstr):
    if revstr == "":
        return revstr
    else:
        return rec_revstr(revstr[1:]) + revstr[0]


# print(rec_revstr("hello human"))

