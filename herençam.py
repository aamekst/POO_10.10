class Funcionario: 
    def __init__(self, nome, rg, cpf):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf


class Vendedor(Funcionario):
    def __init__(self, nome, rg, cpf, comissao):
        Funcionario.__init__(self,nome, rg, cpf) #obrigatorio coloca a class no lugar do super e self
        self.comissao = comissao
    
    def teste(self):
        print('executou vendendor')

class Gerente(Funcionario):
    def __init__(self, nome, rg, cpf, adicional):
        Funcionario.__init__(self,nome, rg, cpf)
        self.adicional = adicional

    def teste(self):
        print('executou gerente')
    
    def salario(self):
        print('ok')

#class GerenteVendas(Vendedor, Gerente): #herença multipla 
 #   def __init__(self, nome, rg, cpf, comissao, adicional, area):
 #       super().__init__(nome, rg, cpf, comissao) #executar o init da super da primeira class que foi definida no construção, no caso, o vendendor que usuario a comissao que foi o add da class vendedor
 #       self.area =area


class GerenteVendas(Gerente,Vendedor): #herença multipla 
    def __init__(self, nome, rg, cpf, comissao, adicional, area):
        Vendedor.__init__(self, nome, rg, cpf, comissao) #para chama o init as duas classe para ser super, porem não é recomendavel
        Gerente.__init__(self,nome, rg, cpf, adicional)
        self.area =area

    def teste(self):
        Vendedor.teste()
        print('-----------------')#da prioridade 


gv= GerenteVendas('João', '343434', '888888', 505, 150, 'vendas')
gv.teste()
gv.salario()

