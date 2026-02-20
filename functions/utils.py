import os
import platform

def clear_screen():
    """
    Вспомогательный модуль для очистки консоли
    """
    
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')