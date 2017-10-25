#Greg Phillips
#10/23/17
#stringUnion.py

def stringIntersect(word1, word2):
    total = " "
    word1 = word1.lower()
    word2 = word2.lower()
    for ch in word2:
        if ch in word1 and ch not in total:
            total += ch
    return total

total = stringIntersect("pensylvania", "mississippi")
print(total)
