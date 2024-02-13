# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
#multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
#"FizzBuzz"
x = range(1,101)
for i in x:
    print(i)

    if i%3==0:
        print('Fizz')
    if i % 5 ==0:
        print('Buzz')
    if i % 3 ==0 and i % 5 ==0: 
        print('FizzBuzz')