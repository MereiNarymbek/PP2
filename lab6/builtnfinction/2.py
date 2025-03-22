def my_function(str):
  counterUpper=0
  counterLower=0
  for i in str:
        if i.isupper():
            counterUpper+=1
        elif i.islower():
                counterLower+=1
  return counterUpper,counterLower

str_input=input()
counterUpp, counterLow=my_function(str_input)
print(f"Uppercase: {counterUpp}")
print(f"Lowercase: {counterLow}")