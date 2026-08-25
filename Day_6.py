tpl = ()

sisters = ('Soy','Almond')
brothers = ('Hazelnut','Peanut')
siblings = sisters + brothers
print(siblings)

print(len(siblings))

lst = list(siblings)
lst.append('Red Bean')
lst.append('Green Bean')
family_members = tuple(lst)
print(family_members)

parents = family_members[4:6]
siblings = family_members[0:4]
print(parents)
print(siblings)

fruits = ('Apple','Orange')
vegetables = ('Spinach','Coriander')
animal_products = ('Milk','Meat')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

mid = len(food_stuff_tp)/2
mid = int(mid)
print(food_stuff_tp[mid])

print(food_stuff_tp[0:3])
print(food_stuff_tp[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)