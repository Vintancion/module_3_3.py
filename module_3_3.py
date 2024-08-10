def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(8, False, 'str')
print_params(b = 25)
print_params(c=[1, 2, 3])
print('-----')
values_list = ['string', [1,2], 34]
values_dict = {'a': 33, 'b': 'iphone', 'c': 33.33}
print(*values_list)
print(*values_dict)
print('-----')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)



