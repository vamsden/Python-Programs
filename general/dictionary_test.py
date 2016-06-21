birthdays = {'Luke Skywalker': '5/24/19',
             'Obi-Wan Kenobi': '3/11/57', 'Darth Vader': '4/1/41'}

if 'Yoda' in birthdays:
    print('Yoda present')
else:
    birthdays['Yoda'] = 'unknown'

if 'Darth Vader' in birthdays:
    print('Darth Vader present')
else:
    birthdays['Darth Vader'] = 'unknown'

print()
print(birthdays)
print()

for key in birthdays:
    print(key, birthdays[key])

print()

del(birthdays['Darth Vader'])

print(birthdays)
print()
