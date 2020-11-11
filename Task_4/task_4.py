print("Enter the string : ")
userInputString = input()

listOfWords = userInputString.split(' ')

indexRow = 1
for string in listOfWords:
    print(f"{indexRow}. {string[0:10:1]}")
    indexRow += 1

