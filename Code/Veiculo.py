from Roda import Roda

class Veiculo():
    def __init__(self,placa):
        self.setPlaca(placa)
        self.rodas = []

    def addRoda(self,roda):
        self.rodas.append(roda)

    def getRodas(self):
        return self.rodas

    def getNumRodas(self):
        """
            Retorna o número de rodas atuais no veículo
        """
        return len(self.rodas)

    def setPlaca(self,placa):
        self.placa = placa
		
    def getPlaca(self):
        return self.placa
