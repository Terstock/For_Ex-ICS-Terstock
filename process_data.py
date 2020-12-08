""" розрахунок заявок на товари по магазину
"""
from data_service1 import get_clients
from data_service2 import get_orders

# словник в якому будуть накоплюватись результати розрахунків
rahunok = {
    'cod of orderer'   : 0.0,           #код замовника
    'cod of product'   : 0.0,           #код товару
    'name'             : '',            #назва
    'author'           : '',            #автор
    'price'            : 0.0,           #ціна
    'amount'           : 0.0,           #кількість
    'podatok'          : 0.0,           #податок на подану вартість
    'total'            : 0.0            #сума
}

def create_analize():
    """формування списку заявок по магазину

    Returns:
        rahunok_list: список заявок
    """
    
    def get_cod_of_orderer(client_code):
        """знаходить код замовника товару

        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: код замовника товару
        """
        for client in clients:
            if client_code == client[2]:
                return client[0]
            
        return "*** назва не знайдена"
    
    def get_amount(client_code):
        """знаходить кількість товару

        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: кількість товару
        """
        for client in clients:
            if client_code == client[2]:
                return client[3]
            
        return "*** назва не знайдена"
    
    # накопичувач рахунку-фактури 
    rahunok_list = []

    orders = get_orders()
    clients = get_clients()

    for order in orders:
        
        # робоча змінна
        rahunok_work = rahunok.copy()
        
        rahunok_work['cod of orderer'] = get_cod_of_orderer(order[0])                       #код замовника
        rahunok_work['cod of product'] = order[0]                                           #код товару
        rahunok_work['name'] = order[1]                                                     #назва
        rahunok_work['author'] = order[2]                                                   #автор
        rahunok_work['price'] = order[3]                                                    #ціна
        rahunok_work['amount'] = get_amount(order[0])                                       #кількість
        rahunok_work['podatok']  = int(rahunok_work['price']) * int(rahunok_work['amount']) * float(0.2)                                               
        rahunok_work['total'] =  int(rahunok_work['price']) * int(rahunok_work['amount']) + int(rahunok_work['podatok'])

        rahunok_list.append(rahunok_work)
       
    
    return rahunok_list

#rahunok = create_analize()

#for item in rahunok:
    #print(item)     