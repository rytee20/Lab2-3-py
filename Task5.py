import os


if os.path.exists("example"): #работаем только если есть папка
    left=-1
    while True: #ввод с клавиатуры с проверкой левой границы
        try:
            while (left<1 or left>100):
                    left=int(input("Введите левую границу: "))
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")
        except Exception:
            print("Вы ввели не верно. Попробуйте снова: ")

    right=-1
    while True: #ввод с клавиатуры с проверкой правой границы
        try:
            while (right<1 or right>100 or right<left):
                    right=int(input("Введите правую границу: "))
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")
        except Exception:
            print("Вы ввели не верно. Попробуйте снова: ")

    for i in range(0,100):
        if os.path.exists("example/examplefile"+str(i)): #еси есть файл
            if (os.path.getsize("example/examplefile"+str(i))//1024)>=left and (os.path.getsize("example/examplefile.txt"+str(i))//1024) <= right: #если его размер лежит в диапазоне
                print("example/examplefile"+str(i)+"\n") #выводим
else: #если папки нет
    print("Папки example не существует")
