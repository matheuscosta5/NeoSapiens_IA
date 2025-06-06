# interface/menu.py

import customtkinter as ctk
from interface.grafico import GraficoUsoSemanal  # Importa a classe do gráfico

class MenuPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NeoSapiens - Jarvis Pessoal")
        self.geometry("700x450")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Título
        self.label_titulo = ctk.CTkLabel(
            self, text="🧠 NeoSapiens", font=("Roboto", 28, "bold")
        )
        self.label_titulo.pack(pady=30)

        # Botão: Ativar Jarvis
        self.btn_ativar = ctk.CTkButton(
            self, text="🎙 Ativar Jarvis", command=self.ativar_jarvis, width=200
        )
        self.btn_ativar.pack(pady=10)

        # Botão: Histórico
        self.btn_historico = ctk.CTkButton(
            self, text="📁 Ver Histórico", command=self.ver_historico, width=200
        )
        self.btn_historico.pack(pady=10)

        # Botão: Uso semanal (agora abre a janela do gráfico)
        self.btn_uso = ctk.CTkButton(
            self, text="📊 Uso Semanal", command=self.ver_uso_semanal, width=200
        )
        self.btn_uso.pack(pady=10)

        # Botão: Sair
        self.btn_sair = ctk.CTkButton(
            self, text="❌ Sair", command=self.destroy, fg_color="red", width=200
        )
        self.btn_sair.pack(pady=40)

    def ativar_jarvis(self):
        print("🧠 Jarvis ativado... (conectar ao core/jarvis.py depois)")

    def ver_historico(self):
        print("🔎 Exibindo histórico de conversas...")

    def ver_uso_semanal(self):
        
        grafico = GraficoUsoSemanal(self)
        grafico.grab_set()  # Dá foco na janela do gráfico, bloqueando a principal até fechar
