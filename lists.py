# Lists
# An ordered of object types

# Lets create a list of 03 items 
my_list = [1,2,3]
print(my_list)

# List can have different types
my_list = ['STRING',100,23.2]
print(my_list)

# Lets count with len method
print(len(my_list))

# Lets create another list called my_list
my_list = ['one','two','three']
print(my_list[0])
print(my_list[1:])

# Lets create another list and print concatenating my_list and another_list
another_list = ['four','five']
print(my_list + another_list)

# Let create a new list which is a concatanation of my_list and another_list
new_list = my_list + another_list
print(new_list)

# Let change the value of first item in the list, realize that in lists we can change the value of a item
new_list[0] = 'ONE ALL CAPS'
print(new_list)

# Lets append a new item in the list, at the end of the list values
new_list.append('six')
print(new_list)

new_list.append('seven')
print(new_list)

new_list.pop()
print(new_list)

# Lets save the item popped out
popped_item = new_list.pop()
print(popped_item)
print(new_list)

# Lets remove the first item from the list now
new_list.pop(0)
print(new_list)

# Lets order a list
new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]

# Lets sort/order the new list
new_list.sort()
print(new_list)

# Lets sort/order the num list
num_list.sort()
print(num_list)

# Lets reverse the num_list
num_list.reverse()
print(num_list)


