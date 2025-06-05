import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.database.historico import salvar_conversa, listar_conversas
from core.database.historico import salvar_conversa, listar_conversas

# Simula um diálogo
salvar_conversa(
    usuario="Neo",
    mensagem="Qual a previsão do tempo hoje?",
    resposta="Hoje o tempo está ensolarado com máxima de 28°C.",
    modulo="clima"
)

# Lista os últimos registros
conversas = listar_conversas()
for conversa in conversas:
    print(f"[{conversa['data_hora']}] {conversa['usuario']}: {conversa['mensagem']} → {conversa['resposta']} (via {conversa['modulo']})")
