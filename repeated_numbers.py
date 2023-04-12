#Write a function that reads 3 numbers from the user and print the number repeats most times.

def repeat_num():
    a=int(input('Enter a number '))
    b=int(input('Enter a number '))
    c=int(input('Enter a number '))
    if a==b or a==c:
        print('The most repeating number is ' +str(a))
    elif b==c:
        print('The most repeating number is ' +str(b))
    else:
        print('No repeated numbers')
            
