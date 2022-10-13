letters = {"а": 0, "б": 0, "в": 0, "г": 0, "д": 0, "е": 0, "ё": 0, "ж": 0, "з": 0, "и": 0, "й": 0, "к": 0, "л": 0,
           "м": 0, "н": 0, "о": 0, "п": 0, "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0,
           "щ": 0, "ъ": 0, "ы": 0, "ь": 0, "э": 0, "ю": 0, "я": 0}  # словарь букв
amount_of_letters = 0  # количество букв всего

line_in_text = 'no'  # строка
with open('article_rus.txt', 'r', encoding='utf-8') as f:
    while line_in_text != '':  # до тез пор пока строка не пустая
        line_in_text = f.readline()  # считываем новую
        if line_in_text == '':  # если пустая выходим из цикла
            break
        else:
            line_in_text.lower()  # если нет, делаем ее маленькой
            for i in range(0, len(line_in_text)):  # для каждого символа
                if line_in_text[i] in letters:  # проверяем есть ли он в словаре
                    amount_of_letters += 1  # если да увеличиваем количество всех букв
                    letters[line_in_text[i]] += 1  # и конкретно количество каждой
    f.close()

for letter in letters:
    letters[letter] /= amount_of_letters

sorted_values=sorted(letters.values(), reverse=True)

new_sorted_letters={}
for i in sorted_values:
    for k in letters.keys():
        if letters[k]==i:
            new_sorted_letters[k]=letters[k]
            break
print(new_sorted_letters)

with open('article_rus_solve.txt', 'w', encoding='utf-8') as f:
    for letter in new_sorted_letters:
        f.write("{} : {}".format(letter, round(new_sorted_letters[letter], 5)) + '\n')
    f.close()
