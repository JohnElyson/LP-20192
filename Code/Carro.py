from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,placa):
        self.setPlaca(placa)
        self.rodas = []
        self.setMaxRodas(4)
    
    def getMaxRodas(self):
        return self.maxRodas

    def setMaxRodas(self,maxRodas):
        self.maxRodas = maxRodas
        
    def addRoda(self,roda):
        if self.getNumRodas() <= self.maxRodas():
            self.rodas.append(roda)
