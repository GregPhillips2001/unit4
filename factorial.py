#greg phillips
#10/26/17
#factorial.py

def factorial(n):
    total = n
    if n == 0:
        return total
    else:
        total = total*(n-1)
        factorial(n-1)
total = factorial(5)
print(total)
    
