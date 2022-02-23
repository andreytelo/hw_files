import os

dct = {}

def test_read():
    a = os.listdir()

    for i in a:
        if '.txt' in i:
            with open(i, encoding='utf-8') as read_list:
                dct[i] = read_list.readlines()


def get_key(key, value):
    for k, v in key.items():
        if v == value:
            return k


def test_write():
    sort = sorted(dct.values(), reverse=True)
    with open('new_file.txt', 'w', encoding='utf-8') as ff:
        counter = 0
        for i in sort:
            ff.write(str(get_key(dct, i)))
            ff.write('\n')
            ff.write(str(len(sort[counter])))
            ff.write('\n')
            ff.write(str('\n'.join(dct[get_key(dct, i)])))
            ff.write('\n')
            counter += 1


test_read()
test_write()
