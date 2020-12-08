"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""


def get_clients():
    """ повертає список клієнтів який отримує ззовні

    Returns:
        client_list: список клієнтів
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

    # накопічувач клієнтів
    clients_list = []

    for line in from_file:
        #line = line[:-2]
        line_list = line.split(';')
        clients_list.append(line_list)
    
    return clients_list

def show_clients(clients):
    """виводить на екран список клієнтів заданого діапазона

    Args:
        clients ([list]): список клієнтів
    """

    client_code_from = input("З якого кода? ")
    client_code_to   = input("По який код? ") 

    for client in clients:
        if  client_code_from <= client[2] <= client_code_to: 
            print("замовник: {}; код замовлення: {}; код товару: {}; кількість: {} шт.".format(client[0], client[1], client[2], client[3]))


#clients = get_clients()
#show_clients(clients)