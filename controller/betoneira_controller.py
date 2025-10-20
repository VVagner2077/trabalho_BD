from conexion import database
import sys

def cadastrar_betoneira(modelo, valor):

    conn = None
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."

        with conn.cursor() as cursor:
            sql = "INSERT INTO betoneiras (modelo, valor, status) VALUES (%s, %s, 'disponivel')"
            cursor.execute(sql, (modelo, valor))
        
        conn.commit()
        return "Betoneira registada com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [cadastrar_betoneira]: {e}", file=sys.stderr)
        return "Erro ao registar betoneira."
    finally:
        if conn:
            conn.close()

def atualizar_dados_betoneira(id_betoneira, novo_modelo, novo_valor):

    conn = None
    partes_sql = []
    valores = []

    if novo_modelo:
        partes_sql.append("modelo = %s")
        valores.append(novo_modelo)
    if novo_valor is not None:
        partes_sql.append("valor = %s")
        valores.append(novo_valor)
    
    if not partes_sql:
        return "Nenhuma informação fornecida para atualização."
        
    valores.append(id_betoneira)

    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."
        
        with conn.cursor() as cursor:
            sql = f"UPDATE betoneiras SET {', '.join(partes_sql)} WHERE id = %s"
            cursor.execute(sql, valores)
            
            conn.commit()

            if cursor.rowcount == 0:
                return "Erro: Betoneira não encontrada (ID inválido)."
            
            return "Dados da betoneira atualizados com sucesso!"
    
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [atualizar_dados_betoneira]: {e}", file=sys.stderr)
        return "Erro ao atualizar dados da betoneira."
    finally:
        if conn:
            conn.close()

def atualizar_status_manutencao(id_betoneira, novo_status):

    conn = None
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."
        
        if novo_status == 'alugada':
            return "Erro: O status 'alugada' é definido automaticamente ao registrar um aluguel."

        status_permitidos = ['disponivel', 'manutencao']
        if novo_status not in status_permitidos:
            return f"Erro: Status '{novo_status}' não é válido para operação manual."

        with conn.cursor() as cursor:
            cursor.execute("SELECT status FROM betoneiras WHERE id = %s", (id_betoneira,))
            resultado = cursor.fetchone()
            
            if not resultado:
                return "Erro: Betoneira não encontrada."
            
            status_atual = resultado[0]
            if status_atual == 'alugada':
                return "Erro: Não é possível alterar o status de uma betoneira que está alugada."

            sql = "UPDATE betoneiras SET status = %s WHERE id = %s"
            cursor.execute(sql, (novo_status, id_betoneira))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            return "Erro: Betoneira não encontrada (ID inválido)."
            
        return "Status da betoneira atualizado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [atualizar_status_manutencao]: {e}", file=sys.stderr)
        return "Erro ao atualizar status."
    finally:
        if conn:
            conn.close()

def deletar_betoneira(id_betoneira):

    conn = None
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."

        with conn.cursor() as cursor:
            sql_check = "SELECT status FROM betoneiras WHERE id = %s"
            cursor.execute(sql_check, (id_betoneira,))
            resultado = cursor.fetchone()
            
            if not resultado:
                return "Erro: Betoneira não encontrada."
            if resultado[0] == 'alugada':
                return "Erro: Não é possível apagar uma betoneira que está atualmente alugada."
            
            sql_delete = "DELETE FROM betoneiras WHERE id = %s"
            cursor.execute(sql_delete, (id_betoneira,))
        
        conn.commit()
        
        return "Betoneira apagada com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        
        if "foreign key" in str(e).lower():
            return "Erro: Não é possível apagar a betoneira, pois ela possui um histórico de alugueres."
            
        print(f"Erro inesperado [deletar_betoneira]: {e}", file=sys.stderr)
        return "Erro ao apagar betoneira."
    finally:
        if conn:
            conn.close()
