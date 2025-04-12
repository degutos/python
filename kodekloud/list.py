# Lists


countries = ["USA", "Canada", "India"]
print(countries[0])
print(countries[1])
print(countries[2])

# Lets change a value of index 2
countries[2] = "UK"
print(countries[2])

# Lets get a number of items in our list
n=len(countries)
print(n)

# Lets delete an item in the list
del countries[1]
print(countries)

# Let print reverse
list1=[2,5,3,1]
print(list1[::-1])

# this will print the 4th character in the list
list1=[1,2,3,4,5]
print(list1[4])

# lets change a value of the item in the list and print that new value
numbers = [1,2,3,4,5]
numbers[4] = 6
print(numbers[4])

list1 = [1, 2, 3, 4, 5]
list1[0] = 10
print(list1)

# this will print index 0 and index 3 [10, 13]
list1 = [10, 11, 12, 13, 14]
print(list1[::3])

# Lets now use the methods .append and .insert to add a item to the end of the list and to insert a new item in the middle of the list. It wil print ['USA', 'Canada', 'Italy', 'India', 'Spain']
countries = ["USA", "Canada", "India"]
countries.append("Spain") # use .append to add a new item to the end of the list
countries.insert(2, "Italy") # use .insert to insert a index in the middle of the list, in this case we added a index 2.
print(countries)

# Lets swap the value of item in the list, USA and Canada - we use a variable temp to store the value
countries = ["USA", "Canada", "India"]
temp = countries[0]
countries[0] = countries[1]
countries[1] = temp
print(countries)

# A easier way to swap values
countries[0], countries[1] = countries[1], countries[0]
print(countries)

# Lets use the method .sort
ages = [56, 72, 24, 46, 13, 5]
ages.sort()
print(ages)

# Lets reverse now
ages = [56, 72, 24, 46, 13, 5]
ages.reverse()
print(ages)

# the method .pop(2) will pop up (remove) the item 2 from the list
list1 = [4, 4, 3, 1]
list1.pop(2)
print(list1)

list1=['UK','India','Canada']
list1.insert(1,8)
print(list1)

# Lets use method .sort again 
num = [4, 4, 3, 1]
num.sort()
print(num)

# Lets use .sort and sort this again
ages = [56, 72, 24, 46]
ages.sort()
print(ages)

# The max() method will print the max value in this case the Java word
list1=["Go","Java","C","Aython"]
print(max(list1))

list1 = [10, 20, 30, 40, 50]
list1.append(60)
print(list1)

# The min() function will print the min value in the list in this case will print C
list1=["Go","Java","C","Rust"]
print(min(list1))

list1=['h', 'e', 'l', 'l', 'o']
print(len(list1))


# Lets calculate the average of a list of numbers
ages = [56,72, 24, 46]
total = 0
for age in ages:
    total += age
average = total / len(ages)
print(average)

# Lets skip the letter 'e'
for letter in 'kodekloud':
    if letter == 'e':
        continue
    print('Letter : ' + letter)

# Lets print all items in our list
for i in [9, 1, 5, 6]:
    print(i)

# Lets sum each item in our list and print sum
sum = 0 
values = [2,9,1,7]
for number in values:
    sum += number
print(sum)

# Lets print * 16 times
for x in [0, 1, 1, 3]:
    for y in [0, 2, 1, 2]:
        print('*')

# Lets print all items in our list
for i in [1, 1, 7, 0, 6]:
    print(i)

# Lets sum all items in our list
sum = 0
values = [2,9,1,7]
for number in values:
    sum = sum + number

print(sum)

# Lets skip the letter 'u' and print all others
for letter in 'KodeKloud':
    if letter == 'u':
        continue
    print('Letter : ' + letter)

# Lets iterate through a list of lists, when the list has 3 elements we can print out each item from the list
list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
      if len(i)==3:
        print(i)

# Lets add a new item to the last position on our list
list1 = [10, 11, 12, 13, 14]
list1.append(15)
print(list1)

# Lets print the first element [0] in the list
list1 = [10, 11, 12, 13, 14]
print(list1[0])

# Lets print a list in reverse order
list1=[4,0,7,1]
print(list1[::-1])

# Lets print from second item in the list [1] to the end
letters = ["A", "B", "C", "D", "E"]
print(letters[1:])

# Lets print from second item in the list [1] to 3rd item in the list, this will print 2nd and 3rd item in the list 
letters = ["A", "B", "C", "D", "E"]
print(letters[1:3])

# Lets print index and each item in the list
list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
     print(index, j)



list1 = [10, 11, 12, 13, 14]
print(list1[::1])

# Lets iterate through the list of list, check if number of elements in the list is 4, if so we print out each element in the list
list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
      if len(i)==4:
        print(i)


