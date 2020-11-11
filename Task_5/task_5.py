standartList = [7, 5, 3, 3, 2]

print('Enter new value, 0 = exit')
tempValue = 1
while tempValue != 0:
    tempValue = int(input())

    boolValue = True
    for item in standartList:
        if tempValue >= item:
            index = standartList.index(item)
            standartList.insert(index, tempValue)
            boolValue = False
            break;

    if boolValue:
        standartList.append(tempValue)

    print(f'You are enter : {tempValue}, summaryList = {standartList}')
