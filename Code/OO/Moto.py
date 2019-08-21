from Veiculo import Veiculo 

class Moto(Veiculo):

    def __init__(self,placa):
        self.setPlaca(placa)
        self.rodas = []
        self.setMaxRodas(2)
        self.setTipoVeiculo("Moto")
    
    def getMaxRodas(self):
        return self.maxRodas

    def setMaxRodas(self,maxRodas):
        self.maxRodas = maxRodas
    
    def addRoda(self,roda):
        if self.getNumRodas() <= self.getMaxRodas():
            self.rodas.append(roda)

    def setTipoVeiculo(self,tipoVeiculo):
        self.tipoVeiculo = tipoVeiculo

    def getTipoVeiculo(self):
        return self.tipoVeiculo
