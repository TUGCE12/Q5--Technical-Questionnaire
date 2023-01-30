#---------------def findPrime_inRange(A, B):---------------
# To find prime numbers in a given range, we follow these steps:
# Check if the first number is 2, if it is 2, the screen is printed.
# The first number is checked to see if it is an even number. If it is an even number, 1 is added. In this way, our starting number becomes an odd number.
# The reason for adding 1 is that we only want to navigate the odd numbers while navigating the range with the for loop. For time saver.
# We start scanning by skipping the number range given by the for loop two by two.
# For each number, it is checked whether that number is prime. If it is prime, it is printed on the screen.

# ---------------Check if it's prime-- def checkPrime(number):---------------
# Check whether the number is 1 or less than 1. If this condition is met, it is not prime.
# Check if the number is equal to 2. Because 2 is the only even number that is prime.
# After checking whether the number is 2, it is checked whether the number is divisible by 2. If it is divisible by 2, it is an even number and cannot be prime.
# Check whether the Number can be divided by odd numbers between 3 and Number.
# If even 1 quotient is without a remainder, it means the number is not prime.
# A number is prime if it is not divisible by any.


def checkPrime(number):
    if number <= 1:
        return False
    if number == 2: #prime
        return True
    if number % 2 == 0: #not prime
        return False
    for i in range(3,number,2):
        if(number % i == 0): #not prime
             return False
    return True

def findPrime_inRange(A, B):
    if(A == 2):
        print(A)
    if A % 2 == 0:
        A = A+1
    for i in range(A,B,2):
        if checkPrime(i):
            print(i)

findPrime_inRange(500,600)
