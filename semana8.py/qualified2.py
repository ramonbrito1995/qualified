'''Descrição
Nesta atividade você deve criar uma classe simples chamada Pessoa com o mesmos atributos da atividade anterior Pessoa, mas adicionando 2 métodos:

Atributos

nome
rg
pai
mae

Métodos

adiciona_pai
adiciona_mae
O método adiciona_pai deve receber um objeto do tipo Pessoa e atribuí-lo ao atributo pai do objeto que invocou o método.
O método adiciona_mae deve receber um objeto do tipo Pessoa e atribuí-lo ao atributo mae do objeto que invocou o método.

Exemplos:
p = Pessoa("Naruto", "111111")
p2 = Pessoa("Minato", "010101")
p3 = Pessoa("Kushina", "020202")
p.adiciona_pai(p2)
p.adiciona_mae(p3)

p.pai.nome --> "Minato"
p.mae.nome --> "Kushina"'''




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


p = Pessoa("Naruto","11123223")
print(p.nome,p.rg,p.pai,p.mae)
p.adiciona_pai("Ramon")
p.adiciona_mae("Benedita")
print(p.nome,p.rg,p.pai,p.mae)