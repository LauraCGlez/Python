 #Dictionary contact for a class

contacts = {
     'number': 3,
     'students':
     [
         {'name':'Laura', 'email':'laura@example.com', 'age': 22},
         {'name':'Luis', 'email':'luis@example.com', 'age': 19},
         {'name':'Ramos', 'email':'ramos@example.com', 'age': 24}
     ]
}

#Printing the 'email' key
for student in contacts['students']:
    print(student['email'])