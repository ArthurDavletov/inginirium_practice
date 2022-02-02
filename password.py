def ask_password(password):
    for i in range(3, 0, -1):
        if i != 1:
            temp = input(f"У вас {i} попытки. Введите пароль: ")
        else:
            temp = input(f"У вас 1 попытка. Введите пароль: ")
        if temp == password:
            return "Вы угадали пароль. Доступ разрешен."
        while True:
            input("Доступ запрещен. ")


print(ask_password("password"))
