''''Descrição
Utilizando as mesmas 8 funções das atividades Pilha- Funções Básicas e Fila - Funções Básicas:

cria_fila()
tamanho(fila)
adiciona(fila, valor)
remove(fila):
Implemente a função fila_prioridade(lista) que recebe uma lista com números inteiros que representam idades de pessoas. A lista representa a ordem de chegada de cada pessoa. A função deve retornar uma fila que dê prioridade aos idosos.

Pessoas com 65 anos ou mais devem ser colocadas no início da fila, mas respeitando o funcionamento normal da fila (primeiro a entrar, primeiro a sair).

DICA: VOCÊ PODE UTILIZAR MAIS DE UMA FILA PARA RESOLVER O PROBLEMA !

Lembre-se:

A fila funciona seguindo a sequência FIFO(First In First Out) - Primeiro a entrar, primeiro a sair.
IMPORTANTE
É OBRIGATÓRIO utilizar pelo menos as funções cria_fila, adiciona e remove da atividade anterior para implementar a função fila_prioridade. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos
Chamada da função fila_prioridade(lista)
Entrada: [18, 20, 23, 18]
Saída: [18, 20, 23, 18]

Entrada: [18, 23, 65, 89]
Saída: [65, 89, 18, 23]

Entrada: [30, 70]
Saída: [70, 30]

Entrada: []
Saída: []

Entrada: [65, 30, 70, 18, 66]
Saída: [65, 70, 66, 30, 18]'''





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
  
  
def fila_prioridade(lista):
    fila = cria_fila()
    fila_2 = cria_fila()
    for i in lista:
        if i >= 65:
            adiciona(fila,i)
        else:
            adiciona(fila_2,i)
    return fila + fila_2

print(cria_fila())
print(tamanho([1,2,3,4]))
print(adiciona([1,2,3,4],9))
print(remove([1,2,3]))
print(fila_prioridade([23,21,90,89,17,65]))
