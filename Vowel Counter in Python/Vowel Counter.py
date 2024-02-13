#Write a program that counts the number of vowels in a sentence.
str1 = input("Please Enter Your Own String : ")
c=str1.lower()
vowels = 0
 
for i in c:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
       
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)