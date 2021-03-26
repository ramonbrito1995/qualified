'''Descrição
Utilizando as mesmas 4 funções da atividade Pilha - Funções Básicas:

cria_pilha()
tamanho(pilha)
adiciona(pilha, valor)
remove(pilha):
Implemente a função inverte_texto(texto) que recebe um texto(string) como parâmetro e retorna seu conteúdo invertido.

Utilize o funcionamento da pilha para que isso aconteça.

Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
IMPORTANTE
É OBRIGATÓRIO utilizar pelo menos as funções cria_pilha, adiciona e remove da atividade anterior para implementar a função inverte_texto. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos
Chamada da função inverte_texto(texto)
Entrada: "abc"
Saída: "cba"

Entrada: ""
Saída: ""

Entrada: "a"
Saída: ""

Entrada: "aAbA"
Saída: "AbAa"'''

















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
    return pilha.pop()
 
def insere_par_remove_impar(lista):
    pilha = cria_pilha()
    for i in lista:
        if i%2 == 0:
            adiciona(pilha,i)
        else:
            remove(pilha)
    
    return pilha
  
  
  
print(cria_pilha())
print(tamanho([1,2,3,4]))
print(adiciona([1,2,3,4],9))
print(remove([1,2,3]))
print(insere_par_remove_impar([1,3,5]))