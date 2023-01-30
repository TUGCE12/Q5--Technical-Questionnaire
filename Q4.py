def checkPrime(number):
    if number == 1:
        return False
    if number == 2: #prime
        return True
    if number > 2:
        if number % 2 == 0: #not prime
            return False
        for i in range(3,number,2):
            if(number % i == 0): #not prime
                return False
    return True

def findPrime_inRange(A, B):
    if A % 2 == 0:
        A = A+1
    for i in range(A,B,2):
        if checkPrime(i):
            print(i)

findPrime_inRange(500,600)
