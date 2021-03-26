'''Descrição
Crie quatro funções básicas para simular uma Pilha:

cria_pilha(): Retorna uma pilha vazia.
tamanho(pilha): Recebe uma pilha como parâmetro e retorna o seu tamanho.
adiciona(pilha, valor): Recebe uma pilha e um valor como parâmetro, adiciona esse valor na pilha e a retorna.
remove(pilha): Recebe uma pilha como parâmetro e retorna o valor no topo da pilha. Se a pilha estiver vazia, deve retornar None.
Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
Exemplos
Função cria_pilha()
Saída: []
Função tamanho(pilha)
# minha_pilha = [9, 1, 2, 3, 100]
Entrada: minha_pilha
Saída: 5
Função adiciona(pilha, valor)
# minha_pilha = [1, 2, 3]
Entrada: minha_pilha, 100
Saída: [1, 2, 3, 100]
Função remove(pilha)
# minha_pilha = [1, 2, 3]
Entrada: minha_pilha
Saída: [1, 2]

# minha_pilha = []
Entrada: minha_pilha
Saída: None'''

def cria_pilha():
    pilha = list()
    return pilha

def tamanho(pilha):
    return len(pilha)

def adiciona(pilha, elemento):
    pilha.append(elemento)
    return pilha

def remove(pilha):
    if pilha == []:
      return None
    num = pilha.pop()
    return num
  
print(cria_pilha())
print(tamanho([1,2,3,4]))
print(adiciona([1,2,3,4],9))
print(remove([1,2,3]))
 