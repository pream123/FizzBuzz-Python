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
#I was using jupyter notebook, sum was printed intil 200000 and then after for 2 mil it stoped.