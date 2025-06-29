st = input("Enter the text to write in the file: ")

f = open("example.txt", "w")

if(f.write(st)):
    print("Data written successfully.")
else:
    print("Failed to write data.")

f.close()

# Test the read lines and readline functions
f = open("example1.txt")

data = f.readlines()
print(data, type(data))

f.close()

f = open("example1.txt")
line = f.readline()
while line != "":
    print(line, end="")
    line = f.readline()
f.close()