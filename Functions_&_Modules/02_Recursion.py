# A function calling itself


'''
 Fibonacci Series : 0 1 1 2 3 5 8 13
 
 Fib(0) = 0
 Fib(1) = 1
 Fib(2) = Fib(0) + Fib(1) 
 Fib(3) = Fib(1) + Fib(2) 
 Fib(n) = Fib(n-2) + Fib(n-1)

'''
def fib(n):
    # Base Case of recursion (Must)
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(5))   # Output: 5



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120





