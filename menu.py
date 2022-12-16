#Diferent dictionary

breakfast = ['Egg Sandwich', 'Bagel', 'Coffee']

lunch = ['BLT', 'PB&J', 'Turkey Sandwich']

dinner = ['Soup', 'Rise', 'Taco', 'Spaghetti']

#Container of containers, all in one

#Dictionary of list

menus = [['Egg Sandwich', 'Bagel', 'Coffee'], ['BLT', 'PB&J', 'Turkey Sandwich'], ['Soup', 'Rise', 'Taco', 'Spaghetti']]

print('Breakfast menu:\t', menus[0])
print('Lunch menu:\t', menus[1])
print('Dinner menu:\t', menus[2])

#Get one item from de distionary, for example 'Taco'

print(menus[2][2])

#List of dictionary, another way

menus1 = { 'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
           'lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
           'dinner': ['Soup', 'Rise', 'Taco', 'Spaghetti'] }

#We obtained the value
for food in menus1:
    print(food)

#We obtained the key and the value with two variables
for food, menus1 in menus1.items():
    print(food, ':', menus1)
