def snake_to_camel(snake_str):
    snake_txt=snake_str.split('_')
    return snake_txt[0]+''.join(x.title() for x in snake_txt[1:])

x=str(input())
y=snake_to_camel(x)
print(y)
