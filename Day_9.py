#Day 9: 30 Days Of Python
#Exercises: Level 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    year = 18 - age
    print(f"You need {year} more years to learn to drive.")

your_age = int(input("Enter your age: "))
my_age = 19
if my_age > your_age:
    year = my_age - your_age
    if year == 1:
        print(f"I am {year} year older than you.")
    else: print(f"I am {year} years older than you.")
elif your_age > my_age:
    year = your_age - my_age
    if year == 1:
        print(f"You are {year} year older than me.")
    else: print(f"You are {year} years older than me.")
else:
    print("We are the same age.")

a = int(input("Enter number one:"))
b = int(input("Enter number two:"))
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else: print("There are the same value")

#Exercises: Level 2
score = int(input("Enter your score: "))
if score > 89:
    print("A")
elif score > 79:
    print("B")
elif score > 69:
    print("C")
elif score > 59:
    print("D")
else: print("F")

month = input("Enter a month: ")
month = month.capitalize()
autumn = ['September','October','November']
winter = ['December','January','February']
spring = ['March','April','May']
summer = ['June','July','August']
if month in autumn:
    print("The season is autumn")
elif month in winter:
    print("The season is winter")
elif month in spring:
    print("The season is spring")
elif month in summer:
    print("The season is summer")
else: print("That is not a month")

fruit = input("Enter a fruit: ")
fruits = ['banana','orange','mango','lemon']
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)

#Exercises: Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if person['skills']:
    skills = list(person['skills'])
    mid = int(len(skills)/2)
    print(skills[mid])
else:
    print("What i do wrong?")

if person['skills']:
    skills = list(person['skills'])
    if 'Python' in skills:
        print(skills)
    else: print("He do not have python skills")

if person['skills']:
    skills = list(person['skills'])
    front_end = ['Javascript','React']
    backend = ['Node','Python','MongoDB']
    fullstack = ['React','Node','MongoDB']
    if front_end == skills:
        print("He is a front end developer")
    elif backend == skills:
        print("He is a backend developer")
    elif fullstack == skills:
        print("He is a fullstack developer")
    else: print("Unknown Title")

if person['is_married'] == True and person['country'] == "Finland":
    print("Asabeneh Yetayeh lives in Finland. He is married")
else:None