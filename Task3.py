import csv

def sort_key(key): #ключ для сортировки
    return key['Количество побед']

def printList(flist): #функция для печати списка
    for i in range(0, len(flist)):
        print(flist[i])

def sortByThird(fparticipants): #сортировка по дополнительным баллам методом камня
    for i in range(len(fparticipants)-1):
        for j in range(len(fparticipants)-i-1):
            if fparticipants[j]['Количество побед']==fparticipants[j+1]['Количество побед'] and fparticipants[j]['Доп. показатель'] < fparticipants[j + 1]['Доп. показатель']:
                fparticipants[j], fparticipants[j + 1] = fparticipants[j + 1], fparticipants[j]
    return fparticipants


participants=[] #участники
winners=[] #результаты
heading='' #заголовок
endoffile='no' #конец строки
raiting=1 #призовые места


with open('players.csv', encoding='utf-8') as r_file: #считываем содеримое файла
    file_reader = csv.DictReader(r_file, delimiter = ";")
    participants=list(file_reader) #преобразовываем в лист

printList(participants) #печатаем участников для проверки

#for i in range(0,len(participants)): #преобразоваваем победы и дополнительные баллы в int из str
 #   participants[i]['Количество побед']=int(participants[i]['Количество побед'])
 #   participants[i]['Доп. показатель']=int(participants[i]['Доп. показатель'])

participants.sort(key=sort_key,reverse=True) #сортируем по победам
printList(participants) #вывод для проверки
participants=sortByThird(participants) #сортируем по дополнительным очкам
printList(participants) #вывод для проверки

for i in range(len(participants)): #формеруем список результатов
    if i == 0:  # если участник первый в списке
        winners.append({'Спортсмен': participants[i]['Спортсмен'], 'Место': raiting}) # то записываем его на первное место
    else:
        if participants[i]['Количество побед'] == participants[i - 1]['Количество побед'] and participants[i]['Доп. показатель'] == participants[i - 1][
            'Доп. показатель']:  # если у текущего участника и предыдущго совпадают победы и доп баллы
            winners.append({'Спортсмен': participants[i]['Спортсмен'], 'Место': raiting})  # то записываем текущего участника с таким же местом как у предыдущего
        else:
            if participants[i]['Количество побед'] == participants[i - 1]['Количество побед'] and participants[i]['Доп. показатель'] != participants[i - 1][
                'Доп. показатель']:  # если у учатника текущего и предыдущего совпадают победы но разные доп баллы
                raiting=raiting+1  # прибавляем место
                winners.append({'Спортсмен': participants[i]['Спортсмен'], 'Место': raiting})  # записываем его со следующим местом
            else:  # если вообще ничего не совпадает
                raiting=raiting+1
                winners.append({'Спортсмен': participants[i]['Спортсмен'], 'Место': raiting})  # и записываем

printList(winners) #печатаем для проверки

details = ['Спортсмен', 'Место'] #заголовок
with open("results.csv", "w", newline="") as f: #записываем результаты
    write = csv.DictWriter(f, fieldnames=details, delimiter = ";")
    write.writeheader()
    write.writerows(winners)

print('Результаты совервнований записаны в файл!')
