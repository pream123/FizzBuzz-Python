#PROBLEM 10
#Find the sum of all the primes below two million.

l=[]

for i in range(1,2000001):

    for j in range(1,i):

        if i%j==0 and i!=j:

            l.append(i)

print("sum : ",sum(l))

total=0

for i in range(0,len(l)):

    total=total+l[i]

print("sum = ",total)

#another way 


total=0

for num in range(1,2000001):  
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            count = count + 1
            break

    if (count == 0 and num != 1):
        total = total + num

print("sum = ",total)
#I was using jupyter notebook, sum was printed intil 200000 and then after for 2 mil it stoped.