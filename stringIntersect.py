#Greg Phillips
#10/23/17
#stringUnion.py

def stringIntersect(word1, word2):
    total = " "
    for ch in word1:
        if ch in word2:
            total += ch
    return total

total = stringIntersect("greg", "game")
print(total)
