for _ in range(int(input())):
    n,c=map(int, input("").split())
    a=list(map(int, input("").split()))
    assert(len(a)==n)
    if c>=sum(a):
        print("Yes")
    else:
        print("No")
