import time
import sys
import os
import requests
import webbrowser
import subprocess
from plyer import notification

# Константы для авторизации
VALID_USERNAME = "Crack"
VALID_PASSWORD = "Cracked"

def display_ascii_art():
    """Выводит ASCII-арт на экран."""
    ascii_art = """
/$$   /$$                                         /$$   /$$                        
| $$$ | $$                                        | $$  | $$                        
| $$$$| $$ /$$   /$$  /$$$$$$   /$$$$$$$ /$$   /$$| $$ /$$$$$$    /$$$$$$  /$$$$$$$ 
| $$ $$ $$| $$  | $$ /$$__  $$ /$$_____/| $$  | $$| $$|_  $$_/   |____  $$| $$__  $$
| $$  $$$$| $$  | $$| $$  \__/|  $$$$$$ | $$  | $$| $$  | $$      /$$$$$$$| $$  \ $$
| $$\  $$$| $$  | $$| $$       \____  $$| $$  | $$| $$  | $$ /$$ /$$__  $$| $$  | $$
| $$ \  $$|  $$$$$$/| $$       /$$$$$$$/|  $$$$$$/| $$  |  $$$$/|  $$$$$$$| $$  | $$
|__/  \__/ \______/ |__/      |_______/  \______/ |__/   \___/   \_______/|__/  |__/
                                                                                     
"""
    # Печатаем ASCII-арт
    print(ascii_art)
    print("Добро пожаловать в систему! Пожалуйста, авторизуйтесь для продолжения.")

def print_loading_bar(iteration, total, length=40):
    """Печатает загрузочный бар с прогрессом."""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r[{bar}] {percent}% Завершено')
    sys.stdout.flush()

def fake_loader(duration):
    """Функция для имитации загрузки."""
    total_steps = 100
    for i in range(total_steps + 1):
        time.sleep(duration / total_steps)
        print_loading_bar(i, total_steps)
    print()  # Печатаем новую строку после завершения

def authenticate():
    """Функция для авторизации пользователя."""
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return True
    else:
        print("Неверный логин или пароль. Завершение программы.")
        return False

def show_success_notification(timeout=10):
    """Функция для показа уведомления о успешной авторизации."""
    notification.notify(
        title="Успех!",
        message="Успешно вошли в систему!",
        timeout=timeout  # Уведомление будет отображаться заданное количество секунд
    )

def download_file(url, save_path):
    """Скачивает файл по указанной ссылке и сохраняет его в указанное место."""
    try:
        response = requests.get(url, stream=True)
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Файл успешно загружен: {save_path}")
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")

def open_file(file_path):
    """Открывает загруженный файл."""
    try:
        subprocess.Popen([file_path], shell=True)
        print(f"Файл открыт: {file_path}")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def main():
    """Основная функция."""
    display_ascii_art()  # Показать ASCII-арт

    print("Пожалуйста, авторизуйтесь для доступа к системе.")
    
    # Авторизация
    if authenticate():
        # Уведомление о успешной авторизации
        show_success_notification(timeout=10)  # Уведомление длится 10 секунд
        print("Авторизация успешна!")
        print("Загрузка...")
        fake_loader(5)  # Загрузка длится 5 секунд
        print("Загрузка завершена.")
        
    else:
        print("Не удалось авторизоваться. Завершение программы.")

if __name__ == "__main__":
    main()
