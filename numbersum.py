n=int(input("Enter a number: "))
sum=0
for num in range(1,n+1):
    if num%3==0:
        sum=sum+num
    if num%5==0:
        sum=sum+num
print(sum)

