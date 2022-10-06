import ipaddress
import random

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1

def generator(amount):
    for n in range(amount):
        ip = ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
        f = open('ip.log', 'a', encoding='utf-8')
        f.write(str(ip)+'\n')
        f.close()
    print('Адреса сгенерированы!')

generator(5)
