#Day 2: 30 Days of python programming
first_name = "Amir"
last_name = "Hazeem"
full_name = "Amir Hazeem"
country = "Malaysia"
city = "Tanjung Malim"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
print(len(last_name))
print(len(first_name)-len(last_name))
num_one = 5
num_two = 4
total = num_one+num_two
print(total)
diff = num_one-num_two
print(diff)
multiply = num_one*num_two
print(multiply)
divide = num_one/num_two
print(divide)
remainder = num_two%num_one
print(remainder)
exp = num_one**num_two
print(exp)
floor_division = num_one//num_two
print(floor_division)
rad = 30
pi = 3.141
area_of_circle = pi*(rad**2)
print(area_of_circle)
circum_of_circle = 2*pi*rad
print(circum_of_circle)
rad=int(input("Enter the radius of the circle: "))
area = pi*(rad**2)
print(area)
first_name=input("Enter your first name: ")
last_name=input("Enter you last name: ")
country=input("Enter you country: ")
age=input("Enter you age: ")
print(f"Full name: {first_name+""+last_name}")
print(f"Country: {country}")
print(f"Age: {age}")