# Tuples
# Tuples are similar to lists. However they are immutable 

# Creating a variable of type Tuple
t = (1,2,3)

# Creating a variable of type List
mylist = [1,2,3]

# Printing variable type t
print(type(t))

# Printing variable type mylist
print(type(mylist))

# Printing size of t
print(len(t))

# Reasigning a tuple variable 
t = ('one',2)
print(t)
print(len(t))

print(t[0])

print(t[-1])


t = ('a','b', 'a')

print(t.count('a'))
print(t.count('b'))

print(t.index('a'))
print(t.index('b'))