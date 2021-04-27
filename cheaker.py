import winreg

# Функция наличия ключей блокировки встроенного редактора реестра и диспетчера задач.
def proverkablock():
    value = [] # Массив, куда будут записываться все ключи
    j = 0
    startup = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies")
    while 1:
        try:
            value.append(reg.EnumValue(startup, j)) # Запись ключей в массив
            j += 1
        except:
            break
    print(value)
    if (('ff', '', 0)) in value: # Проверка массива на определенный ключ
        print("OK")              # Действие, если ключ есть
    else:
        print("Что-нибудь")      # Действие, если ключа нет (например добавление оного)
