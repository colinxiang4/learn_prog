L1=('1','3','5')
L2=('2','4','6')
result=[None]*(len(L1)+len(L2))
result[::2]=L1
result[1::2]=L2
print(result)
