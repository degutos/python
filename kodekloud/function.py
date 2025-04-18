# Function


#def input_number():
#    return int(input("Enter a number: "))
#
#input1 = input_number()
#input2 = input_number()
#input_number()
#
#print(input1)
#print(input2)
#print(input3)



a = 0
def add_one(a):
	return a+1

result = add_one(a)
print(result)


def my_function(*students):
  print("The tallest student is " + students[2])

my_function("James", "Ella", "Jackson")

# Lets pass a number 19 as argument, and attribute value 18 to age. When we print age we actually print the value passed as parameter
def print_info(name, age=18):
    print(name, age)

print_info('john', 19)


#
#def input_number(num1, num2):
#     return int(input("Enter a number: ")) * num1 - num2
#
#input1 = input_number(num2=10,num1=20)
#print(input1)

# Lets create a function that has a default value of 10. 
#def input_number(num=10):
     #return int(input("Enter a number: ")) * num
#print(input_number()) # if we pass a value here the python will use the value we passed and not the default value.


# This function will consider the value passed and not the default value in the function.
def print_name_age(name, age=19):
    print(name, age)

print_name_age('john', 18)


# Lets create a function that receives a list of parameters, within the function we change the value of the last element in the list.
# then we print the function values, we will notice that it will print the new value changed. It will print [7,4,5]
nums= [7,4,1]
def change_third_item(list):
	list[2] = 5

change_third_item(nums)
print(nums)

# lets create a function that recieves a parameter type list, then print the first element in the list [0]
def my_function(*friends):
  print("The tallest student is " + friends[0])

my_function("john", "Ella", "mark")


# simple function to sum 2 values 
def add_func(num1,num2):
            	  	return num1 + num2 
		
print ( add_func(5 , 5) )


def fullname_func(fname, lname):
  print(fname + " " + lname)

fullname_func("John", "Mark")

# Lets  attribute a variable a value of 0, then create afunction that receives a as paramenter as variable a and the value passed 
# is 3, when we print out we will print the value passed as parameter 3 and not 0.
a = 0
def add_three(a):
	return a+3

result = add_three(3)
print(result)

# create a function that recieve a name and concatenate with surname
def fullname_func(fname):
  print(fname + " Mark")

fullname_func("John")

#def add_func(num1,num2):
#                   	return num1 + num2
# 
#print ( add_func(5 , num1= 10) ) # this function will return an error because python get lost with parameters passed 

a = 0
def add_three(a):
	return a+3

result = add_three(a)
print(result)


# Lets create a function that return a number multiplied by the same number (square)
def square(i):
    j = i * i
    return j

num = 2
result = square(num)
print("The result of ", num, " is ", result)


# lets create a function that receives a value that we will dived 10 by the number passed.
def my_function(x):
  return 10 / x

print(my_function(2))


# lets create a function that receives (3<6) and return a boolean like true or false, it will return True
def is_true(a): 
  return bool(a) 

result = is_true(3<6) 
print("The result is", result)

# lets create a function now that receives (6<3) and returns boolean true or false
def is_true(a): 
  return bool(a) 

result = is_true(6<3) 
print("The result is", result)


def return_greeting():
  return "Hello, World"

print(return_greeting())



#
def multiply_values(list):
     multiplied_values = []
     for item in list:
          multiplied_values.append(item * 2)
     return multiplied_values
multiplied_values=multiply_values([1,3])
print(multiplied_values)


# lets create a function that receives a list of numbers, sum each element in the list and divide by number of elements 
def mean_func(list1):
    return sum(list1) / len(list1)

print(mean_func([5, 2, 2, 4]))


# lets create function that receives a number and do multiplication and sum
def my_function(numbers):
  for i in numbers:
    print(i*2+10, end=' ')

numbers = [1, 2, 3]
my_function(numbers)


# lets create a function that recieves a list of elements and print only odd numbers
def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers

print(get_odd_func([1, 2, 3, 4, 5, 6]))


# same to print only odd numbers
def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers

print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))




# lets do a function that sum 1 to each element in the list
def my_function(numbers):
  for i in numbers:
    print(i+1, end=' ')

numbers = [1, 2, 3] 
my_function(numbers)

def my_function(names):
  for i in names:
    print(i, end=' ')

names = ["john", "mark", "emmy"]
my_function(names)




def mean_func(list1):
    return sum(list1) / len(list1)

print(mean_func([5, 6, 7, 8]))


# lets create a function that receives a list of numbers, multiple 2 by the entire list, we will notice that in this it will print twice each list and not multiply each element in the list.
def double_list(numbers):
  return 2 * numbers

numbers = [1, 2, 3]
print(double_list(numbers))



# print even numbers
def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers

get_even_func([1, 2, 3, 4, 5, 6])

# lets play with variables within the functions
# variables declared within the function exits only inside the of the function
# we can declare a global variable scope from within the function, if we want to use the variable in the global scope.
num=100
# this function will print 
#def input_number():
##    num = 50
#    result = int(input("Enter a number: ")) * num
#    print(result) # this result will be printed since it exist and print from within the function
#    return result
#
#input_number()
#print(result) # result won't print anything since result exist only within the function.

###################################

# Lets create a function and declare a variable as global from inside of the function.
# when we print outside of the function the variable will print out because it was declared as "global"
x = 30
def my_function():
  global x
  x = 20

my_function()
print(x)


# Lets create another function and also create a global variable.
def my_function():
  global x
  x = 30

my_function()
print(x)



def myfunc():
  a = 20

myfunc()
print(a)


# Lets create a code with variable x =20 from outside of the function
# then create a x=30 within of the function. Then we print both.
x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x, end=' ')



# lets create another code with x=20 outside of the function 
# then create a x=30 from inside of the function.
x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x, end=' ')


# this example we create a function within another function
# when we print x from within the function python doesn't know the 
# variable x then it searches outside of internal function. 
def my_function():
  x = 20
  def my_inner_function():
    print(x)
  my_inner_function()
my_function()


# this example we print 20 because its declared within the function.
def my_function():
  def my_inner_function():
    x = 20
    print(x)
  my_inner_function()

my_function()



# easy way declaring within the function, it values only within the function
def myfunc():
  a = 20
  print(a)

myfunc()



# this function will give an error, when we print x python doesn't down about its value
def my_function():
  def my_inner_function():
    x = 20
  print(x)
  my_inner_function()

my_function()

# this example will print 20 from within the function and 20 from outside of the function.
x = 20
def my_function():
  print(x, end=' ')

my_function()
print(x, end=' ')
