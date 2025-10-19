from ..conex.database import get_db_connection
import sys

def cadastrar_betoneira(modelo, marca):
    """
    Cadastra uma nova betoneira no banco de dados.
    O status inicial é sempre 'disponivel'.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."

        with conn.cursor() as cursor:
            sql = "INSERT INTO betoneiras (modelo, marca, status) VALUES (%s, %s, 'disponivel')"
            cursor.execute(sql, (modelo, marca))
        
        conn.commit()
        return "Betoneira cadastrada com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [cadastrar_betoneira]: {e}", file=sys.stderr)
        return "Erro ao cadastrar betoneira."
    finally:
        if conn:
            conn.close()

def listar_betoneiras():
    """
    Lista TODAS as betoneiras cadastradas (disponíveis ou não).
    Retorna uma lista de tuplas.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return None, "Erro de conexão."
        
        with conn.cursor() as cursor:
            sql = "SELECT id, modelo, marca, status FROM betoneiras ORDER BY id"
            cursor.execute(sql)
            betoneiras = cursor.fetchall()
            
        return betoneiras, "Consulta realizada com sucesso."

    except Exception as e:
        print(f"Erro inesperado [listar_betoneiras]: {e}", file=sys.stderr)
        return None, "Erro ao listar betoneiras."
    finally:
        if conn:
            conn.close()

def listar_betoneiras_disponiveis():
    """
    Lista apenas as betoneiras com status 'disponivel'.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return None, "Erro de conexão."
        
        with conn.cursor() as cursor:
            sql = "SELECT id, modelo, marca FROM betoneiras WHERE status = 'disponivel' ORDER BY id"
            cursor.execute(sql)
            betoneiras = cursor.fetchall()
            
        return betoneiras, "Consulta realizada com sucesso."

    except Exception as e:
        print(f"Erro inesperado [listar_betoneiras_disponiveis]: {e}", file=sys.stderr)
        return None, "Erro ao listar betoneiras."
    finally:
        if conn:
            conn.close()

def atualizar_status_betoneira(id_betoneira, novo_status):
    """
    Atualiza o status de uma betoneira (ex: 'disponivel', 'alugada', 'manutencao').
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."
        
        status_validos = ['disponivel', 'alugada', 'manutencao']
        if novo_status not in status_validos:
            return f"Erro: Status '{novo_status}' não é válido. Use: {status_validos}."

        with conn.cursor() as cursor:
            sql = "UPDATE betoneiras SET status = %s WHERE id = %s"
            cursor.execute(sql, (novo_status, id_betoneira))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            return "Erro: Betoneira não encontrada (ID inválido)."
            
        return "Status da betoneira atualizado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [atualizar_status_betoneira]: {e}", file=sys.stderr)
        return "Erro ao atualizar status."
    finally:
        if conn:
            conn.close()

def deletar_betoneira(id_betoneira):
    """
    Deleta uma betoneira do banco de dados pelo ID.
    Só permite deletar se não estiver alugada.
    """
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            return "Erro: Não foi possível conectar ao banco."

        with conn.cursor() as cursor:
            sql_check = "SELECT status FROM betoneiras WHERE id = %s"
            cursor.execute(sql_check, (id_betoneira,))
            resultado = cursor.fetchone()
            
            if not resultado:
                return "Erro: Betoneira não encontrada."
            if resultado[0] == 'alugada':
                return "Erro: Não é possível deletar uma betoneira que está alugada."
            
            sql_delete = "DELETE FROM betoneiras WHERE id = %s"
            cursor.execute(sql_delete, (id_betoneira,))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            return "Erro: Betoneira não encontrada (ID inválido)."
            
        return "Betoneira deletada com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        
        if "foreign key" in str(e):
            return "Erro: Não é possível deletar betoneira que possui histórico de aluguéis."
            
        print(f"Erro inesperado [deletar_betoneira]: {e}", file=sys.stderr)
        return "Erro ao deletar betoneira."
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("--- ATENÇÃO ---")
    print("Este arquivo não deve ser executado diretamente.")
    print("Execute o 'main.py' na pasta raiz do projeto.")