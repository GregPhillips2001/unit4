#Greg Phillips
#10/16/30
#functionDemo.py - learning functions 

def hw():
    print("Hello, world!") #defines what function will do

hw() #actually runs the function

def bigger(num1, num2): #Prints which number is bigger
    if num1 > num2:
        print(num1)
    else:
        print(num2)

def slope(x1, y1, x2, y2):
    print((y2-y1)/(x2-x1))

"""bigger(13, 27) #Test one
bigger(-10,-15)#test2
bigger("Smeds", "Yllino")"""
slope(1,2,3,4) #allows you to jump back up in the code