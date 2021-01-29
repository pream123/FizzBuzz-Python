factor3=0
factor5=0
for i in range(1,101):
   
    factor3 =factor3+1
    factor5 =factor5+1
    output=""
    
    if factor3==3:
        output+="fizz" 
        factor3=0
    if factor5==5:
        output+="buzz"
        factor5=0
    
    if output=="":
        print(i)
    else:
        print(output)