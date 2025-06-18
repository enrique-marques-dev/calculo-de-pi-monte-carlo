import threading
import random

# Variáveis globais para a versão paralela
inside_circle = 0
lock = threading.Lock()  # Lock para evitar condições de corrida

def monte_carlo_pi_thread(points_per_thread):
    """
    Calcula o número de pontos dentro do círculo para uma dada thread.
    Atualiza um contador global com um lock para segurança de thread.
    """
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

def monte_carlo_pi_paralelo(total_points, num_threads):
    """
    Calcula Pi usando o método Monte Carlo em paralelo com múltiplas threads.

    Args:
        total_points (int): O número total de pontos aleatórios a serem gerados.
        num_threads (int): O número de threads a serem usadas para a computação paralela.

    Returns:
        float: O valor estimado de Pi.
    """
    global inside_circle
    inside_circle = 0  # Reseta o contador global
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