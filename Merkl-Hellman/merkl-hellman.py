# Найти открыть ключ и зашифровать слово "why"

def find_key(inc_list, q, r):
    result = []
    for w in inc_list:
        result.append( (r*w) % q)
    return result

def encrypt(message, key):
    #for char in message:
     #   m = format(char, 'b')
    print(list(format(25, 'b')))

if __name__ == '__main__':
    key = find_key([2, 3, 7, 15, 31], 61, 17)
    print(key)
    print(encrypt("why", key))
