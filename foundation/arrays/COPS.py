for _ in range(int(input())):
    m,x,y=map(int, input('').split())
    c=list(map(int, input('').split()))
    total=x*y
    check=set()
    for i in c:
        a=i-total
        if a<1:
            a=1
        j=i+total
        if j>100:
            j=100
        check.update(range(a,j+1))
        #print(check)
        if len(check)==100:
            break
    print(100-len(check))
