# Lets see how to format string to print out

my_name = 'Jose'
print("Hello " + my_name)

# Lets use .format method. Method format basically insert a word into
# a place called {}

print('This is a string {}' .format('INSERTED'))

print('The {} {} {}' .format('fox','brown', 'quick'))

# Lets change the order of showing variables 
print('The {2} {1} {0}' .format('fox','brown', 'quick'))

# Lets use variables key words and .format method
print('The {q} {b} {f}' .format(f='fox',b='brown',q='quick'))

result = 100/777
print(result)
print('The result was {r}' .format(r=result))

# Let format the float number with 2 numbers after comma
print('The result was {r:1.2f}' .format(r=result))


# Let use float method to concatenate a string
name = 'Jose'
print(f'Hello, his name is {name}')

name = 'Sam'
age = 3
print(f'{name} is {age} year old.')


