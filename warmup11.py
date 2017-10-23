#greg phillips
#10/23/17
#warmup11.py - is number prime

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(isPrime(25))
