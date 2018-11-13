for _ in range(int(input())):
    s=input()
    f=1
    if len(s)%2!=0:
        l=s[:len(s)//2]
        r=s[(len(s)//2)+1:]
    else:
        l=s[:len(s)//2]
        r=s[len(s)//2:]
    #print(l,r)
    if set(l)!=set(r):
        print('NO')
        continue
    else:
        for i in set(l):
            if l.count(i)!=r.count(i):
                f=0
                break
    if f==1:
        print('YES')
    else:
        print('NO')
