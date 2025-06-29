# File I/O -> In Python file I/O used because, if you run any program it stores in the RAM that is a volatile memory. It means once your program closes, all the data will be lost. But in some cases we need to store some data permanently for further use. So, In that point we use file I/O. Because using files we can store data permanently and read it later for further use.

# File Functions in Python
# 1. open() - Opens a file and returns a file object.
# 2. close() - Closes the file.
# 3. read() - Reads the contents of the file.
# 4. write() - Writes data to the file.
# 5. append() - Appends data to the end of the file.
# 6. readline() - Reads a single line from the file.
# 7. readlines() - Reads all lines from the file and returns a list.
# 8. detach()	Returns the separated raw stream from the buffer
# 9. fileno()	Returns a number that represents the stream, from the operating system's perspective
# 10. flush()	Flushes the internal buffer
# 11. isatty()	Returns whether the file stream is interactive or not
# 12. readable()	Returns whether the file stream can be read or not
# 13. seek()	Change the file position
# 14. seekable()	Returns whether the file allows us to change the file position
# 15. tell()	Returns the current file position
# 16. truncate()	Resizes the file to a specified size
# 17. writable()	Returns whether the file can be written to or not
# 18. writelines()	Writes a list of strings to the file

# File Modes in Python
# 1. 'r' - Read mode (default) - Opens a file for reading.
# 2. 'w' - Write mode - Opens a file for writing (creates a new file or truncates an existing file).
# 3. 'a' - Append mode - Opens a file for appending (creates a new file if it doesn't exist).
# 4. 'b' - Binary mode - Opens a file in binary mode (e.g., for images or non-text files).
# 5. 't' - Text mode (default) - Opens a file in text mode (e.g., for text files).
# 6. '+' - Update mode - Opens a file for both reading and writing.


# How we work with files in Python?
# 1. Open a file
file = open("example.txt", "r")
# 2. Read or write to the file
data = file.read()
# 3. Print the data
print(data)
# 4. Close the file
file.close()