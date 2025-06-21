li = ["Hello", "World", "Aniket", "et"]

def rem(li, word) :

    n = []
    for item in li:
        if not(item == word):
            n.append(item.strip(word))
    return n

res = rem(li, "et")
print(res)
