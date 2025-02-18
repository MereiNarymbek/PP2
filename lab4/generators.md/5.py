n=int(input())
def gen():
    for i in reversed(range(n+1)):
        yield i
    
for i in gen():
    print(i, end=' ')
