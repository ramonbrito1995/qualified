def complete_series(seq): 
    lista_nova = []
    for i in seq:
        if i not in lista_nova:
            lista_nova.append(i)
        else:
            lista_nova.clear()
            lista_nova = [0]
            break
    for c in range(0,max(lista_nova)):
        if c not in lista_nova:
            lista_nova.append(c)
        else:
            continue
    
    
    lista_nova.sort()
    return lista_nova

print(complete_series([1,2,8,4]))
