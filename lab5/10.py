import re
def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str
x = str(input())
y = camel_to_snake(x)
print(y)