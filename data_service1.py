"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

def get_zayavki():
    """ повертає список заявок на постачання товару, який отримує ззовні
    Returns:
        zayavka_list: список заявок на постачання товару
    """    

    from_file = [
        "КНТЕУ;1101;1001;5",
        "КНТЕУ;1222;1002;5",
        "КНТЕУ;1029;1003;20",
        "КНТЕУ;1040;1004;5",
        "КНТЕУ;1050;1005;30",
        "КНЕУ;1100;1006;200",
        "КНЕУ;1101;1001;6",
        "КНЕУ;1222;1002;6",
        "КНЕУ;1029;1003;25",
        "КНЕУ;1040;1004;7",
        "КНЕУ;1050;1005;25",
        "КНЕУ;1100;1006;220",
        "КНУ;1101;1001;8",
        "КНУ;1222;1002;8",
        "КНУ;1029;1003;23",
        "КНУ;1040;1004;7",
        "КНУ;1050;1005;28",
        "КНУ;1100;1006;210"
    ]

    # накопічувач заявок
    zayavki_list = []

    for line in from_file:
        #line = line[:-2]                #обрізання строк
        line_list = line.split(';')
        zayavki_list.append(line_list)
    
    return zayavki_list

def show_zayavki(zayavki):
    """виводить на екран список заявок заданого діапазона

    Args:
        zayavki ([list]): список заявок
    """

    zayavka_code_from = input("З якого коду? ")
    zayavka_code_to   = input("По який код? ") 

    for zayavka in zayavki:
        if  zayavka_code_from <= zayavka[2] <= zayavka_code_to: 
            print("замовник: {}; код замовлення: {}; код товару: {}; кількість: {} шт.".format(zayavka[0], zayavka[1], zayavka[2], zayavka[3]))

#zayavki = get_zayavki()
#show_zayavki(zayavki)