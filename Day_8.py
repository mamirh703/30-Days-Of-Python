#Day 8: 30 Days Of Python
dog = {}
dog['Name'] = 'Peanut'
dog['Color'] = 'Golden'
dog['Breed'] = 'Golden Retriever'
dog['Legs'] = '4'
dog['Age'] = '3'
print(dog)

student  = {
    'first_name' : 'Alex',
    'last_name' : 'Wolfgang',
    'gender' : 'Male',
    'Age' : '14',
    'Marital Status' : 'False',
    'Skills' : ['Python','HTML'],
    'Country' : 'Canada',
    'City' : 'Toronto',
    'Address' : {
        'Street' : '5th Avenue'
    }
}
print(student)

print(len(student))

print(student['Skills'])
print(type(student['Skills']))

student['Skills'].append('CSS')
student['Skills'].append('JS')
print(student['Skills'])

print(list(student.keys()))

print(list(student.values()))

print(tuple(student.items()))

del student['Address']
print(student)

del student