#Day 4: 30 Days Of Python
thirty = 'Thirty'
days = 'Days'
of = 'Of'
python = 'Python'
space = ' '
result = thirty+space+days+space+of+space+python
print(result)

coding = 'Coding'
For = 'For'
all = 'All'
result = coding+space+For+space+all
print(result)

company = "Coding For All"

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

company = "Coding For All"
print(company[0:6])

print(company.find("Coding"))

company = company.replace("Coding", "Python")
print(company)

challenge = "Python for Everyone"
challenge = challenge.replace("Everyone", "All")
print(challenge)

string = 'Coding For All'
string = string.split(' ')
print(string)

medsos = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
medsos = medsos.split(", ")
print(medsos)

sen = "Coding For All"
print(sen[0])

print(sen[-1])

print(sen[10])

sen = 'Python For Everyone'
print("".join(word[0].upper() for word in sen.split()))

sen = 'Coding For All'
print("".join(word[0].upper() for word in sen.split()))


sub = 'C'
print(sen.index(sub))

sub = 'F'
print(sen.index(sub))


sen = 'Coding For All People'
print(sen.rfind('l'))

sen = 'You cannot end a sentence with because because because is a conjunction'
print(sen.find('because'))

print(sen[31:54])

sen = 'Coding For All'
print(sen.startswith('Coding'))

print(sen.endswith('Coding'))

sen = '   Coding For All     '
print(sen.strip(' '))

sen1 = "30DaysOfPython"
sen2 = "thirty_days_of_python"
print(sen1.isidentifier())
print(sen2.isidentifier())

lib = ['Django','Flask','Bottle','Pyramid','Falcon']
result = '# '.join(lib)
print(result)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius,area))

a = 8
b = 6
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {}".format(a,b,a/b))
print("{} % {} = {}".format(a,b,a%b))
print("{} // {} = {}".format(a,b,a//b))
print("{} ** {} = {}".format(a,b,a**b))