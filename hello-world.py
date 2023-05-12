# Print a simple hello world
print('Hello World')
print('hello \n world')
print('hello \t world')


# Count number of caracters 
count = len('I am')
print(count)

# Print some addiction math
print(2+1+3)
print(0.1+0.2+0.3)



# Variables
a = 5
b = "andre-test"
c = 0.15

print(a+1)
print(a+a)

# type function basically check what type a variable is
print(type(a))
print(type(b))
print(type(c))

# Variables can use double quotes or single quotes
d = "Using double quotes"
e = 'Using single quotes'
f = "I'm using double quotes because I need to use single quotes inside of the string. :)"

# Calculate using variables
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

# String Variables can be sliced and take it partially. 
# This prints from caracter 0 to 3 but not include 3
print(b[0:3])

mystring = 'abcdefghijk'
print(mystring)

# Print from caracter position 2 till the end
print(mystring[2:])

# Print from begining to position 3 (but not include), so 0,1,2
print(mystring[:3])

# Print from position 3 to position 6 (not included position 6)
print(mystring[3:6])

# Print from position 1 to position 3 (not included position 3)
print(mystring[1:3])

# Print from position 3 to 9 (not included 9)
print(mystring[3:9])

# Print from begining to the end jumping the step size of 2
print(mystring[::2])

# Print from to 2 to 7 step size of 2
print(mystring[2:7:2])

# Print all the caracters backword step
print(mystring[::-1])

# Strings are imutabble, we can not change the value or reassign new value. Lets change name Sam to Pam
name = 'Sam'
last_letters = name[1:]
print(last_letters)
print('P' + last_letters)

# Lets concatenate strings 
x = 'Hello World'
x = x + ' it is beautiful outside'
print(x)

#Lets see another example
print('2' + '3')

# Lets print a string multiples time 
letter = 'z' 
print(letter * 10)


# Upper case function
x = 'Hello World'
print(x.upper())

# Lower case function
print(x.lower())

# Split words, let use the split method to create a list with words
print(x.split())

x = 'Hi this is a string'
print(x.split())
print(x.split('i'))


