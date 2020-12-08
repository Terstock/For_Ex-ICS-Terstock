"""головний модуль задачі
- виводить на екран та в файл розразункову таблицю
- виводить на екран первинні файли
"""

import os
import process_data2, data_service1, data_service2
from process_data2 import create_analize
from data_service1 import show_zayavki, get_zayavki
from data_service2 import show_dovidniks, get_dovidniks

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА ЗАЯВОК РАХУНКУ-ФАКТУРИ  ~~~~~~~~~

1 - вивести заявки на екран
2 - записати результат в файл
3 - вивести список заявок на постачання товарів
4 - вивести довідник товарів
0 - завершити роботу
---------------------------------------------------
"""

TITLE = "~~~~~~~~~~~~ ВИХІДНІ ДАНІ РАХУНКУ-ФАКТУРИ ~~~~~~~~~~~~"

HEADER =        \
"""
===========================================================================================================================================================
  Код замовника  |  Код товару  |                 Назва товару                    |        Автор        |   Ціна   |  Кількість  |  Податок  |    Сума      
===========================================================================================================================================================
"""

FOOTER = \
"""
============================================================================================================================================================
"""

STOP_MESSAGE = "Для продовження натисніть <Enter>"

def show_analize_table(rahunok_list):
    """вивід на екран таблиці заявок рахунку-фактури
    """
    print(f"\n\n{TITLE:^155}") #62
    print(HEADER)
    
    for rahunok in rahunok_list:
        print(f"{rahunok['cod of orderer']:^15}",        #код замовника
              f"{rahunok['cod of product']:^16}",        #код продукту
              f"{rahunok['name']:53}",                   #назва товару
              f"{rahunok['author']:20}",                 #автор
              f"{rahunok['price']:>3}",                  #ціна
              f"{rahunok['amount']:>12}",                #кількість
              f"{int(rahunok['podatok']):>12}",          #податок на додану вартість
              f"{rahunok['total']:>12}"                  #сума
              )

    print(FOOTER)
    
def write_analize(rahunok_list):
    """ запис заявок рахунку-фактури в файл
    """  
    with open('./data/analize.txt', "w") as analize_file:
        for rahunok in rahunok_list:
            line =  rahunok['cod of orderer'] + ';' +   \
            rahunok['cod of product'] + ';' +   \
            rahunok['name'] + ';' +   \
            str(rahunok['author']) + ';' +  \
            str(rahunok['price']) + ';' +  \
            str(rahunok['amount']) + ';' + \
            str(rahunok['podatok']) + ';' + \
            str(rahunok['total']) + '\n'       

            analize_file.write(line)
            
    print("Файл  успішно сформовано - можете його переглянути ...")
    
    
while True:
    
    os.system('clear')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")
    
    # обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)
        
    elif command_number == '1':
        rahunok_list = create_analize()
        show_analize_table(rahunok_list)
        input(STOP_MESSAGE)
        
    elif command_number == '2':
        rahunok_list = create_analize()
        write_analize(rahunok_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        orders = get_dovidniks()
        show_dovidniks(orders)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        clients = get_zayavki()
        show_zayavki(clients)
        input(STOP_MESSAGE)