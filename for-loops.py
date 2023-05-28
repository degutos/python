# For loops


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)




for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')


list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)


mystring = 'Hello World'
for letter in mystring:
    print(letter)


tup = (1,2,3)
for item in tup:
    print(item)



mylist = [(1,2),(3,4),(5,6),(7,8)]
for tup in mylist:
    print(tup)


for (a,b) in mylist:
    print(a)
    print(b)

for (a,b) in mylist:
    print(a)


d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
#    print(key)
#    print(value)
#    print('==============')
    print(f'the key is {key} and the value is {value}')















