'''Descrição
Nesta atividade você deve criar uma classe simples chamada Pessoa com o mesmos atributos da atividade anterior Pessoa com Pai e Mãe, mas adicionando mais 3 métodos:

Atributos

nome
rg
pai
mae

Métodos

adiciona_pai - já feito na atividade anterior
adiciona_mae - já feito na atividade anterior
eh_mesma_pessoa
eh_antecessor_direto
eh_irmao
O método eh_mesma_pessoa deve receber um objeto do tipo Pessoa como parâmetro e:

retornar True se as pessoas tiverem o mesmo rg, mesmo nome e mesma mãe*
retornar True se uma das pessoas não tiver mãe, mas nome e rg são iguais
retornar False em qualquer outro caso
* Para saber se é a mesma mãe, deve-se comprar o RG e nome da mãe também.

O método eh_antecessor_direto deve receber um objeto do tipo Pessoa como parâmetro e retornar True se o objeto recebido é pai OU mãe do objeto que invocou o método.

O método eh_irmao deve receber um objeto do tipo Pessoa como parâmetro e retornar True se as pessoas possuem um antecessor em comum. Caso contrário, retornará False.

Exemplos:
p1 = Pessoa("Sasuke", "222222")
p2 = Pessoa("Itachi", "202020")

p1.eh_mesma_pessoa(p1) --> True
p1.eh_mesma_pessoa(p2) --> False

p3 = Pessoa("Mikoto", "444444")
p4 = Pessoa("Fugaku", "333333")

# Adiciona pai e mãe de p1
p1.adiciona_mae(p3)
p1.adiciona_pai(p4)

# Verifica se as pessoas são antecessoras de p1
p1.eh_antecessor_direto(p3) --> True
p1.eh_antecessor_direto(p4) --> True
p1.eh_antecessor_direto(p2) --> False

# Adiciona pai e mãe de p2
p2.adiciona_mae(p3)
p2.adiciona_pai(p4)

# Verifica se p2 é irmão de p1
p1.eh_irmao(p2) --> True
p1.eh_irmao(p4) --> False'''






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



p = Pessoa("Naruto","11123223","Ramon","Benedita")
p1 = Pessoa("Naruto","11123223","Bruno","Maressa")
print(p.nome,p.rg,p.pai,p.mae)
print(p.nome,p.rg,p.pai,p.mae)
print(p.eh_mesma_pessoa(p1))
print(p.eh_antecessor_direto(p1))