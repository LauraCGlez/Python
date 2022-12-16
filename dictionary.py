#Empty dictionary
from imghdr import what

acronyms = {} 

#Adding new dictionary items
acronyms['LOL'] = 'laugh out loud'
acronyms['IDK'] = 'I dont know'
acronyms['TBH'] = 'to be honest'

#acronyms = { 'LOL': 'laugh out loud', 'IDK': 'I dont know', 'TBH': 'to be honest'}

#Random order
print(acronyms)

#Delete an item from dictionary
del acronyms['TBH']
print(acronyms)

#Adding item
acronyms['TBH'] = 'to be honest'

#Get a word in the dictionary
definicion = acronyms.get('LOL')

if definicion:
    print(definicion)
else:
    print("Key doesnt exist")

sentence = 'IDK' + ' what happend ' + 'TBH'

translation = str(acronyms.get('IDK')) + ' what happend ' + str(acronyms.get('TBH'))

print('sentence:', sentence, sep=' ')
print('translation:', translation, sep=' ')
