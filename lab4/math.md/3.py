import math
n,s=map(int, input().split())
rad=math.tan(math.pi/n)
A=(n*pow(s,2))/(4*rad)
print(f"{A:.4g}")