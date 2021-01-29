#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

'''f is_prime(n):
    i=2
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 1
  
    return True

#print(is_prime(9))
y = []  
m = 1 
while len(y) < 100000:
    if is_prime(m):
       
        y = y + [m]
        m = m + 1
print(y,m)'''
def count():
    D = {}  
    q = 2   
    while 1:
        if q not in D:
            yield q        
            D[q*q] = [q]   
        else:
            for p in D[q]: 
                D.setdefault(p+q,[]).append(p)
            del D[q]       
        q += 1

def n_prime(n):
    for i, prime in enumerate(count()):
        if i == n - 1:
            return prime

print(n_prime( 10001))
