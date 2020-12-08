"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

def get_dovidniks():
    """ повертає список довідника товарів, який отримує ззовні

    Returns:
        dovidniks_list: список довідника
    """    

    with open("./data/dovidniks.txt", encoding="utf-8") as dovidniks_file:
        from_file = dovidniks_file.readlines()

    # накопічувач довідника товарів
    dovidniks_list = []

    for line in from_file:
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        dovidniks_list.append(line_list)
    
    return dovidniks_list

def show_dovidniks(dovidniks):
    """виводить на екран список довідника товарів заданого діапазона

    Args:
        dovidniks ([list]): список довідника товарів
    """

    dovidnik_code_from = input("З якого коду? ")
    dovidnik_code_to   = input("По який код? ") 

    for dovidnik in dovidniks:
        if  dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to: 
            print("код: {}; назва: {}; автор: {}; ціна: {} грн.".format(dovidnik[0], dovidnik[1], dovidnik[2], dovidnik[3]))

#dovidniks = get_dovidniks()
#show_dovidniks(dovidniks)