#Day 10: 30 Days Of Python
#Exercises: Level 1
for i in range(1,11):
    print(i)
i=0
while i < 10:
    i +=1
    print(i)

for i in range(10,0,-1):
    print(i)
i=10
while i > 0:
    print(i)
    i -= 1

for i in range(1,8):
    print("#"*i)

#Question 4

for i in range(11):
    ans = i*i
    print(f"{i} x {i} = {ans}")

lan = ['Python','Numpy','Django','Flask']
for la in lan:
    print(la)

for i in range(0,101,2):
    print(i)

for i in range(1,100,2):
    print(i)

#Exercises: Level 2
for i in range(1,101):
    ans += i
    if i == 100:
        print(f"The sum of all numbers is {ans}")
    else: continue

even = 0
odd = 0
for i in range(1,101):
    if i % 2 == 0:
        even += i
    else: 
        odd += i
print(f"The sum of all evens is {even}")
print(f"The sum of all odds is {odd}")

#Exersices: Level 3
lst = []
from countries import countries
for i in countries:
    if 'land' in i:
        lst.append(i)
    else: None
print(lst)

fruit = ['banana', 'orange', 'mango', 'lemon']
for i in fruit:
    for j in range(3,0,-1):
        i[j]
print(fruit)

languages = set()
from countries_data import countries_data
for data in countries_data:
    lan = data['languages']
    lan = str(lan)
    l = lan.split()
    lan = set(l)
    languages = languages.union(lan)
print(len(languages))

#Question 3ii

population = []
for data in countries_data:
    pop = data['population']
    population.append(pop)
population.sort(reverse=True)
print(population[:10])