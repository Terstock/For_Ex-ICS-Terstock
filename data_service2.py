"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""


def get_orders():
    """ повертає список заказів який отримує ззовні

    Returns:
        order_list: список заказів
    """    

    with open("./data/orders.txt", encoding="utf-8") as orders_file:
        from_file = orders_file.readlines()

    # накопічувач клієнтів
    orders_list = []

    for line in from_file:
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        orders_list.append(line_list)
    
    return orders_list

def show_orders(orders):
    """виводить на екран список заказів заданого діапазона

    Args:
        orders ([list]): список заказів
    """

    order_code_from = input("З якого кода? ")
    order_code_to   = input("По який код? ") 

    for order in orders:
        if  order_code_from <= order[0] <= order_code_to: 
            print("код: {}; назва: {}; автор: {}; ціна: {} грн.".format(order[0], order[1], order[2], order[3]))


#orders = get_orders()
#show_orders(orders)