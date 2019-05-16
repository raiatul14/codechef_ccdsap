#Let's test this
for _ in range(int(input())):
    x,y,k,n=map(int, input('').split())
    l=[]
    flag=0
    for i in range(n):
        p,c=map(int,input('').split())
        l.append([p,c])
    for i in range(n):
        if y+l[i][0]>=x and k>=l[i][1]:
            flag=1
            print('LuckyChef')
            break
    if flag==0:
        print('UnluckyChef')
