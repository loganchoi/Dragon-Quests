import random as rand

num1 = rand.randrange(-10,10)
num2 = rand.randrange(-10,10)


print("What is",num1,"plus",num2,"?" )
ans = input()
if int(ans) == num1+num2:
    print("YOU GOT IT RIGHT")


num1 = rand.randrange(-10,10)
num2 = rand.randrange(-10,10)
print("What is",num1,"times",num2,"?" )
ans = input()
if int(ans) == num1 % num2:
    print("You got it right!")