import winreg

# Функция наличия ключа блокировки (невозможности открытия) диспетчера задач.
def proverka_registry():
    value = [] # Массив, куда будут записываться все ключи sub_key System.
    j = 0
    startup = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
    while 1:
        try:
            value.append(reg.EnumValue(startup, j)) # Запись всех ключей sub_key System в массив.
            j += 1
        except:
            break
    print(value)
    if (('DisableTaskMgr', 1, 4)) in value: # Проверка массива на ключ
        print("OK")              # Действие, если ключ есть
    else:
        print("Что-нибудь")      # Действие, если ключа нет (например добавление оного)
