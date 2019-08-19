from Carro import Carro
from Moto import Moto

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
			lstVeiculos.append(Carro("kkk-0123"))
		elif tipo.lower() == 'moto':
			lstVeiculos.append(Moto("abc-0022"))
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
