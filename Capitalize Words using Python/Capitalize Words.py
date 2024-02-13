''' Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string'''
# fuction to capitalize
def capital(c):
    return c.title()

string = input('Enter a string ')
capitalized=capital(string)
print('Capitalized string')
print(capitalized)
