
#IEEExtreme Prime Number Solution
#Developed by Guilherme Hollweg
#Last modified in 10/2016

#input number (prime or not)
num = 3517

origNum = num
lstPrimes = []

#Test input to see if its prime or not
def TestPrime(n):
    
    #Kills a lot of prime numbers in an easy way
    if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11 == 0 or n == 0 or n == 1:
        return False
    
    #test it via brute way
    for x in range(n):
        if x != 0 and x != 1:
            if n%x == 0 and n != x:
                return False
    return True

#Find all prime numbers and store it on a list
def primes(n):
    global lstPrimes
    for x in range(n):
        if x!= 0 and x!=1:
            if n%x == 0 and n != x:
                return '%s is not a prime number' %n
    lstPrimes.append(n)
    return '%s is prime' %n

testNum = TestPrime(num)

if testNum == True:
    print '%s is prime' %num
    while num > 2:
        y = TestPrime(num-1)
        if y == True:
            print '%s is prime \n' %(num-1)
            break
        #else:
            #print '%s is not a prime number' %(num-1)
        num = num - 1
    
    dif = origNum - (num - 1)
    print 'The difference between the prime number and its antecessor is: %s' %(dif)
    lst = map(primes, range(dif))
    
    if 0 in lstPrimes:
        lstPrimes.remove(0)
    
    if 1 in lstPrimes:
        lstPrimes.remove(1)   
    
    for i in range(len(lstPrimes)):
        res = dif - lstPrimes[i]
        if res in lstPrimes:
            if ((res + lstPrimes[i] + num - 1) == origNum):
                print '\n The prime number %s can be represented by the sum %s + %s + %s = %s' %(origNum, res, lstPrimes[i], (num - 1), origNum)
                break
else:
    print '%s is not a prime number' %num
    

