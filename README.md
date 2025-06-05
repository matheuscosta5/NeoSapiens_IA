<h1 align="center">🧠 NeoSapiens – Seu Jarvis Pessoal</h1>

<p align="center">
  Um assistente de IA pessoal com comando de voz, visual futurista, bom humor e utilidade real.
  <br><br>
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/vers%C3%A3o-1.0--alpha-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/intera%C3%A7%C3%A3o-voz%20ativa-success?style=for-the-badge"/>
</p>

---

## 📜 Descrição

O **NeoSapiens** é um assistente pessoal de inteligência artificial inspirado no Jarvis do Homem de Ferro. Ele conversa com você por voz, entende comandos naturais e responde com inteligência, bom humor e visual moderno. Ideal para quem quer um assistente realmente interativo e funcional, sem depender de cliques ou telas.


## 🚀 Funcionalidades

🎙 **Comando de Voz Total**  
🧠 **Conversas sobre qualquer tema**  
📰 **Noticiário diário + clima local**  
📊 **Gráficos de uso semanal (Matplotlib)**  
📁 **Histórico de conversas por texto ou voz**  
🎵 **Player de música por voz (Spotify/YouTube)**  
🎞 **Animação de boot com fala inicial ("Bom dia, chefe. A revolução começou.")**


## 🧬 Estrutura do Projeto

NeoSapiens IA/
├── main.py
├── .env
├── requirements.txt
├── README.md
│
├── assets/
│ ├── logo/
│ ├── audio/
│ ├── video/
│ └── icons/
│
├── core/
│ ├── boot_sequence.py
│ ├── voice_interface.py
│ ├── ai_engine.py
│ ├── utils.py
│ └── database/
│ └── connection.py
│
├── modules/
│ └── jarvis.py
│
├── interface/
│ ├── app.py
│ ├── menu.py
│ ├── circle_animation.py
│ └── themes/
│
├── data/
│ ├── history/
│ ├── usage/
│ └── logs/
│
└── tests/
└── test_jarvis.py

---

## 🗄️ Banco de Dados (MySQL)

```sql
CREATE TABLE IF NOT EXISTS historico_conversas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entrada_usuario TEXT,
    resposta_ia TEXT,
    data_conversa TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS uso_semanal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_uso DATE,
    minutos_uso INT
);

CREATE TABLE IF NOT EXISTS favoritos_musicais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_musica VARCHAR(200),
    artista VARCHAR(100),
    url TEXT,
    data_adicionado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

📦 Requisitos
Python 3.10+

MySQL

SpeechRecognition, pyttsx3, gTTS

openai, matplotlib, customtkinter, requests

APIs: OpenAI, Spotify (ou YouTube para música)

Instale tudo com:
pip install -r requirements.txt


▶️ Execução
python main.py

Ao abrir o app:

O Jarvis dá bom dia com som e vídeo.

Começa a animação de "pensamento".

Você comanda por voz: "Jarvis, toca Nirvana" ou "Me atualiza".

💡 Exemplos de Comando
Comando de Voz	Resposta Esperada
"Jarvis, me explica buracos negros"	Explicação com base científica via IA
"Me atualiza"	Notícias + Clima local
"Mostre meus dados da semana"	Gráfico de uso (tempo total)
"Toca AC/DC"	Player busca e inicia a música
"Lembra o que falamos sobre ansiedade?"	Mostra histórico relevante

🛡️ Status do Projeto
🔨 Em desenvolvimento (versão 1.0-alpha).
O objetivo é criar um assistente funcional, útil e fluido via voz, com possibilidade de expansão para domótica, agenda, e outros sistemas no futuro.

👨‍💻 Autor
Desenvolvido por [Seu Nome Aqui]
GitHub: github.com/seuusuario

<p align="center"> <em>"A revolução começou." – NeoSapiens</em> </p> ```