#greg phillips
#10/26/17
#factorial.py



def factorial(n):
    total = n
    while n>=2:
        n-=1
        total = total*n
    return total
print(factorial(5))
        
def factorial(num):
    if num == 1:
        print(num)
    else:
        num *= (num-1)
        factorial(num-1)
factorial(5)