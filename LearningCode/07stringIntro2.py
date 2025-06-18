# In python we can decalare string in three ways:
# single quotes, double quotes and triple quotes. But mostly we use single and double quotes. Triple quotes are used for multi-line strings.
text = "Hello Aniket"
text2 = 'Hello World'
text3 = '''Hello World I am Aniket'''

print(text)
print(text2)
print(text3)


#But if we want to use single or double quotes for multi-line strings, then we can do like this: 
text4 = 'Multi-line String '\
        'using single quotes'
text5 = "Multi-line String "\
        "using double quotes"

print(text4)
print(text5)

# Slice string
# In python, we can slice a string using the slice operator [:]. The slice operator takes two arguments: start and end. The start index is inclusive and the end index is exclusive. So, the slice operator will return the characters from start to end-1.

newText = text[0:5]
print(newText)
print(text[-6:-2]) # output: Anik
print(text[:4]) # This [:4] is same as [0:4]
print(text[1:]) # This [1:] is same as [1:len(text)]


print(text[0:5:2]) # step of 2
# This is extended slicing: text[start:stop:step]
# start = 0 → start at index 0 (H)
# stop = 5 → go up to (but not include) index 5
# step = 2 → take every second character


print(text[::-1])  # Output: NOHTYP (reverses the string)