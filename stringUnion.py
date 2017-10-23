#Greg Phillips
#10/23/17
#stringUnion.py

def stringUnion(word1, word2):
    total = " "
    for ch in word1:
        if not ch in total:
            total += ch
            
    for ch in word2:
        if not ch in total:
            total += ch
    
    return total

total = stringUnion("book", "goodrich")
print(total)

