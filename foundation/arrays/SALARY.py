for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        w=list(map(int, input('').split()))
        print((sum(w)-n*min(w)))
        break
