import input 
# Função para o submenu de gerenciamento de betoneiras
def gerenciar_betoneiras():
    while True:
        # Mostra o menu do CRUD que discutimos antes
        escolha_crud = input('''
========================================
      CADASTRO DE BETONEIRAS (CRUD)
========================================

[1] Adicionar nova betoneira (Create)
[2] Listar todas as betoneiras (Read)
[3] Atualizar dados de uma betoneira (Update)
[4] Remover uma betoneira (Delete)
[5] Voltar ao Menu Principal

----------------------------------------

Escolha uma opção: ''')
        
        # Aqui viria a lógica para chamar as funções do CRUD
        if escolha_crud == '1':
            print("\n-- Adicionando Nova Betoneira --")
            # adicionar_betoneira()
        elif escolha_crud == '2':
            print("\n-- Listando Todas as Betoneiras --")
            # listar_betoneiras()
        elif escolha_crud == '3':
            print("\n-- Atualizando Betoneira --")
            # atualizar_betoneira()
        elif escolha_crud == '4':
            print("\n-- Removendo Betoneira --")
            # remover_betoneira()
        elif escolha_crud == '5':
            print("\nRetornando ao menu principal...")
            break # Quebra o loop e volta para o menu principal
        else:
            print("\nOpção inválida! Tente novamente.")

# Funções de CRUD para betoneiras (serão implementadas aqui)
def adicionar_betoneira():
    input.modelo("Digite o modelo da betoneira: ")
    input.valor("Digite o valor da betoneira: ")

def listar_betoneiras():
    raise NotImplementedError

def atualizar_betoneira():
    raise NotImplementedError

def remover_betoneira():
    raise NotImplementedError

#--------------------------------------------------------------------------

def gerenciar_clientes():
    while True:
        # Mostra o menu do CRUD que discutimos antes
        escolha_crud = input('''
========================================
      Gerenciamento de Clientes (CRUD)
========================================

[1] Adicionar novo cliente (Create)
[2] Listar todos os clientes (Read)
[3] Atualizar dados de um cliente (Update)
[4] Remover um cliente (Delete)
[5] Voltar ao Menu Principal

----------------------------------------

Escolha uma opção: ''')
        
        # Aqui viria a lógica para chamar as funções do CRUD
        if escolha_crud == '1':
            print("\n-- Adicionando Novo Cliente --")
            adicionar_cliente()
        elif escolha_crud == '2':
            print("\n-- Listando Todos os Clientes --")
            listar_clientes()
        elif escolha_crud == '3':
            print("\n-- Atualizando Cliente --")
            atualizar_cliente()
        elif escolha_crud == '4':
            print("\n-- Removendo Cliente --")
            remover_cliente()
        elif escolha_crud == '5':
            print("\nRetornando ao menu principal...")
            break # Quebra o loop e volta para o menu principal
        else:
            print("\nOpção inválida! Tente novamente.")

# Funções de CRUD para clientes (serão implementadas aqui)
def adicionar_cliente():
    input.nome("Digite o nome do cliente: ")
    input.telefone("Digite o telefone do cliente: ")
    input.cpf("Digite o CPF do cliente: ")

def listar_clientes():
    raise NotImplementedError

def atualizar_cliente():
    raise NotImplementedError

def remover_cliente():
    raise NotImplementedError

#--------------------------------------------------------------------------


# Funções para operações de aluguel
def registrar_novo_aluguel():
    raise NotImplementedError

def registrar_devolucao():
    raise NotImplementedError


# Funções para consultas e relatórios
def listar_alugueis_ativos():
    raise NotImplementedError

def listar_betoneiras_disponiveis():
    raise NotImplementedError

def historico_alugueis():
    raise NotImplementedError

# Menu principal
def menu():
    while True:
        escolha_str = input('''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   GERENCIADOR DE ALUGUEL DE BETONEIRAS          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

MENU PRINCIPAL

--- OPERAÇÕES DE ALUGUEL ---
[1] Registrar Novo Aluguel
[2] Registrar Devolução

--- CADASTROS ---
[3] Gerenciar Clientes
[4] Gerenciar Betoneiras (CRUD)

--- CONSULTAS E RELATÓRIOS ---
[5] Listar Aluguéis Ativos
[6] Listar Betoneiras Disponíveis
[7] Histórico de Aluguéis

--- SISTEMA ---
[8] Sair

---------------------------------------------------

Digite o número da opção desejada: ''')
        
        # Tratamento de erro
        try:
            escolha = int(escolha_str)
            if not (1 <= escolha <= 8):
                print(f"\nERRO: ({escolha}) é um número fora do intervalo válido (1-8). Tente novamente.")
                continue # Pula para a próxima iteração do loop
        except ValueError:
            print(f"\nERRO: ({escolha_str}) não é um número. Tente novamente.")
            continue # Pula para a próxima iteração do loop

        if escolha == 1:
            registrar_novo_aluguel()
        elif escolha == 2:
            registrar_devolucao()
        elif escolha == 3:
            gerenciar_clientes()
        elif escolha == 4:
            gerenciar_betoneiras() # Chama o submenu do CRUD
        elif escolha == 5:
            listar_alugueis_ativos()
        elif escolha == 6:
            listar_betoneiras_disponiveis()
        elif escolha == 7:
            historico_alugueis() # Agora na opção correta
        elif escolha == 8:
            print("\nSaindo do sistema. Até logo!")
            break # Encerra o loop e o programa

# Inicia o programa
menu()