#Greg Phillips
#10/27/17
#warmup12.py - GCF

def GCF(x,y):
    if x<y:
        for x in range(x,0,-1):
            if x%y==0:
                return x
            elif y%x==0:
                return x
    elif x>y:
        for y in range(y,0,-1):
            if y%x==0:
                return y
            elif x%y==0:
                return y
    else:
        return x
print(GCF(20,50))
    
