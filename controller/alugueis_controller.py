from conexion import database
import sys

def registrar_aluguel(id_cliente, id_betoneira, data_inicio, data_prevista_termino):

    conn = None
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."

        with conn.cursor() as cursor:

            cursor.execute("SELECT status FROM betoneiras WHERE id = %s FOR UPDATE", (id_betoneira,))
            resultado = cursor.fetchone()
            
            if not resultado:
                return "Erro: Betoneira não encontrada."
            if resultado[0] != 'disponivel':
                return f"Erro: A betoneira não está disponível (status: {resultado[0]})."

            sql_aluguel = """
            INSERT INTO alugueis (id_cliente, id_betoneira, data_inicio, data_prevista_termino, status)
            VALUES (%s, %s, %s, %s, 'ativo')
            """
            cursor.execute(sql_aluguel, (id_cliente, id_betoneira, data_inicio, data_prevista_termino))

            sql_betoneira = "UPDATE betoneiras SET status = 'alugada' WHERE id = %s"
            cursor.execute(sql_betoneira, (id_betoneira,))
        

        conn.commit()
        return "Aluguer registado com sucesso!"

    except Exception as e:

        if conn:
            conn.rollback()
        print(f"Erro inesperado [registrar_aluguel]: {e}", file=sys.stderr)
        return "Erro ao registar aluguer."
    finally:
        if conn:
            conn.close()

def finalizar_aluguel(id_aluguel, data_termino_real):
    conn = None
    try:
        conn = database.criar_conexao()
        if not conn:
            return "Erro: Não foi possível conectar ao banco de dados."

        with conn.cursor() as cursor:

            sql_aluguel = """
            UPDATE alugueis 
            SET data_termino_real = %s, status = 'finalizado' 
            WHERE id = %s AND status = 'ativo'
            RETURNING id_betoneira
            """
            cursor.execute(sql_aluguel, (data_termino_real, id_aluguel))
            
            resultado = cursor.fetchone()
            if not resultado:
                return f"Erro: Aluguer com ID {id_aluguel} não encontrado ou já finalizado."
            
            id_betoneira = resultado[0] 


            sql_betoneira = "UPDATE betoneiras SET status = 'disponivel' WHERE id = %s"
            cursor.execute(sql_betoneira, (id_betoneira,))
            

        conn.commit()
        return f"Aluguer {id_aluguel} finalizado. Betoneira {id_betoneira} libertada."

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro inesperado [finalizar_aluguel]: {e}", file=sys.stderr)
        return "Erro ao finalizar aluguer."
    finally:
        if conn:
            conn.close()

