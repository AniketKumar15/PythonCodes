# Write a program to read text from the file poem.txt and find out whether it contains the word "Twinkle" or not.

# Open and read the file safely
with open("poem.txt", "r") as f:
    content = f.read().lower()  # Convert to lowercase for case-insensitive search
print(content)
word_to_find = "twinkle".lower()

if word_to_find in content:
    count = content.count(word_to_find)
    print(f"Yes! The word '{word_to_find}' is present in the file and it appears {count} times.")
else:
    print(f"No, the word '{word_to_find}' is not present in the file.")
