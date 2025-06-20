import socket
import threading
import time

# Configurações do servidor
HOST = 'localhost'
PORT = 5000

# Quantidade de clientes esperados e pontos por cliente
NUM_CLIENTES = 4
PONTOS_POR_CLIENTE = 2_500_000  

resultados = []
lock = threading.Lock()

def lidar_com_cliente(conn, addr):
    global resultados
    print(f"[Servidor] Conectado a {addr}")
    try:
        # Envia a quantidade de pontos
        conn.sendall(str(PONTOS_POR_CLIENTE).encode())

        # Recebe o número de pontos dentro do círculo
        data = conn.recv(1024).decode()
        local_inside = int(data)
        with lock:
            resultados.append(local_inside)
        print(f"[Servidor] Resultado de {addr}: {local_inside}")
    except:
        print(f"[Servidor] Erro com cliente {addr}")
    finally:
        conn.close()

# Início do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(NUM_CLIENTES)
print(f"[Servidor] Aguardando {NUM_CLIENTES} clientes...")

start_time = time.time()

threads = []
for _ in range(NUM_CLIENTES):
    conn, addr = server.accept()
    t = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
    t.start()
    threads.append(t)

# Espera todas as threads terminarem
for t in threads:
    t.join()

# Cálculo final de π
total_inside = sum(resultados)
total_pontos = PONTOS_POR_CLIENTE * NUM_CLIENTES
pi_estimado = 4 * total_inside / total_pontos
tempo_total = time.time() - start_time

print(f"\n[Servidor] Estimativa de π: {pi_estimado:.6f}")
print(f"[Servidor] Tempo total: {tempo_total:.4f} segundos")
server.close()

# Salva os resultados em um arquivo CSV
with open("tempo_distribuido.csv", "w") as f:
    f.write("pontos_por_cliente,total_pontos,pi_estimado,tempo_segundos\n")
    f.write(f"{PONTOS_POR_CLIENTE},{total_pontos},{pi_estimado:.6f},{tempo_total:.4f}\n")
