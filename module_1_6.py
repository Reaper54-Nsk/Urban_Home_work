my_dict = {'Yana': 1998, 'Aleksey': 1994, 'Lyda': 1959}
print(my_dict)
print(my_dict['Lyda'])
my_dict.update({'Artem': 2020, 'Ilya': 2022})
abc = my_dict.pop('Aleksey')
print(my_dict.get('Aleksey'))
print(abc)
print(my_dict)
my_set = {1, 1, 2, 3, 4, 1, 2, 2, 'Pajiero', True}
print(my_set)
my_set.add('pinche')
my_set.add((1, 2, 3, 4, 5))
print(my_set.discard(2))
print(my_set)