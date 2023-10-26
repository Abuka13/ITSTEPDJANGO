import random
import string

# Генерация случайного логина
login_length = 8
characters = string.ascii_letters + string.digits
random_login = ''.join(random.choice(characters) for _ in range(login_length))

# Генерация случайного пароля
password_length = 12
characters = string.ascii_letters + string.digits
random_password = ''.join(random.choice(characters) for _ in range(login_length))

print("Случайный логин:", random_login)
print("Случайный пароль:", random_password)