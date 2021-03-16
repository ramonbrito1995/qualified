def distinct(seq):
    lista_nova = []
    for i in seq:
        if i not in lista_nova:
            lista_nova.append(i)
    return lista_nova

print(distinct([2,4,2,2,7,6,4,9,0])) 