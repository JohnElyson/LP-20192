from Carro import Carro
from Moto import Moto
from Roda import Roda

lstVeiculos = []


def listaVeiculos(lstVeiculos):
    print("Veiculos existentes:")
    for veiculo in lstVeiculos:
        print()
        print("-"*15)
        print()
        print((lstVeiculos.index(veiculo)+1), " - ", veiculo.getPlaca()) 
        print("Quantidade de rodas: ", veiculo.getNumRodas())
        print()
        print("-"*15)
        print()
        

def criaVeiculos(qtd,tipo):
        for i in range(qtd):
                if tipo.lower() == 'carro':
                    carro = Carro("kkk-0123")
                    for i in range(carro.getMaxRodas()):
                        roda = Roda(14)
                        carro.addRoda(roda)
                        lstVeiculos.append(carro)
                elif tipo.lower() == 'moto':
                    moto = Moto("abc-0022")
                    for i in range(moto.getMaxRodas()):
                        roda = Roda(14)
                        carro.addRoda(roda)
                    lstVeiculos.append(moto)
                        
                else:
                        pass
        listaVeiculos(lstVeiculos)

while True:
    print("Se desejar, crie um veículo")
    print("1 - Criar veículo")
    cmd = input(">> ")
    if cmd == '1':
        num = input("Número de veículos a criar: ")
        num = int(num)
        tipo = input("Tipo de veículos a serem criados : ")
        criaVeiculos(num,tipo)
    elif cmd == 'exit':
        quit()
    else:
        pass
