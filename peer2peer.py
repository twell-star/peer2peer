password = input('Введите пароль:')
const = 15                            # назначение технической целочисленной константы 
password_length = len(password)       # определение длины пароля в символах

try:
    result1 = const/password_length   # выражение для проверки деления на ноль
    result2 = int(password)           # выражение для проверки корректности перевода пароля из строкового типа в целочисленный 
    print('Ваш пароль состоит только из цифр')
    
except ZeroDivisionError:
    print('Вы ввели пустой пароль')

except ValueError:
    print('Требования к паролю соблюдены') 
