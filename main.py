# main.py

# Importa a função principal 'menu' do módulo 'menu.py' que está dentro da pasta 'utils'
from utils.menu import menu

def main():
    """
    Função principal que inicia a aplicação.
    """
    # Chama a função que exibe o menu principal e inicia o loop da aplicação
    menu()

if __name__ == "__main__":
    # Esta verificação garante que a função main() só será executada
    # quando este arquivo (main.py) for rodado diretamente.
    main()

    