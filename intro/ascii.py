# find the ASCII value a the given character

print("Enter a single character: ")
char = input()

if(type(char) != str or len(char) != 1):
    print("Do as you're told!")
else:
    print("The ASCII value of '" + char + "' is", ord(char))