#Greg Phillips
#10/30/17
#quiz4.py

def csia():
    print("Computer Science is Awesome " *5)
csia()

def average(x,y,z):
    return (x+y+z)/3
print(average(1,2,3))

def lastLetter(word):
    end = len(word)
    letter = 0
    for ch in word:
        letter += 1
        if letter == end:
            print(ch) 
lastLetter("Greg")

def same(x,y):
    if x == y:
        return True
    else:
        return False
print(same(2*3,7-1))


    
