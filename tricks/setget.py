class Person():
    pass

person = Person()

first_key = 'first'
first_value = 'Jake'

# setattr(person, first_key, first_value)

# first = getattr(person, first_key)

# print(first)

person_info = {'first': 'Jake', 'last': 'Peralta'}

for key, value in person_info.items():
    setattr(person, key, value)
    
# print(person.first)
# print(person.last)

for key in person_info.keys():
    print(getattr(person, key))