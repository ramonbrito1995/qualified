class Pessoa:
    def __init__(self,nome,rg,pai=None,mae=None):
        self.nome = nome
        self.rg = rg
        self.pai = pai
        self.mae = mae


p = Pessoa("Naruto","11123223")
print(p.nome,p.rg,p.pai,p.mae)

