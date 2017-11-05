L=(1,2,3,4,5,6,7,8,9,10)
t1=0
for i in L:
    t1=t1+i
print(t1)
t2=0
i=0
while i<len(L):
    t2=t2+L[i]
    i=i+1
print(t2)
def sum_digits(n,t3):
    if n<len(L):
        t3=t3+L[n]
        n=n+1
        return  sum_digits(n,t3)
    else:
        return t3

print(sum_digits(0,0))
