word = "Donkey"

with open("example.txt") as f :
    content = f.read()

content = content.replace(word, "######")

with open("example.txt", "w") as f :
    f.write(content)