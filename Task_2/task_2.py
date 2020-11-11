print("How many numbers you want to enter? ")
countOfNumber = int(input())

userList = []
newList = []

while countOfNumber > 0:
    print(f"Enter the number, remains to enter: {countOfNumber}")
    tempValue = int(input())
    userList.append(tempValue)
    countOfNumber -= 1

print(f'Start List is : {userList} ')

startValue = 0
while startValue < len(userList) // 2:
    newList.append(userList[startValue * 2 + 1])
    newList.append(userList[startValue * 2])
    startValue += 1

if len(userList) % 2 != 0:
    newList.append(userList[-1])

print(f'Summary List is : {newList}')

