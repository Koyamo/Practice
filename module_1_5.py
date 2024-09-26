immutable_var = (1, 2, True, 'string' )
print(immutable_var)
#print(type(immutable_var))
#immutable_var[0] = 5
#Значения внутри кортежа нельзя заменить. Данные в нем всегда неизменны.
mutable_list = [1, 2, 3, 'melon']
mutable_list[0] = 'apple'
print(mutable_list)