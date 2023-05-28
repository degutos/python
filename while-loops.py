# While loop


# while boolean_condition:
#   do something
#  else:
#   do something_else


x = 0
while x < 5:
    print(f'The current value of X is {x}')
    x = x + 1
  #  x += 1 # This is another way of doing the same above
else:
    print('X is not less than 5s')


# We can use break, continue and pass within a IF
# break -> break/stop the code
# continue -> go back to closest loop
# pass -> does nothing at all, used to avoid error within a if when no instructions given 

mystring = 'Sammy'

for letter in mystring:
    pass # without pass here the code would error
print('End of programm')


for letter in mystring:
    if letter == 'm':
        continue # this will go back to loop for above, it won't execute next line
    print(letter)


mystring = 'Sammy'
for letter in mystring:
    if letter == 'm':
        break
    print(letter)

