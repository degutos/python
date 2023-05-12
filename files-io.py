# Files

# set library os to use commands from OS 
import os

# running pwd command with os library
os.system('pwd')

# set variable to open the file
myfile = open('/Users/degutos/git/github-doc/python/myfile.txt')

# set file reading to first line. We need to set first line of file to read it.
myfile.seek(0)

# print the content of the file
print(myfile.read())

# os.system('cat /Users/degutos/git/github-doc/python/myfile.txt')

myfile.seek(0)

# print content as a list where we can iterate through position line
print(myfile.readlines())

# we need to close the file after using it
myfile.close()

with open('/Users/degutos/git/github-doc/python/myfile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('/Users/degutos/git/github-doc/python/myfile.txt','r') as myfile:
    contents = myfile.read()
    print(contents)


%%writefile my_new_file.txt
ONE ON FIRST
TWO on SECOND


