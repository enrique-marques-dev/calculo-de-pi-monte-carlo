# 🧠 Cálculo de Pi por Método de Monte Carlo (Versões: Sequencial, Paralela e Distribuída)

Este projeto implementa o cálculo da constante π (Pi) usando o método de Monte Carlo, abordando três abordagens computacionais distintas: **sequencial**, **paralela com threads** e **distribuída via sockets**. O objetivo é analisar desempenho, escalabilidade e eficiência entre essas abordagens.

---

## 🚀 Tecnologias e Ferramentas

- **Linguagem:** Python 3
- **Paralelismo:** `threading`
- **Distribuído:** `socket` (TCP/IP)
- **Visualização:** `matplotlib`
- **Execução:** Localhost

---

## 🔢 Lógica do Método de Monte Carlo
A técnica simula pontos aleatórios dentro de um quadrado unitário e calcula a razão de pontos que caem dentro de um quarto de círculo inscrito. A fórmula é:

π ≈ 4 × (pontos dentro do círculo / total de pontos simulados)

## ⚙️ Como Executar o Projeto
🧪 1. Instale as dependências

pip install matplotlib

🧠 2. Execute a versão sequencial e paralela

python solution.py

🌐 3. Execute a versão distribuída
Abra 1 terminal para o servidor:

python server.py

Em outros 4 terminais separados, execute o cliente:

python client.py

📊 4. Gere gráficos comparando com a versão distribuída

python comparacao_distribuida.py
