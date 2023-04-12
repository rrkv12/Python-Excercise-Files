'''Write a function capable of reading two integers from the user.
If both integers are the same, print on the screen
“same”, if they are different print on the
screen the lowest of the two.'''

def lowest_of_two():
    var1=float(input('Please enter first number '))
    var2=float(input('Please enter second number '))
    if var1==var2:
        print('Same')
    else:
        if var1<var2:
            print(var1)
        else:
            print(var2)
    print('THANK YOU!!!')
