import sys
from core import save_info, create_file, crate_dir, list_file_dir, list_dir, list_file, rm_file_dir, \
    copy_file_dir, save_info, clear_log, change_dir

command = sys.argv[1]

if command == "mk_file":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название файла")
    else:
        create_file(name)
elif command == "mk_dir":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название папки")
    else:
        crate_dir(name)
elif command == "list":
    list_file_dir()
elif command == "list_dir":
    list_dir()
elif command == "list_file":
    list_file()
elif command == "rm_file":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название файла")
    else:
        rm_file_dir(name)
elif command == "copy_file":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название копируемого файла")
    else:
        try:
            new_name = sys.argv[3]
        except IndexError:
            print("Отсутствует название нового файла")
        else:
            copy_file_dir(name, new_name)
elif command == "save_info":
    try:
        message = sys.argv[2]
    except IndexError:
        print("Отсутствует сохраняемое сообщение")
    else:
        save_info(message)
elif command == "clear_log":
    clear_log()
elif command == "ch_dir":
    name = sys.argv[2]
    change_dir(name)
elif command == "help":
    print(
        "[mk_file] + [<file_name>] -- Создание файла в текущей дериктории.\n"
        "[mk_dir] + [<folder_name>] -- Создание папки в текущей дериктории.\n"
        "[list] -- Просмотр файлов и папок в текущей дериктории.\n"
        "[list_dir] -- Просмотр папок в текущей дериктории.\n"
        "[list_file] -- Просмотр файлов в текущей дериктории.\n"
        "[rm_file] + [<folder_name or file_name>] -- Удаление фала или папки в текущей дериктории.\n"
        "[copy_file] + [<file_name>] + [<new_file_name>] -- Копирование файла или папки в текущей дериктории.\n"
        "[save_info] + [<message>] -- Сохранение своей информации о работе прораммы в отдельный файл.\n"
        "[clear_log] -- Очистка лога.\n"
        "[ch_dir] + [<dir_name>] -- Сменить рабочую дерикторию"
    )
