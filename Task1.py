from random import randint

def generator(amount):
    for n in range(amount):
        a = randint(0,255)
        b = randint(0,255)
        c = randint(0,255)
        d = randint(0,255)
        f = open('ip-addresses.txt', 'a', encoding='utf-8')
        f.write(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+'\n')
        f.close()
    print('Адреса сгенерированы!')

generator(5)
