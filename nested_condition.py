'''Nested condition example'''

def nested_condition():
    var=float(input('Please enter your number '))
    if var==0:
        print('Your number is Zero.')
    else:
        if var>0:
            print('Your number is positive')
        else:
            print('Your number is negative')
    print('THANK YOU!!!')
