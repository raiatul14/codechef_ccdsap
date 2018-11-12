def solve(s):
    n=0
    #print(len(s))
    for i in range(0,len(s)):
        if s[i]=='1':
            n+=1
    return (n*(n+1))//2
for _ in range(int(input())):
    n=int(input())
    st=input()
    print(solve(st))
