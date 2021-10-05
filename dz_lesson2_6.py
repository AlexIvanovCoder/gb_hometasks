##### 6 
products_lst = []

i = 1 # для цикла загрузки товаров

print('введите параметры продуктов:')

while 1 == 1: # бесконечный цикл
    print('------------')
    print(f'продукт {i}')
    print('------------')
    nm = input("название: ")
    prc = int(input("цена: "))
    qnt = int(input("количество: "))
    qnt2 = input("ед: ")
    
    products_lst.append((i, {"название": nm
                             , "цена": prc
                             , "количество": qnt
                             , "ед": f'{qnt2} шт.'
                            }
                                )
                                   )
    one_more = input("ещё 1 товар?")
    if one_more == "да":
        i += 1
    else:
        break

#структура финальной аггрегированного словаря
lst_of_items = ["название", "цена", "количество", "ед"]
#аггрегированный словарь
aggr_list = {}

for i in lst_of_items: #определяем категорию элемента
    for j in products_lst: #берем значение категории
        #print(j[1][i])
        if i not in aggr_list.keys():
            aggr_list[i] = [j[1][i]] #если категория не существует, создаем
        else: #иначе, добавляем в уже существующую
            aggr_list[i].append(j[1][i])
        
print(aggr_list)