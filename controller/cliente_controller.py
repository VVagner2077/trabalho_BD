from conexion import database
import sys

def cadastrar_cliente(nome, telefone, cpf):

    conn = None
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."

        with conn.cursor() as cursor:
            sql = "INSERT INTO clientes (nome, telefone, cpf) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, telefone, cpf))
        
        conn.commit()
        return "Cliente registado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        
      
        error_msg = str(e).lower()
        if "violates unique constraint" in error_msg:
            if "clientes_cpf_key" in error_msg:
                return "Erro: O CPF informado já está registado."
            if "clientes_telefone_key" in error_msg:
                return "Erro: O telefone informado já está registado."
        
        print(f"Erro inesperado [cadastrar_cliente]: {e}", file=sys.stderr)
        return "Erro ao registar cliente."
    finally:
        if conn:
            conn.close()

def atualizar_cliente(id_cliente, novo_nome, novo_telefone):
    
    conn = None
    partes_sql = []
    valores = []

    
    if novo_nome:
        partes_sql.append("nome = %s")
        valores.append(novo_nome)
    if novo_telefone:
        partes_sql.append("telefone = %s")
        valores.append(novo_telefone)
    
    if not partes_sql:
        return "Nenhuma informação fornecida para atualização."
    
    valores.append(id_cliente)
    
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."

        with conn.cursor() as cursor:
            sql = f"UPDATE clientes SET {', '.join(partes_sql)} WHERE id = %s"
            cursor.execute(sql, valores)
        
        conn.commit()
        
        if cursor.rowcount == 0:
            return "Erro: Cliente não encontrado (ID inválido)."
            
        return "Cliente atualizado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        
        error_msg = str(e).lower()
        if "violates unique constraint" in error_msg and "clientes_telefone_key" in error_msg:
            return "Erro: O novo telefone informado já pertence a outro cliente."

        print(f"Erro inesperado [atualizar_cliente]: {e}", file=sys.stderr)
        return "Erro ao atualizar cliente."
    finally:
        if conn:
            conn.close()

def deletar_cliente(id_cliente):

    conn = None
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."

        with conn.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE id = %s"
            cursor.execute(sql, (id_cliente,))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            return "Erro: Cliente não encontrado (ID inválido)."
            
        return "Cliente apagado com sucesso!"

    except Exception as e:
        if conn:
            conn.rollback()
        
        if "foreign key" in str(e).lower():
            return "Erro: Não é possível apagar um cliente que possui um histórico de alugueres."
            
        print(f"Erro inesperado [deletar_cliente]: {e}", file=sys.stderr)
        return "Erro ao apagar cliente."
    finally:
        if conn:
            conn.close()

