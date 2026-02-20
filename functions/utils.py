import os
import platform

def clear_screen():
    """Очищает консоль."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')