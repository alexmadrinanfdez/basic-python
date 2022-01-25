print("Enter a number:", end=" ")
try:
    num = int(input())
    print(str(num)[::-1])
except ValueError:
    print("Next time, enter a number...")