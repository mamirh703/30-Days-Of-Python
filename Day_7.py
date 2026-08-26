#Day 7: 30 Days Of Python
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise 1
print(len(it_companies))

it_companies.add('Twitter')

it_companies.update(['X','Instagram'])

it_companies.remove('Amazon')
print(it_companies)

#I think remove and discard is the same

#Exercise 2
print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A, B

#Exercise 3
age = set(age)
print(len(age))
age = list(age)
print(len(age))

#String is a text
#List is a collection of different data type which is ordered and changeable
#Tuple is a collection of different data type which is ordered and unchangeable
#Set is a collection of items

sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
unique_words = set(words)
print(unique_words)
print(len(unique_words))