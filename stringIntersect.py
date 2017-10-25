#Greg Phillips
#10/23/17
#stringUnion.py

def stringIntersect(word1, word2):
    total = " "
    for ch in word1:
        if ch in total:
            total += ch
            
    for ch in word2:
        if ch in total:
            total += ch
    
    return total

total = stringUnion("greg", "game")
print(total)
