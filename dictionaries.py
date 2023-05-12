# Dictionaries
# Unordered mapping for storing objects with a key value pair
# Example: {'key1':'value1,'key2':'value2','key3':'value3'}

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)

print('The value of my key1 is: ' + my_dict['key1'])
print(my_dict['key2'])

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':4.99}
print(prices_lookup)
print(prices_lookup['milk'])
print(prices_lookup['apple'])

new_dict = {'k1':123,'k2':[0,1,2,3],'k3':{'insideKey':100}}
print(new_dict)
print(new_dict['k2'])
print(new_dict['k3'])

print(new_dict['k2'][2])
print(new_dict['k2'][1])

print(new_dict['k3']['insideKey'])

d = {'key1':['a','b','c']}
print(d)

# Printing a letter C inside of a list which is inside of dictionary and showing the letter
# with capital letter using method upper()
print(d['key1'][2].upper())

# How to assign a new key to a existing dictionary 
d['key3'] = 300
print(d)


# How to assign a new value to a key
d['key1'] = 'NEW_VALUE'
print(d)

# How to show all keys within a dictionary
print(d.keys())

# How to show all values within a dictionary
print(d.values())

# how to show all keys and values within a dictionary 
print(d.items())
