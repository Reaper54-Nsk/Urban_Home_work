immutable_var = ('string', 5, 3.5, True)
print(immutable_var)
#immutable_var [0] = 'not string' # элементы кортежа нельзя менять, в отличии от последовательности. Кортеж не поодерживает обращение к элементам!
#print(immutable_var)
mutable_list = [1, 2, 3, 4, 'String', False]
mutable_list[4] = 7
print(mutable_list)


