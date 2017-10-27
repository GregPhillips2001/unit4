#Greg Phillips
#10/27/17
#warmup12.py - GCF

def GCF(x,y):
        for i in range(x,0,-1):
            if y%i==0 and x%i==0:
                return i
print(GCF(7,7))
    
