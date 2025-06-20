import csv
import matplotlib.pyplot as plt

# Listas fixas com os dados da execução sequencial e paralela
total_points_list = [100_000, 500_000, 1_000_000, 5_000_000, 10_000_000]
sequencial_times = [0.0175, 0.0809, 0.1618, 0.8107, 1.6283]
paralelo_4_times = [0.0180, 0.0834, 0.1634, 0.8163, 1.6277]
paralelo_8_times = [0.0177, 0.0836, 0.1679, 0.8227, 1.6445]

# Lê os dados do tempo_distribuido.csv
distribuido_pontos = []
distribuido_tempos = []

with open("tempo_distribuido.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        distribuido_pontos.append(int(row["total_pontos"]))
        distribuido_tempos.append(float(row["tempo_segundos"]))

# Gráfico: Comparação Geral (Sequencial, Paralelo e Distribuído)
plt.figure(figsize=(10, 6))
plt.plot(total_points_list, sequencial_times, label='Sequencial', marker='o')
plt.plot(total_points_list, paralelo_4_times, label='Paralelo (4 Threads)', marker='o')
plt.plot(total_points_list, paralelo_8_times, label='Paralelo (8 Threads)', marker='o')
plt.plot(distribuido_pontos, distribuido_tempos, label='Distribuído (4 Clientes)', marker='o')
plt.xlabel('Total de Pontos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação Geral: Sequencial vs Paralelo vs Distribuído')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("comparacao_geral.png")
plt.show()

# Speedup do Distribuído em relação à Sequencial
speedup_distribuido = [
    seq / dist for seq, dist in zip(sequencial_times, distribuido_tempos)
]

# Eficiência do Distribuído (assumindo 4 clientes)
eficiencia_distribuido = [s / 4 for s in speedup_distribuido]

# Gráfico: Speedup Distribuído
plt.figure(figsize=(10, 6))
plt.plot(distribuido_pontos, speedup_distribuido, label='Speedup (Distribuído)', marker='o')
plt.xlabel('Total de Pontos')
plt.ylabel('Speedup')
plt.title('Speedup da Versão Distribuída em relação à Sequencial')
plt.grid(True)
plt.tight_layout()
plt.savefig("speedup_distribuido.png")
plt.show()

# Gráfico: Eficiência Distribuída
plt.figure(figsize=(10, 6))
plt.plot(distribuido_pontos, eficiencia_distribuido, label='Eficiência (Distribuído)', marker='o')
plt.xlabel('Total de Pontos')
plt.ylabel('Eficiência')
plt.title('Eficiência da Versão Distribuída (4 Clientes)')
plt.grid(True)
plt.tight_layout()
plt.savefig("eficiencia_distribuido.png")
plt.show()
