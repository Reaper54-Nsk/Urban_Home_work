def print_parmas (a=1, b='string', c=True):
    print(a, b, c)
print_parmas()
print_parmas(b=25)
print_parmas(c=[1,2,3])

value_list = [5, 'str 2', (1,2,3)]
value_dict = {'a': 329, 'b': 293, 'c': 932}
print_parmas(*value_list)
print_parmas(**value_dict)

values_list = ['str', 99]
print_parmas(*values_list, 42)