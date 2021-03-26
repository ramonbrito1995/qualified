'''Descrição
Crie quatro funções básicas para simular uma Fila:

cria_fila(): Retorna uma fila vazia.
tamanho(fila): Recebe uma fila como parâmetro e retorna o seu tamanho.
adiciona(fila, valor): Recebe uma fila e um valor como parâmetro, adiciona esse valor na última posição da fila e a retorna.
remove(fila): Recebe uma fila como parâmetro e retorna o valor do início da fila. Se a fila estiver vazia, deve retornar None.
Lembre-se:

A fila funciona seguindo a sequência FIFO(First In First Out) - Primeiro a entrar, primeiro a sair.
Em python, a fila é implementada utilizando a estrutura de uma lista.
Exemplos
Função cria_fila()
Saída: []
Função tamanho(fila)
# minha_fila = [9, 1, 2, 3, 100]
Entrada: minha_fila
Saída: 5
Função adiciona(fila, valor)
# minha_fila = [1, 2, 3]
Entrada: minha_fila, 100
Saída: [1, 2, 3, 100]
Função remove(fila)
# minha_fila = [1, 2, 3]
Entrada: minha_fila
Saída: [2, 3]

# minha_fila = []
Entrada: minha_fila
Saída: None'''



def cria_fila():
    fila = list()
    return fila

def tamanho(fila):
    return len(fila)

def adiciona(fila, valor):
    fila.append(valor)
    return fila

def remove(fila):
    if fila == []:
      return None
    num = fila.pop(0)
    return num
    
print(cria_fila())
print(tamanho([1,2,3,4]))
print(adiciona([1,2,3,4],9))
print(remove([1,2,3]))
 