# Write a function for Fermat theorem check
# Write a function for checking whether the Fermat theorem holds true with a set of values.

def check_fermat(a, b, c, n):
    return a**n+b**n==c**n
def check_numbers():
    # Will go with values 1 to 99 for a, b, c since the range is not mentioned.
    # For n will go with the range 3 to 100
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                for n in range(3,100):
                    if check_fermat(a, b, c, n):
                        print('Fermat was wrong!')
                        print(a)
                        print(b)
                        print(c)
                        print(n)
                        break


#THIS WILL TAKE SOME TIME TO FINISH RUNNING
# if you don't want to way do: ctrl + c
