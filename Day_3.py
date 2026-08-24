#Day 3: 30 Days of python
print("Age:", 19)

print("\nHeight:", 1.67,"m")

print("\nComplex:", 1+2j)

base=int(input("\nEnter base: "))
height=int(input("Enter height: "))
area=0.5*base*height
print(f"The area of the triangle is {area}")

side_a=int(input("\nEnter side a: "))
side_b=int(input("Enter side b: "))
side_c=int(input("Enter side c: "))
perimeter=side_a+side_b+side_c
print(f"The perimeter of the triangle is {perimeter}")

length=int(input("\nEnter length: "))
width=int(input("Enter width: "))
area=length*width
perimeter=2*(length+width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

radius=int(input("\nEnter radius: "))
pi=3.14
area=pi*radius*radius
circumference=2*pi/radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

m=2
y_intercept=-2
x_intercept= -y_intercept/m
print(f"\nSlope is {m}")
print(f"y-intercept is {y_intercept}")
print(f"x-intercept is {x_intercept}")

x1,y1 = 2,2
x2,y2 = 6,10
slope = (y2-y1)/(x2-x1)
distance = (x2-x1)^2 + (y2-y1)^2
print(f"\nThe slope is {slope}")
print(f"The euclidean distance is {distance}")

slope_diff = m - slope

x=int(input("\nEnter x value: "))
y = x^2 + 6^x + 9 
print(y)

print(len("\npython"))
print(len("dragon"))
print(len("python") != len("dragon"))

print("\non" in "python" and "on" in "dragon")

print("\njargon" in "I hope this course is not full of jargon.")

print("\nThere is no 'on' in both python and dragon", "on" in "python" and "on" in "dragon")

py = len("\npython")
float(py)
str(py)
print(py)

num = int(input("\nEnter a number: "))
if num%2 == 0:
    print("Even")
else: print("Odd")

fd = 7//3
n = int(2.7)
print()
print(fd == n)

print("\n10" == 10)
print(int(9.8) == 10)

hours = int(input("\nEnter hours: "))
rate = int(input("Enter rate per hour: "))
earn = hours*rate
print(f"Your weekly earning is {earn}")

years = int(input("\nEnter number of years you have lived: "))
sec = years*365*24*60*60
print(f"You have lived for {sec} seconds.")

print()
for i in range(1,6):
    print(i, 1, i, i*2, i*3) 