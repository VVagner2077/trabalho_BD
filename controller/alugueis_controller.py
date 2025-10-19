# No topo do seu arquivo utils/menu.py
import os
import time

# Ela permite que o menu.py acesse o controller
from controller import alugueis_controller

# Importa a função de conexão do arquivo database.py (usando import relativo)
from .database import get_db_connection
import sys # Usado para imprimir erros simples

def registrar_aluguel(id_cliente, id_betoneira, data_inicio, data_prevista_termino):
    """
    Registra um novo aluguel.
    1. Verifica se a betoneira está 'disponivel'.
    2. Insere o aluguel.
    3. Muda o status da betoneira para 'alugada'.
    Tudo em uma única transação.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."

        with conn.cursor() as cursor:
            # 1. Verificar o status da betoneira
            cursor.execute("SELECT status FROM betoneiras WHERE id = %s", (id_betoneira,))
            resultado = cursor.fetchone()
            
            if not resultado:
                return "Erro: Betoneira não encontrada."
            if resultado[0] != 'disponivel':
                return f"Erro: Betoneira não está disponível (status: {resultado[0]})."
            
            # 2. Inserir na tabela de alugueis
            sql_aluguel = """
            INSERT INTO alugueis (id_cliente, id_betoneira, data_inicio, data_prevista_termino, status)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql_aluguel, (id_cliente, id_betoneira, data_inicio, data_prevista_termino, 'ativo'))

            # 3. Atualizar o status da betoneira
            sql_betoneira = "UPDATE betoneiras SET status = 'alugada' WHERE id = %s"
            cursor.execute(sql_betoneira, (id_betoneira,))
        
        # Se tudo deu certo, salva as alterações
        conn.commit()
        return "Aluguel registrado com sucesso!"

    except Exception as e:
        # Se algo deu errado, desfaz tudo
        if conn:
            conn.rollback()
        print(f"Erro inesperado [registrar_aluguel]: {e}", file=sys.stderr)
        return "Erro ao registrar aluguel."
    finally:
        if conn:
            conn.close()

def finalizar_aluguel(id_aluguel, data_termino_real):
    """
    Finaliza um aluguel.
    1. Atualiza o aluguel para 'finalizado' e pega o ID da betoneira.
    2. Atualiza a betoneira para 'disponivel'.
    Tudo em uma única transação.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."

        with conn.cursor() as cursor:
            # 1. Atualiza o aluguel e descobre qual betoneira era
            sql_aluguel = """
            UPDATE alugueis 
            SET data_termino_real = %s, status = 'finalizado' 
            WHERE id = %s 
            RETURNING id_betoneira
            """
            cursor.execute(sql_aluguel, (data_termino_real, id_aluguel))
            
            resultado = cursor.fetchone()
            if not resultado:
                return f"Erro: Aluguel com ID {id_aluguel} não encontrado."
            
            id_betoneira = resultado[0] # Pega o ID da betoneira

            # 2. Atualiza o status da betoneira
            sql_betoneira = "UPDATE betoneiras SET status = 'disponivel' WHERE id = %s"
            cursor.execute(sql_betoneira, (id_betoneira,))
            
        # Se tudo deu certo, salva as alterações
        conn.commit()
        return f"Aluguel {id_aluguel} finalizado. Betoneira {id_betoneira} liberada."

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [finalizar_aluguel]: {e}", file=sys.stderr)
        return "Erro ao finalizar aluguel."
    finally:
        if conn:
            conn.close()

def listar_alugueis_ativos():
    """
    Lista todos os aluguéis com status 'ativo'.
    Retorna uma lista de tuplas.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return None, "Erro de conexão."
        
        with conn.cursor() as cursor:
            sql = "SELECT * FROM alugueis WHERE status = 'ativo' ORDER BY data_prevista_termino ASC"
            cursor.execute(sql)
            alugueis = cursor.fetchall() # Retorna uma lista de tuplas, ex: [(1, 1, 2, ...), (2, 3, 1, ...)]
            
        return alugueis, "Consulta realizada com sucesso."

    except Exception as e:
        print(f"Erro inesperado [listar_alugueis_ativos]: {e}", file=sys.stderr)
        return None, "Erro ao listar aluguéis."
    finally:
        if conn:
            conn.close()

def listar_historico_cliente(id_cliente):
    """
    Lista todos os aluguéis (ativos e finalizados) de um cliente.
    Retorna uma lista de tuplas.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return None, "Erro de conexão."
        
        with conn.cursor() as cursor:
            sql = "SELECT * FROM alugueis WHERE id_cliente = %s ORDER BY data_inicio DESC"
            cursor.execute(sql, (id_cliente,))
            alugueis = cursor.fetchall()
            
        return alugueis, "Consulta realizada com sucesso."

    except Exception as e:
        print(f"Erro inesperado [listar_historico_cliente]: {e}", file=sys.stderr)
        return None, "Erro ao listar histórico."
    finally:
        if conn:
            conn.close()

# -----------------------------------------------------
# Bloco de teste (NÃO VAI RODAR QUANDO CHAMADO PELO MAIN.PY)
# -----------------------------------------------------
# ATENÇÃO: Se você tentar rodar este arquivo DIRETAMENTE
# (ex: py controller/alugueis_controller.py)
# você receberá o erro: ImportError: attempted relative import with no known parent package
# Isso é o ESPERADO. Este arquivo agora só funciona quando importado pelo main.py.
# -----------------------------------------------------
if __name__ == "__main__":
    print("--- ATENÇÃO ---")
    print("Este arquivo não deve ser executado diretamente.")
    print("Execute o 'main.py' na pasta raiz do projeto.")
    print("py main.py")