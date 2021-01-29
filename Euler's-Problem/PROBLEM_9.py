#Problem9
'''There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

'''for a in range(1, 1000):
     for b in range(a, 1000):
            c = 1000 - a - b
            if c > 0:
                if c*c == a*a + b*b:
                    print (a, b,c,a*b*c)
                    break'''
import math 

while sum<1000:
    if sum<1000:
        a+=1
        b=a+1
       # print(b)
    else:
        b+=1
       # print(b)
    c=math.sqrt(a*a+b*b)

    sum=a+b+c
print(a,b,c,a*b*c)