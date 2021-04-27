import winreg

value = [] # Массив, куда буду записываться все ключи
j = 0
startup = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\ZZZ")
while 1:
    try:
        value.append(winreg.EnumValue(startup, j)) # Запись ключей в массив
        j += 1
    except:
        break
print(value)
