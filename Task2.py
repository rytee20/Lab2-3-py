import ipaddress
import random


def print_list(f_list):  # функция для печати списка
    for i in range(0, len(f_list)):
        print(f_list[i])


def generator(amount):  # генерация айпи адресов
    MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
    for n in range(amount):
        ip = ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))  # генерируем адрес
        with open('ip.log', 'a', encoding='utf-8') as f:
            f.write(str(ip) + '\n')  # выводим в файл
        f.close()
    print('Адреса сгенерированы!')


def create_mask():  # создание маски
    f_mask = []
    a = -1
    b = -1
    c = -1
    d = -1
    print('\nВедите маску подсети.')
    while True:  # ввод с клавиатуры с проверкой
        try:
            while a < 0 or b < 0 or c < 0 or d < 0 or a > 255 or b > 255 or c > 255 or d > 255:
                a, b, c, d = map(int, input(
                    'Маска подсети записывается четырьмя цифрами от 0 до 255 разделенными точками: ').split('.'))
            f_mask.append(a)
            f_mask.append(b)
            f_mask.append(c)
            f_mask.append(d)
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")
        except Exception:
            print("Вы ввели не верно. Попробуйте снова: ")
    return f_mask


def get_network_adress(f_ip_adress, f_masks):  # получаем сатавой адрес
    return str(f_ip_adress[0]&f_masks[0][0])+'.'+str(f_ip_adress[1]&f_masks[0][1])+'.'+str(f_ip_adress[2]&f_masks[0][2])+'.'+str(f_ip_adress[3]&f_masks[0][3])


mask = []  # маска подсети
ip_adresses = []  # список айпи адресов
network_address = []  # список адресов сети

generator(5)  # генерация айпи адресов в файл
end_of_file = 'no'
with open('ip.log', 'r', encoding='utf-8') as f:  # открываем файл
    while end_of_file != '':
        end_of_file = f.readline()  # считываем айпи адрес
        if end_of_file == '':  # как только пустая строка
            break  # выходим из цикла
        ip_adresses.append(list(map(int, end_of_file.split('.'))))  # записываем в список
    f.close()

print("АйПи адреса:")
print_list(ip_adresses)  # печать айпи адресов

mask.append(create_mask())  # считываем маску

for i in range(0, len(ip_adresses)):

    network_address.append(get_network_adress(ip_adresses[i], mask))  # получаем сетевые адреса

with open('ip_solve.log', 'w', encoding='utf-8') as f:  # записываем их в файл
    for i in range(len(network_address)):
        f.write(str(network_address[i]) + '\n')
    f.close()
print('Сетевые адреса записаны в файл!')
