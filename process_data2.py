""" розрахунок заявок на товари по магазину
"""
from data_service1 import get_zayavki
from data_service2 import get_dovidniks

# словник в якому будуть накоплюватись результати розрахунків
rahunok = {
    'cod of orderer'   : 0.0,           #код замовника
    'cod of product'   : 0.0,           #код товару
    'name'             : '',            #назва
    'author'           : '',            #автор
    'price'            : 0.0,           #ціна
    'amount'           : 0.0,           #кількість
    'podatok'          : 0.0,           #податок на додану вартість
    'total'            : 0.0            #сума
}

def create_analize():
    """формування списку заявок по магазину

    Returns:
        rahunok_list: список заявок
    """
    
    def get_cod_of_orderer(zayavka_code):
        """знаходить код замовника товару

        Args:
            (zayavka_code ([type]): код клієнта

        Returns:
            [type]: код замовника товару
        """
        for zayavka in zayavki:
            if zayavka_code == zayavka[2]:
                return zayavka[0]
            
        return "*** назва не знайдена"
    
    def get_amount(zayavka_code):
        """знаходить кількість товару

        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: кількість товару
        """
        for zayavka in zayavki:
            if zayavka_code == zayavka[2]:
                return zayavka[3]
            
        return "*** назва не знайдена"
    
    # накопичувач рахунку-фактури 
    rahunok_list = []

    dovidniks = get_dovidniks()
    zayavki = get_zayavki()

    for dovidnik in dovidniks:
        
        # робоча змінна
        rahunok_work = rahunok.copy()
        
        rahunok_work['cod of orderer'] = get_cod_of_orderer(dovidnik[0])                                                      #код замовника
        rahunok_work['cod of product'] = dovidnik[0]                                                                          #код товару
        rahunok_work['name'] = dovidnik[1]                                                                                    #назва товару
        rahunok_work['author'] = dovidnik[2]                                                                                  #автор
        rahunok_work['price'] =dovidnik[3]                                                                                   #ціна
        rahunok_work['amount'] = get_amount(dovidnik[0])                                                                      #кількість
        rahunok_work['podatok']  = int(rahunok_work['price']) * int(rahunok_work['amount']) * float(0.2)                   #податок на додану вартість                              
        rahunok_work['total'] =  int(rahunok_work['price']) * int(rahunok_work['amount']) + int(rahunok_work['podatok'])   #сума

        rahunok_list.append(rahunok_work)
       
    
    return rahunok_list

#rahunok = create_analize()

#for item in rahunok:
    #print(item)     