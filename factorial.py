# Write a function to calculate the factorial of apositive integer n given by the user.

def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*n
        n=n-1
    return fact

# Write the above function tusing recursion  
def factorial_recursion(n):
    if n==0:
        return 1
    else:
        fac=n*factorial_recursion(n-1)
        return fac
        
    
    
