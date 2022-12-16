person1 = {'name': 'Laura',
           'age': '22',
           'country': 'Cuba'}

person2 = {'name': 'Luis',
           'age': '19',
           'country': 'Cuba'}

for items in person1, person2:
    print(items.get('name'), items.get('age'))
