from .connection import conectar

def salvar_conversa(usuario, mensagem, resposta, modulo):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = """
                INSERT INTO historico_conversas (usuario, mensagem, resposta, modulo)
                VALUES (%s, %s, %s, %s)
            """
            valores = (usuario, mensagem, resposta, modulo)
            cursor.execute(sql, valores)
            conexao.commit()
            print("💾 Conversa salva com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar conversa: {e}")
        finally:
            conexao.close()

def listar_conversas(limit=10):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM historico_conversas ORDER BY data_hora DESC LIMIT {limit}")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar histórico: {e}")
        finally:
            conexao.close()
