n=int(input())
def gen():
    for i in range(n):
        yield i

for i in gen():
    if i%3==0 and i%4==0:
        print(i, end=' ')