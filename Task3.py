from operator import itemgetter


def sort_key(e): #ключ для сортировки
    return e[1]

def printList(flist): #функция для печати списка
    for i in range(0, len(flist)):
        print(flist[i])

def sortByThird(fparticipants): #сортировка по дополнительным баллам методом камня
    for i in range(len(fparticipants)-1):
        for j in range(len(fparticipants)-i-1):
            if fparticipants[j][1]==fparticipants[j+1][1] and fparticipants[j][2] < fparticipants[j + 1][2]:
                fparticipants[j], fparticipants[j + 1] = fparticipants[j + 1], fparticipants[j]
    return fparticipants


participants=[] #участники
heading='' #заголовок
endoffile='no' #конец строки
raiting=1 #призовые места

with open ('players.csv', 'r', encoding='utf-8') as f: #открываем файл
    heading=f.readline() #считываем заголовок
    while endoffile!='':
        endoffile=f.readline()#считываем участника
        if endoffile=='': #как только пустая строка
            break #выходим из цикла
        participants.append(list(map(str,endoffile.split(';')))) #записываем в список
f.close()

printList(participants) #печатаем участников для проверки

for i in range(0,len(participants)): #преобразоваваем победы и дополнительные баллы в int из str
    participants[i][1]=int(participants[i][1])
    participants[i][2]=int(participants[i][2])

participants.sort(key=sort_key,reverse=True) #сортируем по победам
printList(participants) #вывод для проверки
participants=sortByThird(participants) #сортируем по дополнительным очкам
printList(participants) #вывод для проверки 

with open('results.csv', 'a', encoding='utf-8') as f: #записываем результаты в файл
    f.write('Спортсмен;Место\n') #заголовок
    for i in range(len(participants)):
        if i==0: # если участник первый в списке
            f.write(str(participants[i][0]) + ';' + str(raiting) + '\n') #то записываем его на первное место
        else:
            if participants[i][1]==participants[i-1][1] and participants[i][2]==participants[i-1][2]: #если у текущего участника и предыдущго совпадают победы и доп баллы
                f.write(str(participants[i][0]) + ';' + str(raiting) + '\n') #то записываем текущего участника с таким же местом как у предыдущего
            else:
                if participants[i][1]==participants[i-1][1] and participants[i][2]!=participants[i-1][2]: #если у учатника текущего и предыдущего совпадают победы но разные доп баллы
                    raiting=raiting+1 #прибавляем место
                    f.write(str(participants[i][0]) + ';' + str(raiting) + '\n') #записываем его со следующим местом
                else: #если вообще ничего не совпадает
                    raiting = raiting + 1 #прибавляем место
                    f.write(str(participants[i][0]) + ';' + str(raiting) + '\n') #и записываем
    f.close()
print('Результаты совервнований записаны в файл!')
