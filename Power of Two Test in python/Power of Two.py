# Write a program that takes an integer as input and returns true if the input is a power of two.print('Enter an integer')
print('Enter an Integer')
integer = int(input())  


power= integer > 0 and (integer & (integer - 1)) == 0

# Print the result
if power:
    print('True')
else:
    print('False')
