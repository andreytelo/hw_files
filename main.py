import os


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


def write_file():
    note1 = '1.txt'
    note2 = '2.txt'
    note3 = '3.txt'
    os.chdir('sorted')
    new_file = "write_file.txt"
    file1_path = os.path.join(os.getcwd(), note1)
    file2_path = os.path.join(os.getcwd(), note2)
    file3_path = os.path.join(os.getcwd(), note3)
    with open(file1_path, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open(file2_path, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
    with open(file3_path, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()

    with open(new_file, 'w', encoding='utf-8') as f_total:
        if len(file1) < len(file2) and len(file1) < len(file3):
            f_total.write(note1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
            f_total.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
            f_total.write(note2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
            f_total.write('\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
            f_total.write(note3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
            f_total.write('\n')

        if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
            f_total.write(note1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
            f_total.write('\n')
        elif len(file1) > len(file2) > len(file3) or len(file1) < len(file2) < len(file3):
            f_total.write(note2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
            f_total.write('\n')
        elif len(file1) > len(file3) > len(file2) or len(file1) < len(file3) < len(file2):
            f_total.write(note3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
            f_total.write('\n')

        if len(file1) > len(file2) and len(file1) > len(file3):
            f_total.write(note1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
            f_total.write('\n')
        elif len(file2) > len(file1) and len(file2) > len(file3):
            f_total.write(note2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
            f_total.write('\n')
        elif len(file3) > len(file1) and len(file3) > len(file2):
            f_total.write(note3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
            f_total.write('\n')


print(write_cookbook())
print(shop_list(['Омлет', 'Омлет'], 2))
write_file()