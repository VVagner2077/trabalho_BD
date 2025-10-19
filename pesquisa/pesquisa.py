import pandas as pd
from conexion import database

# -------------------------------
# BETONEIRAS
# -------------------------------

def listar_betoneiras():
    conexao = None
    try:
        conexao = database.criar_conexao()
        df = pd.read_sql("SELECT * FROM betoneiras ORDER BY id_betoneira", conexao)
        print(df if not df.empty else "❌ Nenhuma betoneira encontrada.")
    except Exception as e:
        print("❌ Erro ao listar betoneiras:", e)
    finally:
        if conexao:
            conexao.close()


# -------------------------------
# CLIENTES
# -------------------------------

def listar_clientes():
    conexao = None
    try:
        conexao = database.criar_conexao()
        df = pd.read_sql("SELECT * FROM clientes ORDER BY id_cliente", conexao)
        print(df if not df.empty else "❌ Nenhum cliente encontrado.")
    except Exception as e:
        print("❌ Erro ao listar clientes:", e)
    finally:
        if conexao:
            conexao.close()

# -------------------------------
# CONSULTAS E RELATÓRIOS
# -------------------------------

def listar_alugueis_ativos():
    conexao = None
    try:
        conexao = database.criar_conexao()
        sql = "SELECT * FROM alugueis WHERE status='TRUE' ORDER BY data_aluguel"
        df = pd.read_sql(sql, conexao)
        if df.empty:
            print("❌ Nenhum aluguel ativo encontrado.")
        else:
            print("\n🔎 Aluguéis ativos:\n")
            print(df)
    except Exception as e:
        print(f"❌ Erro ao listar aluguéis ativos: {e}")
    finally:
        if conexao:
            conexao.close()


def listar_betoneiras_disponiveis():
    conexao = None
    try:
        conexao = database.criar_conexao()
        sql = "SELECT * FROM betoneiras WHERE status=TRUE ORDER BY id_betoneira"
        df = pd.read_sql(sql, conexao)
        if df.empty:
            print("❌ Nenhuma betoneira disponível.")
        else:
            print("\n🔎 Betoneiras disponíveis:\n")
            print(df)
    except Exception as e:
        print(f"❌ Erro ao listar betoneiras disponíveis: {e}")
    finally:
        if conexao:
            conexao.close()


def historico_alugueis():
    conexao = None
    try:
        conexao = database.criar_conexao()
        sql = "SELECT * FROM alugueis ORDER BY data_aluguel DESC"
        df = pd.read_sql(sql, conexao)
        if df.empty:
            print("❌ Nenhum histórico encontrado.")
        else:
            print("\n🔎 Histórico de Aluguéis:\n")
            print(df)
    except Exception as e:
        print(f"❌ Erro ao consultar histórico de alugueis: {e}")
    finally:
        if conexao:
            conexao.close()