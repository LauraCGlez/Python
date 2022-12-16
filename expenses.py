from traceback import format_tb


#expenses = [10.50, 5.15, 20.5, 3]

#sum = 0

#for expense in expenses:
#    sum = sum + expense

#print('You spent $', sum, ' on luch this week', sep= '')

#range(7)

#range(0, 7, 1)

#range(2, 14, 2)

#for i in range(7):
#    print(i)


#total2 = 0

#expenses2 = []

#for i in range(7):
#    expenses2.append(float(input("Enter an expense:\n")))

#total2 = sum(expenses2)

#print("you spent $", total2, sep = '')

#another way

#expenses1 = [10.50, 5.15, 20, 5, 3]

#total = sum(expenses1)

#print('You spent $', total, ' on luch this week', sep= '')

total3 = 0

expenses3 = []

num_expenses = int(input("Enter # de expenses:\n"))

for i in range(num_expenses):
    expenses3.append(float(input("Enter an expense\n")))

total3 = sum(expenses3)

print(total3)