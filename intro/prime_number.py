import math

num = int(input("Enter a number: "))

flag = False

# prime numbers are greater than 1
if num > 1:
    # a factor must be less than or equal to the square root of the number
    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
    # the else clause of the for loop runs if and only if
    # we don't break out the for loop
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")