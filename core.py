# импотрование нужных библиотек
import os
import shutil
import datetime


# сохранение информации о работе прораммы в отдельный файл
def save_info(message):
    data_time = datetime.datetime.now()
    result = f"{data_time} - {message}\n"
    with open("log_file.txt", "a", encoding="utf-8") as i:
        i.write(result)


# создание файла в текущей дериктории
def create_file(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)
        save_info("Вызвана функция создания файла в текущей дериктории")


# создание папки в текущей дериктории
def crate_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папку уже есть")
    save_info("Вызвана функция создания папки в текущей дериктории")


# просмотр файлов и папок в текущей дериктории
def list_file_dir():
    print(os.listdir())
    save_info("Вызвана функция просмотра файлов и папок в текущей дериктории")


# просмотр папок в текущей дериктории
def list_dir():
    all_file = os.listdir()
    result = []
    for i in all_file:
        if os.path.isdir(i):
            result.append(i)
    print(result)
    save_info("Вызвана функция посмотра папок в текущей дериктории")


# просмотр файлов в текущей дериктории
def list_file():
    all_file = os.listdir()
    for i in all_file:
        if os.path.isdir(i):
            all_file.remove(i)
    print(all_file)
    save_info("Вызвана функция просмотра файлов в текущей дериктории")


# удаление фала или папки в текущей дериктории
def rm_file_dir(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        try:
            os.remove(name)
        except FileNotFoundError:
            print("Такого файла нет")
    save_info("Вызвана функция удаление фала или папки в ткущей дериктории")


# копирование файла или папки в текущей дериктории
def copy_file_dir(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Такая папка уже существует")
    else:
        try:
            shutil.copy(name, new_name)
        except FileNotFoundError:
            print("Такого файла нет в текущей дериктории")
    save_info("Вызвана функция копирования файла или папки в текущей дериктории")


# очистка лога
def clear_log():
    with open("log_file.txt", "w+") as f:
        f.seek(0)


# изменение рабочей дериктории
def change_dir(name):
    os.chdir(name)


# проверка работоспособносоти функций

# if __name__ == "__main__":
# create_file("test.txt") # создание файла в текущей дериктории
# crate_dir("new_folder") # создание папки в текущей дериктории
# list_file_dir() # просмотр файлов и папок в текущей дериктории
# list_dir() # просмотр папок в текущей дериктории
# list_file() # просмотр файлов в текущей дериктории
# rm_file_dir("test.txt") # удаление фала или папки в текущей дериктории
# copy_file_dir("test.txt", "test_copy.txt") # копирование файла или папки в текущей дериктории
# save_info("оло") # сохранение своей информации о работе прораммы в отдельный файл
# clear_log() # очистка лога
