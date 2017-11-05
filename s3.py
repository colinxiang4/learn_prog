numbers=(1,12,32,34,36,39,41,43,50)
n=input()
n=int(n)
checker=False
for i in numbers:
    if i==n:
        checker=True
        break
if checker:
    print("your number is in the list!")
else:
    print("your number is not in the list.")

