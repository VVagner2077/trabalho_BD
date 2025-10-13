alugueis = []
proximo_id = 1

while True:
    print("\n========================================")
    print("  Sistema de Aluguel de Betoneiras")
    print("========================================")
    print("1. Adicionar Aluguel")
    print("2. Listar Todos os Aluguéis")
    print("3. Atualizar Aluguel")
    print("4. Deletar Aluguel")
    print("5. Sair")
    print("========================================")
    
    escolha = input("Escolha uma opção: ")

    # --- 1. ADICIONAR ---
    if escolha == '1':
        cliente = input("Nome do Cliente: ")
        modelo = input("Modelo da Betoneira: ")
        
        novo_aluguel = {
            'id': proximo_id,
            'cliente': cliente,
            'modelo': modelo
        }
        alugueis.append(novo_aluguel)
        
        print(f"-> Aluguel ID {proximo_id} adicionado com sucesso!")
        proximo_id += 1

    # --- 2. LISTAR ---
    elif escolha == '2':
        if not alugueis:
            print("-> Nenhum aluguel cadastrado.")
        else:
            for aluguel in alugueis:
                print(f"ID: {aluguel['id']} | Cliente: {aluguel['cliente']} | Modelo: {aluguel['modelo']}")

    # --- 3. ATUALIZAR ---
    elif escolha == '3':
        try:
            id_para_atualizar = int(input("ID do aluguel para atualizar: "))
            
            encontrado = False
            for aluguel in alugueis:
                if aluguel['id'] == id_para_atualizar:
                    novo_cliente = input(f"Novo nome para '{aluguel['cliente']}': ")
                    novo_modelo = input(f"Novo modelo para '{aluguel['modelo']}': ")
                    
                    aluguel['cliente'] = novo_cliente
                    aluguel['modelo'] = novo_modelo
                    
                    print("-> Aluguel atualizado!")
                    encontrado = True
                    break
            
            if not encontrado:
                print("-> ID não encontrado.")
                
        except ValueError:
            print("-> ID inválido. Digite um número.")

    # --- 4. DELETAR ---
    elif escolha == '4':
        try:
            id_para_deletar = int(input("ID do aluguel para deletar: "))
            
            aluguel_para_remover = None
            for aluguel in alugueis:
                if aluguel['id'] == id_para_deletar:
                    aluguel_para_remover = aluguel
                    break
            
            if aluguel_para_remover:
                alugueis.remove(aluguel_para_remover)
                print("-> Aluguel deletado!")
            else:
                print("-> ID não encontrado.")

        except ValueError:
            print("-> ID inválido. Digite um número.")

    # --- 5. SAIR ---
    elif escolha == '5':
        print("Saindo do programa...")
        break # Quebra o loop 'while True' e encerra o programa

    # --- OPÇÃO INVÁLIDA ---
    else:
        print("-> Opção inválida, tente novamente.")