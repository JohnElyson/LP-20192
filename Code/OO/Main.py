from Carro import Carro
from Moto import Moto
from Roda import Roda

lstVeiculos = []


def listaVeiculos(lstVeiculos):
    print("Veiculos existentes:")
    print()
    print("-Lista de veículos-")
    print("-"*19)
    print()        
    for veiculo in lstVeiculos:
        print((lstVeiculos.index(veiculo)+1), " - ", veiculo.getPlaca(), end='' )
        print(" ",veiculo.getTipoVeiculo()," ")
        print(" Possui ", veiculo.getNumRodas(), " Rodas")
    print()
    print("-"*19)
    print()
        

def criaVeiculos(qtd,tipo):
    for i in range(qtd):
            if tipo.lower() == 'carro':
                carro = Carro("kkk-0123")
                for j in range(carro.getMaxRodas()):
                    roda = Roda(14)
                    carro.addRoda(roda)
                lstVeiculos.append(carro)
            elif tipo.lower() == 'moto':
                moto = Moto("abc-0022")
                for j in range(moto.getMaxRodas()):
                    roda = Roda(14)
                    moto.addRoda(roda)
                lstVeiculos.append(moto)
                    
            else:
                    pass

def menu():
    while True:
        print("Se desejar, crie um veículo")
        print("1 - Criar veículo")
        cmd = input(">> ")
        if cmd == '1':
            num = input("Número de veículos a criar: ")
            num = int(num)
            tipo = input("Tipo de veículos a serem criados : ")
            criaVeiculos(num,tipo)
            listaVeiculos(lstVeiculos)
        elif cmd == 'exit':
            quit()
        else:
            pass

menu()
