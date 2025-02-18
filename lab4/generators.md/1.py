n=int(input())
def generator():
    for i in range(1,n+1):
        yield i**2
for i in generator():
    print(i)