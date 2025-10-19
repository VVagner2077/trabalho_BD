from datetime import date, datetime

#Inputs Genéricos
def modelo(texto):
    while True:
        entrada = input(texto)
        if not entrada and "Novo" in texto: # Permite entrada vazia em atualizações
            return ""
        if (len(entrada) < 3):
            print(">> Erro: Deve ter 3 ou mais caracteres.")
        elif(len(entrada) > 100):
            print(">> Erro: Deve ter no máximo 100 caracteres.")
        else:
            break
    return entrada

def nome(texto):
    while True:
        entrada = input(texto)
        if not entrada and "Novo" in texto: # Permite entrada vazia em atualizações
            return ""
        if (len(entrada) < 3):
            print(">> Erro: O nome deve ter 3 ou mais caracteres.")
        elif(len(entrada) >100):
            print(">> Erro: O nome deve ter no máximo 100 caracteres.")
        else:
            break
    return entrada

def valor(texto):
    while True:
        entrada = input(texto)
        try:
            valor_float = float(entrada)
            if valor_float < 10:
                print(">> Erro: O valor mínimo é R$10,00.")
            elif valor_float > 1000: # Aumentado o limite para mais flexibilidade
                print(">> Erro: O valor máximo é R$1000,00.")
            else:
                break
        except ValueError:
            print(">> Erro: Valor inválido. Por favor, insira um número (ex: 99.90).")
    return valor_float

#Inputs Específicos de Cliente
def telefone(texto):
    while True:
        entrada = input(texto)
        if not entrada and "Novo" in texto: # Permite entrada vazia em atualizações
            return ""

        telefone_limpo = entrada.replace("(","").replace(")","").replace("-","").replace(" ","")
        
        if not telefone_limpo.isdigit():
            print(">> Erro: O telefone deve conter apenas números.")
            continue
        
        if (len(telefone_limpo) == 11):
            break
        else:
            print(">> Erro: O telefone deve ter 11 dígitos (DDD + número).")
            continue
    return telefone_limpo

def cpf(texto):
    while True:
        cpf_str = input(texto)
        cpf_limpo = cpf_str.replace(".", "").replace("-", "").replace(" ","")
        
        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11 or len(set(cpf_limpo)) == 1:
            print(">> Erro: Formato de CPF inválido. Verifique os dados e tente novamente.")
            continue

        try:
            # --- CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR ---
            nove_digitos = cpf_limpo[:9]
            soma_1 = sum(int(digito) * (10 - i) for i, digito in enumerate(nove_digitos))
            resto_1 = soma_1 % 11
            digito_verificador_1 = 0 if resto_1 < 2 else 11 - resto_1

            if int(cpf_limpo[9]) != digito_verificador_1:
                print(">> Erro: CPF inválido.")
                continue

            # --- CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR ---
            dez_digitos = cpf_limpo[:10]
            soma_2 = sum(int(digito) * (11 - i) for i, digito in enumerate(dez_digitos))
            resto_2 = soma_2 % 11
            digito_verificador_2 = 0 if resto_2 < 2 else 11 - resto_2

            if int(cpf_limpo[10]) != digito_verificador_2:
                print(">> Erro: CPF inválido.")
                continue

            return cpf_limpo
        except Exception:
            print(">> Erro: Ocorreu um problema ao validar o CPF.")
            continue

#Input de Data
def data(texto):
    hoje = date.today()
    formatos_aceitos = ["%d/%m/%Y", "%d/%m/%y", "%d%m%Y", "%d%m%y"]
    
    while True:
        data_str = input(texto).strip()
        data_inserida = None

        for formato in formatos_aceitos:
            try:
                data_inserida = datetime.strptime(data_str, formato).date()
                break
            except ValueError:
                continue
        
        if not data_inserida:
            print(">> Erro: Formato de data inválido. Use DD/MM/AAAA.")
            continue

        if data_inserida < hoje:
            print(f">> Erro: A data não pode ser no passado. A data de hoje é {hoje.strftime('%d/%m/%Y')}.")
            continue
        
        return data_inserida
