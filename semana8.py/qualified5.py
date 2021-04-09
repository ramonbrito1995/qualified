'''Descrição
Implemente a função balanceado(texto) que recebe uma string contendo uma série de parênteses - ( e ) - e retorna se os parênteses estão balanceados ou não.

A função deve dizer se todos os parênteses que são abertos possuem um correspondente para fechá-los.

Existem várias formas de implementar esta função. Tente utilizar o conhecimento adquirido até sobre todas as estruturas de dados para pensar numa boa solução.

Não há restrição em relação às ferramentas da linguagem que podem ser utilizadas.

Exemplos
Chamada da função balanceado(texto)
Entrada: "(2+3+4) * 3"
Saída: True

Entrada: "(()))"
Saída: False

Entrada: "((())"
Saída: False

Entrada: "("
Saída: False

Entrada: "2 + 3"
Saída: True

Entrada: "(a / 2) * ((3 * 1) / 9)"
Saída: True

Entrada: ""
Saída: True'''








def balanceado(texto):
    p_1 = list()
    p_2 = list()
    if texto == []:
        return True
    elif texto[0] == ")":
        return False
    else:
        for i in texto:
            if i == "(":
                p_1.append(i)
            elif i == ")":
                p_2.append(i)
            else:
                continue
        resposta = False
        if len(p_1) == len(p_2):
            resposta = True
        return resposta
   

print(balanceado("(s))"))