list1 = ["A", "B", "C", "D", "E"]
print(list1[1:3]) # print 2nd and 3rd element in the list
print(list1[:]) # print all elements in the list
print(list1[:-1]) # print from beginning to the end, but not printing the last element
print(list1[1:-1]) # print all elements from the list except the first and last one.
first_two = list1[1:3] # assigning slice list to a new variable, in this case if we change the list we won't change the new variable
print(first_two)
list1.insert(1,3) # lets add a new element to the list in the position [1] 
print(list1) # when we print the elements from the list we see the new element added, which is the number '3'
print(first_two) # here we print variable first_two which was not changed by the time when we added a new element. 


list1 = ["A", "B", "C", "D", "E"]
del list1[0] # lets delete first element in the list. This will affect into the list elements. 
print(list1)

del list1[:]
print(list1) # lets print list1 and notice we have deleted all elements in the list.

# lets print from beginning to the end, printing only 2 and 2
my_list = [0, 1, 2, 3, 4]
print(my_list[::2])


# lets print from beginning to the end showing 3 in 3 
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[::3])

# lets print from end to beginning
my_list = [0, 1, 2, 3, 4]
print(my_list[::-1])

# lets create a list append a element to the list, slice from 2nd element [1] to the end
my_list = [0, 1, 2, 3, 4]
my_list.append("python")
b = my_list[1:]
print(b)

# lets create a list with elements, other list of elements and different type of elements, then we print 3rc element [2] to 4th element
list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[2:4])


# lets print from beginning to the 4th element
list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[0:4])
    
# lets create a list add an element to the end, and print from 3rd element [2] until the end
my_list = [0, 1, 2, 3, 4]
my_list.append("python")
print(my_list[2:])

# lets print last element
my_list = [0, 1, 2, 3, 4]
print(my_list[-1])

# check if a value is in the list of elements
list1 = ["A", "B", "C", "D", "E"]
print("B" in list1)
print("z" in list1)

# lets create a list, assign new variable to a list, change value of a element in the list, you will notice that the new variable has a new value changed
list1=[3,4,6,1,2]
list2=list1
list1[1]=9
print(list2)

# lets replace a few elements in the list
list1 = [0, 3, 4, 1, 2]
list1[2:5]=[8,9]
print(list1)

# lets replace two values
countries = ["USA", "Canada", "India"]
countries[0], countries[1] = countries[1], countries[0]
print(countries)

# lets replace a value element in the list and print new list values
list1=[3,4,6,1,2]
list2=list1
list1[0]=9
print(list2)

# lets print 3rd element (2)
my_list = [0, 1, 2, 3, 4]
print(my_list.index(2))
my_list = [0, 3, 4, 1, 2]
print(my_list.index(1))

# let create a nested list - a matrix list
classroom = [
    ["Sam", "Max", "Joe", "Anne"],
    ["Sofie", "Lisa", "Tim", "Sacha"],
    ["Clare", "Sara", "Leo", "Kim"],
    ["Zoe", "Guy", "Zoe", "Eva"],
]
# lets print out "Sara" name
student = classroom[2][1]
print(student)



# lets create a list of nested list, then create a second list with empty elements, 
matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2])

a = []
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(j)

print(a)




matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[0])



countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
print(countries2)




matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix[2][1])



a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a[3][3])





matrix = [[j for j in range(4)] for i in range(4)] 
print(matrix[3][1])



a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a[2][3])





countries = [['Egypt', 'USA', 'India'],
       ['Dubai', 'America', 'Spain'], 
       ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in 
                       sublist if len(country) < 6]
print(countries2)




# lets create a 3D matrix list


school = [
    [  # Block 1
        ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona"],
        ["George", "Hannah", "Ian", "Jack", "Kara", "Liam"],
        ["Mona", "Nate", "Olivia", "Paul", "Quinn", "Rachel"],
        ["Sam", "Tina", "Uma", "Victor", "Wendy", "Xander"]
    ],
    [  # Block 2
        ["Yara", "Zane", "Aiden", "Bella", "Caleb", "Dana"],
        ["Eli", "Faith", "Gavin", "Hailey", "Isaac", "Jenna"],
        ["Kevin", "Lila", "Miles", "Nora", "Omar", "Piper"],
        ["Quincy", "Riley", "Sasha", "Tyler", "Ursula", "Vince"]
    ],
    [  # Block 3
        ["Will", "Xena", "Yosef", "Zara", "Abby", "Ben"],
        ["Cara", "Derek", "Elsa", "Finn", "Gia", "Harry"],
        ["Ivy", "Jake", "Kayla", "Leo", "Maya", "Noah"],
        ["Owen", "Paige", "Quinn", "Rose", "Sean", "Tara"]
    ],
    [  # Block 4
        ["Uma", "Vera", "Walt", "Ximena", "Yuri", "Zeke"],
        ["Amber", "Blake", "Cleo", "Dean", "Ella", "Fred"],
        ["Gina", "Hugo", "Isla", "Jon", "Kate", "Lars"],
        ["Mila", "Nico", "Opal", "Pete", "Queenie", "Ray"]
    ]
]

# lets print "Derek" name
print(school[2][1][1])

