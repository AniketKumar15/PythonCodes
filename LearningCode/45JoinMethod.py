# Join Methods -> The join() method in Python is a string method used to concatenate elements of an iterable (such as a list, tuple, or set) into a single string. It is called on the separator string that will be placed between each element of the iterable. 

# The syntax is: 'separator'.join(iterable)

list_of_strings = ['Hello', 'World', 'Python']
joined_string = ' '.join(list_of_strings)
print(joined_string)  # Output: Hello World Python

# Format print 
s = "{} is a Good Man and he work in the {} company.".format("John", "ABC Corp")
print(s)