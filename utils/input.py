def input_modelo():
    
    while True:
        modelo = input("Digite o modelo: ")

        if (len(modelo) < 3):
            print("Modelo deve ter 3 ou mais caracteres\n ")
        elif(len(modelo) >100):
            print("Modelo deve ter até 100 caracteres\n")
        else:
            break
    return modelo

def input_valor():

    valor = input("Degite o valor: ")

modelo = input_modelo()

print(modelo)