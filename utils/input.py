
#Inputs Betoneira
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

    while True:
        valor = input("Degite o valor: ")
        
        try:
            valor = float(valor)
            if valor < 10:
                print("O Valor minimo é R$10,00")
            elif valor > 500:
                print("O Valor maximo é R$500,00")
            else:
                break
        except:
            print("valor invalido")
    
    return valor

#Inputs Clintes
def input_nome():
    
    while True:
        cliente = input("Digite o nome do cliente: ")

        if (len(cliente) < 3):
            print("O Nome deve ter 3 ou mais caracteres\n ")
        elif(len(cliente) >100):
            print("O Nome deve ter até 100 caracteres\n")
        else:
            break
    return cliente

def input_telefone():
    
    while True:
        telefone = input("Digite o nome do cliente: ")

        telefone = telefone.replace("(","").replace(")","").replace("-","").replace(" ","")
        
        if not telefone.isdigit():
            print("Telefone invalido")
            continue
        
        if (len(telefone) == 11):
            break
        else:
            print("Telefone deve ter 11 numeros\n ")
            continue

    return telefone

def input_cpf():
    while True:
        cpf_str = input("Digite seu CPF: ")

        # 1. Limpeza e validações iniciais (da abordagem 1)
        cpf_limpo = cpf_str.replace(".", "").replace("-", "").replace(" ","")
        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11 or len(set(cpf_limpo)) == 1:
            print("Erro: Formato de CPF inválido. Verifique os dados e tente novamente.")
            continue

        # Separa os 9 primeiros dígitos para o cálculo
        nove_digitos = cpf_limpo[:9]
        
        try:
            # --- CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR ---
            soma_1 = 0
            for i, digito in enumerate(nove_digitos):
                soma_1 += int(digito) * (10 - i)
            
            resto_1 = soma_1 % 11
            digito_verificador_1 = 0 if resto_1 < 2 else 11 - resto_1

            # Validação do primeiro dígito
            if int(cpf_limpo[9]) != digito_verificador_1:
                print("Erro: CPF inválido (primeiro dígito verificador não confere).")
                continue

            # --- CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR ---
            dez_digitos = cpf_limpo[:10]
            soma_2 = 0
            for i, digito in enumerate(dez_digitos):
                soma_2 += int(digito) * (11 - i)
                
            resto_2 = soma_2 % 11
            digito_verificador_2 = 0 if resto_2 < 2 else 11 - resto_2

            # Validação do segundo dígito
            if int(cpf_limpo[10]) != digito_verificador_2:
                print("Erro: CPF inválido (segundo dígito verificador não confere).")
                continue

            # Se todas as validações passaram
            print("CPF VÁLIDO!")
            return cpf_limpo

        except Exception as e:
            # Captura qualquer erro inesperado durante o processo
            print(f"Ocorreu um erro inesperado: {e}")
            continue


from datetime import date, datetime

def input_data():
    hoje = date.today()
    

    formatos_aceitos = [
        "%d/%m/%Y",  # Ex: 17/10/2025
        "%d/%m/%y",  # Ex: 17/10/25
        "%d%m%Y",    # Ex: 17102025
        "%d%m%y"     # Ex: 171025    
    ]
    
    while True:
        # Atualizamos o texto de exemplo para o usuário
        data_str = input("Digite uma data (ex: 17/10/2025 ou 17102025): ")
        data_inserida = None

        # Limpa a string de entrada para ser mais tolerante (remove espaços extras)
        data_str_limpa = data_str.strip()

        # O loop tentará converter a string com cada formato da lista
        for formato in formatos_aceitos:
            try:
                data_inserida = datetime.strptime(data_str_limpa, formato).date()
                # Se a conversão funcionar, o loop é interrompido
                break
            except ValueError:
                # Se der erro, tenta o próximo formato
                continue
        
        # Se, após todos os formatos, a conversão falhou
        if not data_inserida:
            print("Formato de data inválido. Por favor, tente novamente.")
            continue

        # Validação para garantir que a data não está no passado
        if data_inserida < hoje:
            print(f"Erro: A data não pode ser no passado. Insira a data de hoje ({hoje.strftime('%d/%m/%Y')}) ou uma futura.")
            continue
        
        # Se tudo estiver correto, retorna a data
        return data_inserida
