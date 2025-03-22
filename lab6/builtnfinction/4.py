import time
import math
def square_root_after_milliseconds(number,zaderjka):
    time.sleep(zaderjka/1000)
    square=math.sqrt(number)
    print(f"Square root of {number} after {zaderjka} is {square}")
    return square
x=int(input())
y=int(input())
square_root_after_milliseconds(x,y)
