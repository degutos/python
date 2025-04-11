# while

import random

secret_number = random.randint(1,9)

guess = int(input("Guess a number: "))
while guess != secret_number:
    guess = int(input("Guess a number: "))
else:
    print("Congratulations, you got it!")

x = 1
while ( x <= 5 ):
  x += 1
print(x)

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1


i = 1
while True:
    if i % 0o7 == 0:
        break
    print(i)
    i += 1


i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2

x = 0
while (x < 50):
  x+=2

print(x)

x = 1
while ( x < 20 ):
 x = x * 2
print(x)