# interface/grafico.py

import customtkinter as ctk
from tkinter import Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from mysql.connector import Error

class GraficoUsoSemanal(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("📊 Uso Semanal - NeoSapiens")
        self.geometry("700x500")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.fig, self.ax = plt.subplots(figsize=(7, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.plotar_grafico()

    def conectar_db(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="neosapiens_db"
            )
            return conexao
        except Error as e:
            print(f"Erro ao conectar no banco: {e}")
            return None

    def buscar_dados(self):
        conexao = self.conectar_db()
        if conexao is None:
            return [], []

        cursor = conexao.cursor()
        query = """
            SELECT data_uso, minutos_uso
            FROM uso_semanal
            ORDER BY data_uso DESC
            LIMIT 7
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()

        # Inverte os dados para ficar do dia mais antigo ao mais recente
        resultados.reverse()

        datas = [row[0].strftime("%d/%m") for row in resultados]
        minutos = [row[1] for row in resultados]
        return datas, minutos

    def plotar_grafico(self):
        datas, minutos = self.buscar_dados()
        self.ax.clear()  # Limpa o gráfico anterior

        # Fundo escuro para figura e eixo
        self.fig.patch.set_facecolor('#2b2b2b')
        self.ax.set_facecolor('#2b2b2b')

        if not datas or not minutos:
            self.ax.text(0.5, 0.5, "Nenhum dado disponível", ha="center", va="center", fontsize=14, color="white")
            self.ax.set_xticks([])
            self.ax.set_yticks([])
        else:
            self.ax.bar(datas, minutos, color='deepskyblue')
            self.ax.set_title("Uso Semanal (minutos)", fontsize=16, color="white")
            self.ax.set_xlabel("Data", fontsize=12, color="white")
            self.ax.set_ylabel("Minutos", fontsize=12, color="white")

            # Ticks e labels brancos para visibilidade no modo dark
            self.ax.tick_params(axis='x', colors='white')
            self.ax.tick_params(axis='y', colors='white')

            # Grid leve para facilitar leitura
            self.ax.grid(True, color='white', alpha=0.3, linestyle='--', linewidth=0.7)

        self.fig.tight_layout()
        self.canvas.draw()
