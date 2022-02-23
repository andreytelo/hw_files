def write_cookbook():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ingridients_list = []
            for item in range(count):
                ingridient = f.readline().strip()
                ingtidient_split = ingridient.split(' | ')
                ingridients = {'ingridient_name': ingtidient_split[0], 'quantity': int(ingtidient_split[1]),
                               'measure': ingtidient_split[2]}
                ingridients_list.append(ingridients)
            f.readline()
            cook_book[dish_name] = ingridients_list
    return cook_book


def shop_list(dishes, person_count):
    ingridient_list = dict()
    cook_book = write_cookbook()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ingridients in cook_book[dish_name]:
                measure_quantity_list = {}
                if ingridients['ingridient_name'] not in ingridient_list:
                    measure_quantity_list['measure'] = ingridients['measure']
                    measure_quantity_list['quantity'] = ingridients['quantity'] * person_count
                    ingridient_list[ingridients['ingridient_name']] = measure_quantity_list
                else:
                    ingridient_list[ingridients['ingridient_name']]['quantity'] = \
                        ingridient_list[ingridients['ingridient_name']]['quantity'] + \
                        ingridients['quantity'] * person_count

        else:
            print("Такого блюда нет в списке!")
    return ingridient_list


print(write_cookbook())
print(shop_list(['Омлет', 'Омлет'], 2))
