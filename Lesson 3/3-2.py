def func_1 (**kwargs):
    return " ".join(kwargs.values())


print(func_1(name=input(" Введите ваше имя: "), surname=input(" Введите вашe фамилию: "),
             birthday=input(" Введите вашу дату рождения: "), city = input(" Введите ваш город: "),
             email = input(" Введите вашу почту: "), phonenumber = input(" Введите номер вашего телефона: ")))