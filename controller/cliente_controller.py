from ..conex.database import get_db_connection
import sys

def cadastrar_cliente(nome, telefone, cpf):
    """
    Cadastra um novo cliente no banco de dados.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."

        with conn.cursor() as cursor:
            sql = "INSERT INTO clientes (nome, telefone, cpf) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, telefone, cpf))
        
        conn.commit()
        return "Cliente cadastrado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        
        if "duplicate key" in str(e) or "UNIQUE constraint" in str(e):
            return "Erro: CPF já cadastrado."
            
        print(f"Erro inesperado [cadastrar_cliente]: {e}", file=sys.stderr)
        return "Erro ao cadastrar cliente."
    finally:
        if conn:
            conn.close()

def listar_clientes():
    """
    Lista todos os clientes cadastrados.
    Retorna uma lista de tuplas.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return None, "Erro de conexão."
        
        with conn.cursor() as cursor:
            sql = "SELECT id, nome, telefone, cpf FROM clientes ORDER BY nome"
            cursor.execute(sql)
            clientes = cursor.fetchall()
            
        return clientes, "Consulta realizada com sucesso."

    except Exception as e:
        print(f"Erro inesperado [listar_clientes]: {e}", file=sys.stderr)
        return None, "Erro ao listar clientes."
    finally:
        if conn:
            conn.close()

def atualizar_cliente(id_cliente, novo_nome, novo_telefone):
    """
    Atualiza o nome e/ou telefone de um cliente existente pelo ID.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."

        with conn.cursor() as cursor:
            sql = "UPDATE clientes SET nome = %s, telefone = %s WHERE id = %s"
            cursor.execute(sql, (novo_nome, novo_telefone, id_cliente))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            return "Erro: Cliente não encontrado (ID inválido)."
            
        return "Cliente atualizado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [atualizar_cliente]: {e}", file=sys.stderr)
        return "Erro ao atualizar cliente."
    finally:
        if conn:
            conn.close()

def deletar_cliente(id_cliente):
    """
    Deleta um cliente do banco de dados pelo ID.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."

        with conn.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE id = %s"
            cursor.execute(sql, (id_cliente,))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            return "Erro: Cliente não encontrado (ID inválido)."
            
        return "Cliente deletado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        
        if "foreign key" in str(e):
            return "Erro: Não é possível deletar cliente que possui aluguéis registrados."
            
        print(f"Erro inesperado [deletar_cliente]: {e}", file=sys.stderr)
        return "Erro ao deletar cliente."
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("--- ATENÇÃO ---")
    print("Este arquivo não deve ser executado diretamente.")
    print("Execute o 'main.py' na pasta raiz do projeto.")