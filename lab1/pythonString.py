print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

#multiline
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#string are arrays
a = "Hello, World!"
print(a[1])

#Looping through a string
for x in "banana":
  print(x)
  
#string length
a = "Hello, World!"
print(len(a))   

#check string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")