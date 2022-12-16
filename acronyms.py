acronyms = ['LOL', 'IDK', 'SMH', 'TBH', 'BFN']
acronyms.remove(acronyms[1])
acronyms.append('BFF')
print(acronyms)
word = 'IDK'

if 'BFF' in acronyms:
    print('True')
else:
    print('FALSE')

if word in acronyms:
    print('true')
else:
    print('false')

for acronym in acronyms:
    print(acronym)