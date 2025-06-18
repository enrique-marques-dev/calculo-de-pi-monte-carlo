import random

def monte_carlo_pi_sequencial(total_points):
    """
    Calcula Pi usando o método Monte Carlo de forma sequencial.

    Args:
        total_points (int): O número total de pontos aleatórios a serem gerados.

    Returns:
        float: O valor estimado de Pi.
    """
    inside = 0
    for _ in range(total_points):
        x = random.random()  # Gera uma coordenada x aleatória entre 0 e 1
        y = random.random()  # Gera uma coordenada y aleatória entre 0 e 1
        if x*x + y*y <= 1:   # Verifica se o ponto está dentro do círculo de raio 1
            inside += 1
    pi = 4 * inside / total_points  # Estimação de Pi
    return pi