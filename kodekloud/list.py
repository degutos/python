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
