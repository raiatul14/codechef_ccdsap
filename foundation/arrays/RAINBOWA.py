for _ in range(int(input())):
    n=int(input())
    s=list(map(int, input('').split()))
    f=0
    if s!=s[::-1]:
        f=1
    if set(s)!=set([i for i in range(1,8)]):
        f=1
    print('no' if f else 'yes')
