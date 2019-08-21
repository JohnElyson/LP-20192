lstPlacas = []
lstNumRodas = []
lstTipoVeiculo = []

def listaVeiculos(lstPlacas,lstNumRodas,lstTipoVeiculo):
    print("Veiculos existentes:")
    print()
    print("-Lista de veículos-")
    print("-"*19)
    print()        
    for veiculo in range(len(lstPlacas)):
        print((veiculo+1), " - ", lstPlacas[veiculo], end='' )
        print(" ",lstTipoVeiculo[veiculo]," ")
        print(" Possui ", lstNumRodas[veiculo], " Rodas")
    print()
    print("-"*19)
    print()

def criaVeiculo(placa,numRodas,tipoVeiculo):
    lstPlacas.append(placa)
    lstNumRodas.append(numRodas)
    lstTipoVeiculo.append(tipoVeiculo)

def criaVeiculos(num,placa,numRodas,tipoVeiculo):
    for i in range(num):
        criaVeiculo(placa,numRodas,tipoVeiculo)

def menu():
    while True:
        print("Você pode criar um veículo")
        print("1 - Criar Veículo")
        cmd = input(">> ")
        if cmd == '1':
            num = input("Número de veículos a criar: ")
            num = int(num)
            tipoVeiculo = input("Tipo de veículos a serem criados : ")
            if tipoVeiculo.lower() == 'carro':
                placa = "kkk-0123"
                numRodas = 4
            elif tipoVeiculo.lower() == 'moto':
                placa = "abc-1111"
                numRodas = 2
            criaVeiculos(num,placa,numRodas,tipoVeiculo)
            listaVeiculos(lstPlacas,lstNumRodas,lstTipoVeiculo)
        elif cmd == 'exit':
            quit()
        else:
            pass

menu()
