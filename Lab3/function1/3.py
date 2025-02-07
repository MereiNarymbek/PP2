def solve(numheads, numlegs):
    y = (numlegs - 2*numheads)/2
    x = numheads - y
    print(f"Chickens are {int(x)} and Rabbits are {int(y)}")

solve(35, 94)