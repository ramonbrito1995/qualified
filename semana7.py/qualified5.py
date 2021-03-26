'''Descrição
Utilizando as mesmas 4 funções da atividade Pilha - Funções Básicas:

cria_pilha()
tamanho(pilha)
adiciona(pilha, valor)
remove(pilha):
Implemente a função palindromo(texto) que recebe um texto(string) como parâmetro e retorna True se o texto é um palíndromo ou False caso contrário.

Um palíndromo é um texto que pode ser lido tanto da esquerda pra direita quanto da direita pra esquerda, contendo o mesmo conteúdo.

Exemplos: arara, ama, abba, ...

Utilize o funcionamento da pilha para que isso aconteça.

Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
IMPORTANTE
É OBRIGATÓRIO utilizar pelo menos as funções cria_pilha, adiciona e remove da atividade anterior para implementar a função palindromo. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos
Chamada da função palindromo(texto)
Entrada: "arara"
Saída: True

Entrada: ""
Saída: True

Entrada: "a"
Saída: True

Entrada: "aAbA"
Saída: False

Entrada: "acac"
Saída: False'''














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
  
def palindromo(s):
  novo_texto = cria_pilha()
  if s == "":
    return True
  if len(s) == 1:
    return ""
  for i in range(len(s),0,-1):
         adiciona(novo_texto,remove(list(s[i - 1])))
  
  x = ""
  for i in novo_texto:
          x += i

  if s == x :
      return True

  else:
      return False

print(cria_pilha())
print(tamanho([1,2,3,4]))
print(adiciona([1,2,3,4],9))
print(remove([1,2,3]))
print(palindromo("aja"))