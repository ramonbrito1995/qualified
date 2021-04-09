'''Descrição
Utilizando a classe Pessoa criada na atividade Parentesco entre Pessoas, crie a função encontre_os_irmaos(lista_pessoas) que recebe uma lista de objetos do tipo Pessoa e retorna uma lista apenas com o nome das pessoas que são irmãos.

Se não houver irmãos na lista, a lista retornada deve ser vazia ([]).

Lembre-se que a mesma pessoa não pode aparecer mais de uma vez na lista final.

Exemplos
p1 = Pessoa("Sasuke", "222222")
p2 = Pessoa("Itachi", "202020")
p3 = Pessoa("Mikoto", "444444")
p4 = Pessoa("Fugaku", "333333")

# Adiciona pai e mãe de p1
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Adiciona pai e mãe de p2
p2.adiciona_mae(p3)
p2.adiciona_pai(p4)

[lista_pessoas = p1, p2]

# Exemplo e chamada da função
encontre_os_irmaos(lista_pessoas)
# Exemplo da saída esperada: ["Sasuke", "Itachi"]
p1 = Pessoa("Pessoa 1", "222222")
p2 = Pessoa("Pessoa 2", "202020")
p3 = Pessoa("Pessoa 3", "444444")
p4 = Pessoa("Pessoa 4", "333333")
p5 = Pessoa("Pessoa 5", "555555")

# Adiciona pai e mãe de p1
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Adiciona pai e mãe de p5
p5.adiciona_mae(p3)
p5.adiciona_pai(p4)

lista_pessoas = [p1, p2, p5]

# Exemplo e chamada da função
encontre_os_irmaos(lista_pessoas)
# Exemplo da saída esperada: ["Pessoa 1", "Pessoa 5"]
p1 = Pessoa("Pessoa 1", "222222")
p2 = Pessoa("Pessoa 2", "202020")
p3 = Pessoa("Pessoa 3", "444444")
p4 = Pessoa("Pessoa 4", "333333")
p5 = Pessoa("Pessoa 5", "555555")

lista_pessoas = [p1, p2, p3, p4, p5]

# Exemplo e chamada da função
encontre_os_irmaos(lista_pessoas)
# Exemplo da saída esperada: []'''





class Pessoa:
    def __init__(self,nome,rg,pai=None,mae=None):
        self.nome = nome
        self.rg = rg
        self.pai = pai
        self.mae = mae


    def adiciona_pai(self,nome_pai):
        self.pai = nome_pai
        return self.pai

    def adiciona_mae(self,nome_mae):
        self.mae = nome_mae
        return self.mae

    def eh_mesma_pessoa(self,Pessoa):
        if self.nome == Pessoa.nome and self.rg == Pessoa.rg and self.mae == Pessoa.mae:
            return True
        elif self.nome == Pessoa.nome and self.rg == Pessoa.rg and self.mae == None:
            return True
        else:
            return False  
            
    def eh_antecessor_direto(self,Pessoa):
        if self.mae == Pessoa or self.pai == Pessoa:
            return True 
        else:
            return False 

    def eh_irmao(self,Pessoa):
        if self.mae == Pessoa.mae and self.pai == Pessoa.pai:
            return True 
        else:
            return False 
    
def encontre_os_irmaos(lista_pessoas):
    lista = lista_pessoas
    irmaos = []
    print([i.nome for i in lista])
    for i in lista:
      for j in lista:
         if i.eh_irmao(j) and i.nome != j.nome and i.mae is not None:
               irmaos.append(i.nome)
           
              
              
                                    


    return irmaos
   


p1 = ("Ramon","1273663")
p2 = ("Bruno","26263563")
p1.adiciona_pai(p1)
lista = [p1,p2,p3]
print(encontre_os_irmaos(lista))