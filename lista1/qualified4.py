def reverse_string(string):
    lista = list()
    for i in range(0,len(string)):
        lista.append(string[i])
    
    invert = list(reversed(lista))
    return ''.join(invert)

    
print(reverse_string("abc123"))