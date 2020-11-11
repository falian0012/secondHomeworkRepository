print('Enter the month number')
month = int(input())

monthsList = [{"number": 1, "season": 'Winter'},
              {"number": 2, "season": 'Winter'},
              {"number": 3, "season": 'Spring'},
              {"number": 4, "season": 'Spring'},
              {"number": 5, "season": 'Spring'},
              {"number": 6, "season": 'Summer'},
              {"number": 7, "season": 'Summer'},
              {"number": 8, "season": 'Summer'},
              {"number": 9, "season": 'Autumn'},
              {"number": 10, "season": 'Autumn'},
              {"number": 11, "season": 'Autumn'},
              {"number": 12, "season": 'Winter'}]

print(monthsList[month]["season"])