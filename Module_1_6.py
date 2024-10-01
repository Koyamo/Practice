my_dict = {'Алексей' : 1988, 'Анна' : 2002, 'Борис' : 1992}
print(my_dict)
print(my_dict['Алексей'])
print(my_dict.get('Артем'))
my_dict.update({'Алла' : 1990, 'Инна' : 2012})
a = my_dict.pop('Анна')
print(a)
print(my_dict)
my_set = {1 , 2 , 3 , 3 , 2 , 1 , 'Коля', 'Вася', 'Коля', False}
print(my_set)
my_set.update(['Кира', 5])
my_set.remove('Коля')
print(my_set)