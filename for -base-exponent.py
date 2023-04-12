''' Write some Python code that does the below 10 times:
Asks the user for a base and an exponent, and then shows the
result of the base to the power of the exponent.
Now, just a quick update. Instead of repeating this 10 times ask the
user how many times he’d like to repeat beforehand '''

x=int(input('How many times do you want to repeat the below exercise?'))
for i in range(x):
    var=(float(input('Enter base ')))**(float(input('Enter the exponent ')))
    print(var)
                                              
