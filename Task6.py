letters = {"а": 0, "б": 0, "в": 0, "г": 0, "д": 0, "е": 0, "ё": 0, "ж": 0, "з": 0, "и": 0, "й": 0, "к": 0, "л": 0,
           "м": 0, "н": 0, "о": 0, "п": 0, "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0,
           "щ": 0, "ъ": 0, "ы": 0, "ь": 0, "э": 0, "ю": 0, "я": 0}
amount_of_letters = 0

line_in_text = 'no'
with open('article_rus.txt', 'r', encoding='utf-8') as f:
    while line_in_text != '':
        line_in_text = f.readline()
        if line_in_text == '':
            break
        else:
            line_in_text.lower()
            for i in range(0, len(line_in_text)):
                if line_in_text[i] in letters:
                    amount_of_letters += 1
                    letters[line_in_text[i]] += 1
    f.close()
for letter in letters:
    letters[letter] /= amount_of_letters
    print("{} : {}".format(letter, round(letters[letter],5)))
