from . import inputs_tratados
# Coloque isso logo abaixo das suas importações

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
        match escolha_crud:
            case '1':
                print("\n-- Adicionando Nova Betoneira --")
                adicionar_betoneira()
            case '2':
                print("\n-- Listando Todas as Betoneiras --")
                listar_betoneiras()
            case '3':
                print("\n-- Atualizando Betoneira --")
                atualizar_betoneira()
            case '4':
                print("\n-- Removendo Betoneira --")
                remover_betoneira()
            case '5':
                print("\nRetornando ao menu principal...")
                break # Quebra o loop e volta para o menu principal
            case _:
                print("\nOpção inválida! Tente novamente.")

# Funções de CRUD para betoneiras (serão implementadas aqui)
def adicionar_betoneira():
    modelo = inputs_tratados("Digite o modelo da betoneira: ")
    valor = inputs_tratados("Digite o valor da betoneira: ")

    #função adicionar
    
    print(f"Betoneira cadastrada: modelo={modelo}, valor={valor}")

def listar_betoneiras():
    #função
    input("\npressione qualquer botão para voltar")


def atualizar_betoneira():

    id = input("Digite o ID da betoneira que deseja atualizar")
    #pesquisar betoneira por id
    nome = inputs_tratados("Atualize o nome do modelo (deixe vazio se não querer atualizar):").strip
    valor = inputs_tratados("Atualize o valor(deixe vazio se não querer atualizar):").split
    if(nome==""):
        #select sem nome
        print("select com valor")
    elif(valor==""):
        #select sem valor
        print("select sem valor")
    else:
        #select com os dois
        print("select com os dois")





def remover_betoneira():
    id = input("Digite o ID da betoneira que deseja remover")

    #função delete
    print(f"Betoneira com ID {id} removida.")

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
        match escolha_crud:
            case '1':
                print("\n-- Adicionando Novo Cliente --")
                adicionar_cliente()
            case '2':
                print("\n-- Listando Todos os Clientes --")
                listar_clientes()
            case '3':
                print("\n-- Atualizando Cliente --")
                atualizar_cliente()
            case '4':
                print("\n-- Removendo Cliente --")
                remover_cliente()
            case '5':
                print("\nRetornando ao menu principal...")
                break # Quebra o loop e volta para o menu principal
            case _:
                print("\nOpção inválida! Tente novamente.")



def adicionar_cliente():
    nome = inputs_tratados("Digite o nome do cliente: ")
    telefone = inputs_tratados("Digite o telefone do cliente: ")
    cpf = inputs_tratados("Digite o CPF do cliente: ")
    # Aqui você pode salvar 'nome', 'telefone' e 'cpf' em uma lista, banco de dados, etc.

    print(f"Cliente cadastrado: nome={nome}, telefone={telefone}, cpf={cpf}")
    inputs_tratados.telefone("Digite o telefone do cliente: ")
    inputs_tratados.cpf("Digite o CPF do cliente: ")



def listar_clientes():
    #função select todos os clientes (select * from clientes)
    input("\npressione qualquer botão para voltar")

def atualizar_cliente():
    id = input("Digite o ID do cliente que deseja atualizar")
    #função select cliente por id
    nome = inputs_tratados("Atualize o nome do cliente (deixe vazio se não quiser atualizar):").strip
    telefone = inputs_tratados("Atualize o telefone (deixe vazio se não quiser atualizar):").strip
    cpf = inputs_tratados("Atualize o CPF (deixe vazio se não quiser atualizar):").strip
    if(nome==""):
        #select sem nome
        print("select com telefone e cpf")
    elif(telefone==""):
        #select sem telefone
        print("select com nome e cpf")
    elif(cpf==""):
        #select sem cpf
        print("select com nome e telefone")
    else:
        #select com os dois
        print("select com os três")

def remover_cliente():
    raise NotImplementedError

#--------------------------------------------------------------------------


# Funções para operações de aluguel
def registrar_novo_aluguel():
    input("id betoneira)")
    input("id cliente)")
    input("data inicio)")
    input("data fim)")
    #função inserir aluguel

def registrar_devolucao():
    input("id aluguel)")
    #função atualizar aluguel

def listar_alugueis_ativos():
    """
    Busca no controller e exibe todos os aluguéis com status 'ativo'.
    """
    # A linha "limpar_tela()" foi removida.
    # Adicionei um '\n' para dar um espaço.
    print("\n=========================================") 
    print("--- 5. Listar Aluguéis Ativos ---")
    print("=========================================")
    
    # Chama o controller para buscar os dados
    alugueis, msg = alugueis_controller.listar_alugueis_ativos()
    
    # Verifica se a consulta ao banco deu certo
    if alugueis is not None:
        
        # Verifica se a lista de aluguéis não está vazia
        if len(alugueis) > 0:
            print(f"{len(alugueis)} aluguéis ativos encontrados:")
            
            for aluguel in alugueis:
                # Ajuste os índices [0], [1], [2] etc. 
                # para bater com a ordem das colunas da sua tabela
                print("-" * 25)
                print(f"  ID Aluguel: {aluguel[0]}")
                print(f"  ID Cliente: {aluguel[1]}")
                print(f"  ID Betoneira: {aluguel[2]}")
                # Exemplo para datas (pode ser aluguel[4], aluguel[5], etc.)
                # print(f"  Data Início: {aluguel[4]}") 
        else:
            # A consulta funcionou, mas não retornou nenhum aluguel
            print("Nenhum aluguel ativo encontrado no banco de dados.")
    else:
        # Se 'alugueis' for None, 'msg' tem o erro vindo do controller
        print(f"Erro ao consultar o banco de dados: {msg}") 

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

        match escolha:
            case 1:
                print("\n-- Registrando Novo Aluguel --")
                registrar_novo_aluguel()
            case 2:
                print("\n-- Registrando Devolução --")
                registrar_devolucao()
            case 3:
                print("\n-- Gerenciando Clientes --")
                gerenciar_clientes()
            case 4:
                print("\n-- Gerenciando Betoneiras --")
                gerenciar_betoneiras()
            case 5:
                print("\n-- Listando Aluguéis Ativos --")
                listar_alugueis_ativos()
            case 6:
                print("\n-- Listando Betoneiras Disponíveis --")
                listar_betoneiras_disponiveis()
            case 7:
                print("\n-- Histórico de Aluguéis --")
                historico_alugueis()
            case 8:
                print("\nSaindo do sistema. Até logo!")
                break # Sai do loop e termina o programa
# Inicia o programa
menu()