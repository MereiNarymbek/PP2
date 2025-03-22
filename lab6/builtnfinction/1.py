def multiple_list(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

str_input=input()
numbers=list(map(int,filter(lambda x:x.isdigit(), str_input.split())))
print(multiple_list(numbers))
