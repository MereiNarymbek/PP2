n=int(input())
def gen():
    for i in range(n):
        yield i

for i in gen():
    if i%2==0:
        print(i, end=' ')
