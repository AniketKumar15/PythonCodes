# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, mark zuckerberg should be capitalised correctly as Mark Zuckerberg

# Read input
name = input("Enter your full name: ")

# Capitalize first letter of each word
corrected_name = name.title()

# Print the result
print(corrected_name)


name = input("Enter your full name: ")
words = name.split()  # split into ["mark", "zuckerberg"]
capitalized_words = [word.capitalize() for word in words]  # ["Mark", "Zuckerberg"]
corrected_name = " ".join(capitalized_words)
print(corrected_name)