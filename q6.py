n=int(input("Enter a number: "))
ans=input("a for addition, m for multiplication: ")
if ans=="a":
  sum=0  
  for num in range(1,n+1): 
        sum=sum+num
  print(sum)
if ans=="m":
    prod=1
    for num in range(1,n+1):
      prod=prod*num
    print(prod)

