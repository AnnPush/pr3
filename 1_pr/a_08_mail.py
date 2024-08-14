#Реализуйте функцию normalize_url(), которая выполняет нормализацию данных. Она принимает адрес
#сайта и возвращает его с https:// в начале.
Функция принимает адреса в виде АДРЕС или http://АДРЕС, но всегда возвращает адрес
#в виде https://АДРЕС. На вход функции также может поступить адрес в уже нормализованном
#виде https://АДРЕС, в этом случае ничего менять не надо.
def normalize_url(url):
    prefix = 'https://'
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == 'http://':
            return prefix + url[7:]
        else:
            return prefix + url
Второе решение:
def normalize_url(text):
    if text[:7] == 'http://':
        text1 = 'https://' + text[7:]
    else:
         if text[:8] != 'https://':
             text1 = 'https://' + text
         else:
            text1 = text
    return text1
