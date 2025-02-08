print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0 #return false

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!") #if function is true it will print YES!
else:
  print("NO!")
  
x = 200
print(isinstance(x, int)) #isinstance() function, which can be used to determine if an object is of a certain data type