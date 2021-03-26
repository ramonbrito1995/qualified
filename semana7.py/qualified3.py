
'''Descrição
Utilizando as mesmas 4 funções da atividade Pilha - Funções Básicas:

cria_pilha()
tamanho(pilha)
adiciona(pilha, valor)
remove(pilha):
Implemente a função insere_par_remove_impar(lista) que recebe uma lista de números inteiros como parâmetro e retorna uma pilha de acordo com a seguinte regra: para cada elemento da lista, se o número for par, deve ser inserido na pilha. Caso contrário, deve ser removido.

0 deve ser considerado par.

Utilize o funcionamento da pilha para que isso aconteça.

Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
IMPORTANTE
É OBRIGATÓRIO utilizar pelo menos as funções cria_pilha, adiciona e remove da atividade Pilha - Funções Básicas para implementar a função insere_par_remove_impar. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos
Chamada da função insere_par_remove_impar(lista)
Entrada: [1, 2, 3]
Saída: []

Entrada: [1, 2, 3, 4]
Saída: [4]

Entrada: []
Saída: []

Entrada: [1]
Saída: []

Entrada: [2, 2, 2, 2, 1, 1, 1]
Saída: [2]

Entrada: [1, 2, 3, 4, 6, 8]
Saída: [4, 6, 8]'''




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
  
def inverte_texto(texto):
  novo_texto = cria_pilha()
  if texto == "":
    return ""
  if len(texto) == 1:
    return ""
  for i in range(len(texto),0,-1):
         adiciona(novo_texto,remove(list(texto[i - 1])))
  
  x = ""
  for i in novo_texto:
          x += i

  

  return x

        
print(cria_pilha())
print(tamanho([1,2,3,4]))
print(adiciona([1,2,3,4],9))
print(remove([1,2,3]))
print(inverte_texto("Atbd"))