def prime_nb(index):
    if index > 1:
        for i in range(2, index):
            if(index % i) == 0:
                print(f"{index} is not prime number.")
                break
        else:
            print(f"{index} is prime number.")
    else:
        print(f"{index} is not prime number.")


# print(prime_nb(4))

