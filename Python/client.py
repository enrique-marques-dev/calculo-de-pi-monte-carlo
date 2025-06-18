import socket
import random

# Função local de cálculo de pontos dentro do círculo
def monte_carlo_local(pontos):
    dentro = 0
    for _ in range(pontos):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            dentro += 1
    return dentro

# Conexão com o servidor
HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Recebe a quantidade de pontos a calcular
data = client.recv(1024).decode()
pontos_recebidos = int(data)
print(f"[Cliente] Recebido: {pontos_recebidos} pontos")

# Calcula localmente e envia resultado
resultado_local = monte_carlo_local(pontos_recebidos)
client.sendall(str(resultado_local).encode())
print(f"[Cliente] Enviado: {resultado_local} pontos dentro do círculo")
client.close()
