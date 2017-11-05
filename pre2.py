n=2
cnt =0
while True:
    is_prime=True
    for i in range(2, n):
        if n % i ==0:
            is_prime=False
            break

    if is_prime:
        print(n)
        cnt +=1
        if cnt>=2270:
            break
    n+=1

