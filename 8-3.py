class NotNumber(ValueError):
    pass
 
my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Введите число!', ex)
print(my_list)
