import threading
import random
import time
import matplotlib.pyplot as plt

# -------------------------------------
# Função: Cálculo de Pi usando Monte Carlo (versão sequencial)
# -------------------------------------
def monte_carlo_pi_sequencial(total_points):
    inside = 0
    for _ in range(total_points):
        x = random.random()  # Gera coordenada x aleatória entre 0 e 1
        y = random.random()  # Gera coordenada y aleatória entre 0 e 1
        if x*x + y*y <= 1:   # Verifica se o ponto está dentro do círculo de raio 1
            inside += 1
    pi = 4 * inside / total_points  # Estimação de Pi
    return pi

# -------------------------------------
# Variáveis globais para a versão paralela
# -------------------------------------
inside_circle = 0
lock = threading.Lock()  # Lock para evitar condições de corrida

# -------------------------------------
# Função executada por cada thread
# -------------------------------------
def monte_carlo_pi_thread(points_per_thread):
    global inside_circle
    local_count = 0  # Cada thread conta localmente os pontos dentro do círculo
    for _ in range(points_per_thread):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            local_count += 1
    # Atualiza o total global com proteção de lock
    with lock:
        inside_circle += local_count

# -------------------------------------
# Função: Monte Carlo paralelo com N threads
# -------------------------------------
def monte_carlo_pi_paralelo(total_points, num_threads):
    global inside_circle
    inside_circle = 0  # Reset do contador global
    threads = []
    points_per_thread = total_points // num_threads  # Divide pontos por thread

    # Criação e execução das threads
    for _ in range(num_threads):
        t = threading.Thread(target=monte_carlo_pi_thread, args=(points_per_thread,))
        threads.append(t)
        t.start()

    # Aguarda todas as threads terminarem
    for t in threads:
        t.join()

    # Estimação de Pi usando todos os pontos gerados
    pi = 4 * inside_circle / (points_per_thread * num_threads)
    return pi

# -------------------------------------
# Lista de diferentes quantidades de pontos para teste
# -------------------------------------
total_points_list = [100_000, 500_000, 1_000_000, 5_000_000, 10_000_000]

# Listas para armazenar os tempos de execução
sequencial_times = []
paralelo_4_times = []
paralelo_8_times = []

print("Executando testes de performance...\n")

# Loop para calcular os tempos de execução das três versões
for points in total_points_list:
    print(f"Pontos: {points:,}")

    # --- Sequencial ---
    start = time.time()
    pi_seq = monte_carlo_pi_sequencial(points)
    end = time.time()
    time_seq = end - start
    sequencial_times.append(time_seq)
    print(f"  Pi Sequencial:         {pi_seq:.6f} | Tempo: {time_seq:.4f}s")

    # --- Paralelo com 4 threads ---
    start = time.time()
    pi_par4 = monte_carlo_pi_paralelo(points, num_threads=4)
    end = time.time()
    time_par4 = end - start
    paralelo_4_times.append(time_par4)
    print(f"  Pi Paralelo (4 threads): {pi_par4:.6f} | Tempo: {time_par4:.4f}s")

    # --- Paralelo com 8 threads ---
    start = time.time()
    pi_par8 = monte_carlo_pi_paralelo(points, num_threads=8)
    end = time.time()
    time_par8 = end - start
    paralelo_8_times.append(time_par8)
    print(f"  Pi Paralelo (8 threads): {pi_par8:.6f} | Tempo: {time_par8:.4f}s\n")

# -------------------------------------
# Gráfico 1: Sequencial vs Paralelo (4 Threads)
# -------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(total_points_list, sequencial_times, label='Sequencial', marker='o')
plt.plot(total_points_list, paralelo_4_times, label='Paralelo (4 Threads)', marker='o')
plt.xlabel('Total de Pontos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Tempo: Sequencial vs 4 Threads')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("comparacao_tempo_4threads.png")
plt.show()

# -------------------------------------
# Gráfico 2: Sequencial vs Paralelo (8 Threads)
# -------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(total_points_list, sequencial_times, label='Sequencial', marker='o')
plt.plot(total_points_list, paralelo_8_times, label='Paralelo (8 Threads)', marker='o')
plt.xlabel('Total de Pontos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Tempo: Sequencial vs 8 Threads')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("comparacao_tempo_8threads.png")
plt.show()
