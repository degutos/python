# Exercise 00 - Data structures 

# write a brief description of all the following object types 

# Numbers: numbers are objects of two types: integer and float
# String: string is a object of type text where we usually write between quotes ' or " 
# List: List is an object represented like [1,'two',3.1], it is an order object type
# Tuples: tuples are very similar to list although they are immutable, represented by t = (1,2,3,4)
# Dictionary:  dictionary is unorder mapping object to store key value pair, example: d = {'apple': 1.99, 'carriot': 1.55, 'onion':1.88}
#print(d['k1'][2]['k2'][1]['tough'][2][0])

import math

# Lets understand the order of maths here
print(4 * (6+5)) # 44
print(4*6+5) # 29
print(4+6*5) # 34

# Let understand the type of this math bellow
print(type(3+1.5+4))

# Square root, we need to import math 
s = math.sqrt(36)
print(s)

# How to square, 5 exponent 2
square = 5 ** 2
print(square)


# Strings

s = 'hello'
# print out 'e' using indexing

print(s[1])


# Reverse the string using slicing 
print(s[::-1])


# printing letter o in two methods
print(s[-1])
print(s[4])

# Lists
# build this list [0,0,0] two separate ways

l = [0,0,0]


# Dictionary

d = {'simple_key':'hello'}

# grab hello
print(d['simple_key'])


d = {'k1':{'k2':'hello'}}

# grab hello
print(d['k1']['k2'])


# grab hello
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])



# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])











