for _ in range(int(input())):
    n,k=map(int, input('').split())
    nw=input().split()
    ans=''
    p=[]
    for i in range(k):
        p+=input().split()
    #print(p)
    for i in range(n):
        if nw[i] in p:
            ans+='YES '
        else:
            ans+='NO '
    print(ans)
