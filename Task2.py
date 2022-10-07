import ipaddress
import random


def printList(flist): #функция для печати списка
    for i in range(0, len(flist)):
        print(flist[i])

def generator(amount): #генерация айпи адресов
    MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
    for n in range(amount):
        ip = ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4)) #генерируем адрес
        with open ('ip.log', 'a', encoding='utf-8') as f:
            f.write(str(ip)+'\n') #выводим в файл
        f.close()
    print('Адреса сгенерированы!')

def createMask(): #создание маски
    fmask=[]
    a = -1
    b = -1
    c = -1
    d = -1
    print('Ведите маску подсети.')
    while True: #ввод с клавиатуры с проверкой
        try:
            while (a < 0 or b < 0 or c < 0 or d < 0 or a > 255 or b > 255 or c > 255 or d > 255):
                a, b, c, d = map(int, input(
                    'Маска подсети записывается четырьмя цифрами от 0 до 255 разделенными точками: ').split('.'))
            fmask.append(a)
            fmask.append(b)
            fmask.append(c)
            fmask.append(d)
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")
        except Exception:
            print("Вы ввели не верно. Попробуйте снова: ")
    return fmask

def getNetworkAdress(fipadresses,fmasks): #получаем сатавой адрес
    for i in range(0,len(fipadresses)):
        fipadresses[i][3]=fmasks[0][3] #заменям последнюю цифру в айпи адресе на последнюю в маске
        fipadresses[i][2]=int(format(fipadresses[i][2], "08b")) #предпоследнюю переводим в двоичную
        fipadresses[i][2]=(fipadresses[i][2]//10)*10+(int(format(fmasks[0][2], "08b")))%10 #меняем в ней последний знак на такой же как в двоичной форме маски
        fipadresses[i][2]=int(str(fipadresses[i][2]), 2) #переводим обратно в десятичную
    return fipadresses
  

mask=[] #маска подсети
ipadresses=[] #список айпи адресов
networkaddress =[] #список адресов сети

generator(5) #генерация айпи адресов в файл
endoffile='no'
with open ('ip.log', 'r', encoding='utf-8') as f: #открываем файл
    while endoffile!='':
        endoffile=f.readline()#считываем айпи адрес
        if endoffile=='': #как только пустая строка
            break #выходим из цикла
        ipadresses.append(list(map(int,endoffile.split('.')))) #записываем в список
    f.close()

print("АйПи адреса:\n")
printList(ipadresses) #печать айпи адресов

mask.append(createMask()) #считываем маску

#printList(masks) # вывод введеной маски

networkaddress=getNetworkAdress(ipadresses,mask) #получаем сетевые адреса
#print("Адреса сети:")
#printList(networkaddress) #вывод на консоль

with open('ip_solve.log', 'a', encoding='utf-8') as f: #записываем их в файл
    for i in range(len(networkaddress)):
        f.write(str(networkaddress[i][0]) + '.')
        f.write(str(networkaddress[i][1]) + '.')
        f.write(str(networkaddress[i][2]) + '.')
        f.write(str(networkaddress[i][3]) + '\n')
    f.close()
print('Сетевые адреса записаны в файл!')
