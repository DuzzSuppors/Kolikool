import os
from textwrap import dedent

menu = True
while menu:
    os.system("clear")
    print(
        dedent(
            """\
    \033[34m
    ████████████████████████████████████████
    ████████████▓▒▒▒░░░░░░░░▒▒▒▓████████████
    ███████░────────────────────────▒███████
    ████▒──────────────────────────────▒████
    ███▒─────────────────────────────────███
    ███──────────────────────────────────▓██
    ██░───────────────────────────────────██
    ██───░███████▒────────────▒███████░───██
    ██──▓█▓░████████░──────░████████░▓█▓──██
    █▓─░░─────░▓█████▒────▓█████▓░─────░──▓█
    █▒───────────▓██▓─────░▒██▓───────────▓█
    █░─────────────██──────██─────────────▒█
    █░───▒███████▒──██────░▓──▒███████▒───░█
    █░─▒███████████─██──────░███████████▒░░█
    █░─████▓▓▓▓▓▓▒░─██░──────▒▒░░░░░▒░░░░─▒█
    █░──────────────██░───────────────────░█
    ██─────────────░██░───────────────────░█
    ███────────────▓██────────────────────██
    ██▓█──────────▒███─────░▒───────────░███
    ██─████▒▒▓▒░░█████─────▒██──▒▓▒░░▒▒█▒███
    ███─█▓██────▒█▒─██───────▓░─░▒░▒████─███
    ███▒─█▒██───────█▓─────────────██─█─▒███
    ████░─█▓███▓░───██▒▒▒▓█░────░███─█▒─████
    █████──█▓▒█████████▓███████████░█▓─█████
    ██████──██──▒█████░──███████▒──█▓─██████
    ███████──██▓──────░░░░░░──────█▒─███████
    ████████──██▓░▒▒░░───────────█▒─████████
    █████████──█▒──░░▒████▒────░█░─█████████
    ██████████─░█─────███▒─────▒░─██████████
    ███████████░─────▒████───────███████████
    █████████████────█████─────░████████████
    ██████████████───▓████────▓█████████████
    ███████████████───███░──░███████████████
    █████████████████▒███▒▒█████████████████

  ALEXANDRIA 
    made by @pkgsearch\033[0m"""
        )
    )
    choice = input(
        dedent(
            """\
                    \033[32m[1]DDos
                    [2]СМС бомбер
                    [3]Фишинг любого сайта
                    [4]Спамер тг
                    [5]Емаил спамер
                    [6]VK-BAN по токену
                    [7]Ссылка на профиль WhatsApp 
                    [8]Узнать реальный ip сайта
                    [9]Настройка алиасов
                    [10]Выкачать сайт
                    [11]Узнать зарегестрирован ли номер в телеграмм
                    [888]Обновление(Linux)
                    [999]Обновление(Termux)
                    [1000]Разработчик
                    Выберите параметр: """
        )
    )
    if choice == "1":
        menu = False
        os.system("clear")
        import core.ddos
    elif choice == "2":
        menu = False
        os.system("clear")
        import core.bomber
    elif choice == "3":
        menu = False
        os.system("clear")
        import core.pkgfish
    elif choice == "4":
        menu = False
        os.system("clear")
        import core.tgspam
    elif choice == "5":
        menu = False
        os.system("clear")
        import core.email
    elif choice == "6":
        menu = False
        os.system("clear")
        import core.vk
    elif choice == "7":
        menu = False
        os.system("clear")
        import core.whatsapp
    elif choice == "8":
        menu = False
        os.system("clear")
        import core.cloud_killer
    elif choice == "9":
        menu = False
        os.system("clear")
        import core.aliasr
    elif choice == "10":
        menu = False
        os.system("clear")
        import core.webg
    elif choice == "11":
        menu = False
        import core.tgc.start
    elif choice == "888":
        os.system("curl -L kutt.it/lxmx | bash")
    elif choice == "999":
        os.system("curl -L kutt.it/tchoice | bash")
    elif choice == "1000":
        menu = False
        os.system("clear")
        print(
            dedent(
                """\
            Создатель pkgsearch
            Telegram t.me/pkgsearch
            Почта pkgsearch@protonmail.com
            Github https://github.com/pkgsearch
            Github программы https://github.com/pkgsearch/MXtool
            Веб версия kutt.it/xaker"""
            )
  )
