#Day 11: 30 Days Of Python
#Exercises: Level 1
def add_two_numbers(num1,num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(2,2))

def area_of_circle(r):
    area = 3.14*r*r
    return area
print(area_of_circle(4))

def add_all_numbers(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(add_all_numbers(2,5,4))

def convert_celcius_to_fahrenheit(c):
    f = (c*9/5)+32
    return f
print(convert_celcius_to_fahrenheit(100))

def check_season(month):
    winter = ['January','February','March']
    spring = ['April','May','June']
    summer = ['July','August','September']
    autumn = ['October','November','December']
    if month in autumn:
        return 'Autumn'
    elif month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'
    elif month in summer:
        return 'Summer'
    else: return 'What month is this?'
print(check_season('December'))

def calculate_slope(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    return m
print(calculate_slope(2,3,4,2))

def solve_quadratic_eqn(a,b,c):
    x1 = (-b + (((b*b) - (4*a*c))**.5))/2*a
    x2 = (-b - (((b*b)-(4*a*c))**.5))/2*a
    return x1,x2
print(solve_quadratic_eqn(1,3,4))

def print_list(list):
    return list
sd = ['d','q','g','t']
print(print_list(sd))

def reverse_list(list):
    list.sort(reverse=True)
    return list
print(reverse_list(['2','3','4']))

def capitalize_list_items(list):
    list = str(list)
    list = list.title()
    return list
print(capitalize_list_items(['koklp','ojon']))

def add_item(list,item):
    list.append(item)
    return list
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
numbers = [2, 3, 7, 9];
print(add_item(food_stuff, 'Meat'))
print(add_item(numbers, 5))

def remove_item(list,item):
    list.remove(item)
    return list
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(food_stuff, 'Mango'))
print(remove_item(numbers, 3))

def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
    return sum
print(sum_of_numbers(10))

def sum_of_odds(num):
    sum = 0
    for i in range(num+1):
        if i % 2 != 0:
            odd = i
            sum = sum + odd
        else:pass
    return sum
print(sum_of_odds(100))

def sum_of_evens(num):
    sum = 0
    for i in range(num+1):
        if i % 2 == 0:
            even = i
            sum = sum + even
        else:pass
    return sum
print(sum_of_evens(100))

#Exercises: Level 2
def evens_and_odds(num):
    even = 0
    odd = 0
    for i in range(num+1):
        if i % 2 == 0:
            even = even + 1
        else: odd = odd + 1
    print("The number of odds is ",odd,"\nThe number of evens is ",even)
evens_and_odds(100)

def factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial*i
    return factorial
print(factorial(4))

def is_empty(list):
    if list == None:
        list = True
    else:list = False
    return list
print(is_empty([]))

cal = ['2','2','2']
def calculate_mean(list):
    sum = 0
    for i in list:
        i = int(i)
        sum = sum + i
    mean = sum/len(list)
    return mean
print(calculate_mean(cal))
def calculate_median(list):
    mid = len(list)/2
    mid = int(mid)
    mid = list[mid]
    return mid
print(calculate_median(cal))
def calculate_mode(list):
    return
def calculate_range(list):
    list.sort()
    min = int(list[0])
    max = int(list[-1])
    range = max - min
    return range
print(calculate_range(cal))
