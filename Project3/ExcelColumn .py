colName = input("Enter the excel row name (e.g A, AA, AAA): ")

def alphabetListToNumber(colList):
    colNum = 0
    for i, char in enumerate(reversed(colList)):
        colNum += (ord(char) - ord('A') + 1) * (26 ** i)
    return colNum

if not colName.isalpha():
    print("Invalid input. Please enter a valid excel row name consisting of letters only.")
else:
    colName = colName.upper()
    colList = list(colName)
    print(f"The list of characters in the column name is: {colList}")
    colNumber = alphabetListToNumber(colList)
    print(f"The corresponding column number is: {colNumber}")


