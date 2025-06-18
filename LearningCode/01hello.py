print("Hello, World! I am aniket kumar")

text = "43"
print(text.zfill(5)) # Output: 00043
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

name = "Aniket Kumar"
print(f"Hello Mr, {name}")
print("Hello Mr,",name) # Without f-string
print("Hello Mr, " + name) # Without f-string