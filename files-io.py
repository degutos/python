# Files

# set library os to use commands from OS 
import os

# running pwd command with os library
os.system('pwd')

# set variable to open the file
#myfile = open('/Users/degutos/git/github-doc/python/myfile.txt')
myfile = open('/Users/andregonzaga/git/dev/python/myfile.txt')

# set file reading to first line. We need to set first line of file to read it.
myfile.seek(0)

# print the content of the file
print(myfile.read())

# os.system('cat /Users/andregonzaga/git/dev/python/myfile.txt')

myfile.seek(0)

# print content as a list where we can iterate through position line
print(myfile.readlines())

# we need to close the file after using it
myfile.close()

# Simple example how to open a file and edit it and close it
f = open('test.txt', mode='w')
f.write('Hello World')
f.close()


# Example on how we use a file without a need to close it, using "with" method
with open('/Users/andregonzaga/git/dev/python/myfile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('/Users/andregonzaga/git/dev/python/myfile.txt','r') as myfile:
    contents = myfile.read()
    print(contents)

#f = open('/Users/andregonzaga/git/dev/python/my-new-file.txt',mode='x')
#f.close()

with open('/Users/andregonzaga/git/dev/python/my-new-file.txt',mode='w') as f:
    f.write('Now the file has a content')
    print(f)


