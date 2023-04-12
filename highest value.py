

# Write a function that reads 10 integers from the user, and then prints on the screen the highest of these.

def high_value():
    high = int(input('Enter a number: '))
    for i in range(9):
        var=int(input('Enter a number: '))
        if var>high:
            high = var
    print('The hisghest among given numbers is ' + str(high))
    
