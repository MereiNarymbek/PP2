def get_permutations(stroka, empty = ""):
    if len(stroka) == 0:
        print(empty)
    else:
        for i in range(len(stroka)):
            combinations = stroka[:i] + stroka[i + 1:]
            get_permutations(combinations, empty + stroka[i])
            
def get_output():
    input_strings = input()
    get_permutations(input_strings)
    
get_output()