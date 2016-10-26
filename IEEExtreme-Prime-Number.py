

#IEEExtreme Prime Number Solution
#Developed by Guilherme Hollweg
#Last modified in 10/2016
#numero de entrada (primo ou não)

num = 3517

origNum = num
lstPrimos = []

#Funcao que testa a entrada, para verificar se é primo ou não
def TestPrimo(n):
    if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
        return False
    for x in range(n):
        if x != 0 and x != 1:
            if n%x == 0 and n != x:
                return False
    return True

#Funcao que varre todos os primos e guarda-os em uma lista
def primos(n):
    global lstPrimos
    for x in range(n):
        if x!= 0 and x!=1:
            if n%x==0 and n!=x:
                return '%s nao e um numero primo' %n
    lstPrimos.append(n)
    return '%s e um numero primo' %n

testNum = TestPrimo(num)

if testNum == True:
    print '%s e um numero primo' %num
    while num > 2:
        y = TestPrimo(num-1)
        if y == True:
            print '%s e um numero primo' %(num-1)
            break
        #else:
            #print '%s nao e um numero primo' %(num-1)
        num = num - 1
    dif = origNum - (num - 1)
    print 'A diferenca entre o numero primo e seu antecessor e: %s' %(dif)
    lst = map(primos, range(dif))
    if 0 in lstPrimos:
        lstPrimos.remove(0)
    if 1 in lstPrimos:
        lstPrimos.remove(1)   
    for i in range(len(lstPrimos)):
        res = dif - lstPrimos[i]
        if res in lstPrimos:
            if ((res + lstPrimos[i] + num - 1) == origNum):
                print '\n O numero primo %s pode ser representado pela soma de %s + %s + %s = %s' %(origNum, res, lstPrimos[i], (num - 1), origNum)
                break
else:
    print '%s nao e um numero primo' %num
    
