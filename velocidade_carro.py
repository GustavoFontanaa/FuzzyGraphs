import numpy as np
import matplotlib.pyplot as plt

# Funções de pertinência
def velocidade_lenta(v):
    # Trapezoidal: Pertence totalmente (1) até 20 km/h, depois decresce linearmente até 40 km/h
    return np.where(v <= 20, 1, np.where(v <= 40, (40 - v) / 20, 0))

def velocidade_moderada(v):
    # Triangular: Aumenta linearmente de 30 km/h a 50 km/h, depois decresce até 80 km/h
    return np.where(v <= 30, 0, np.where(v <= 50, (v - 30) / 20, np.where(v <= 80, (80 - v) / 20, 0)))

def velocidade_rapida(v):
    # Trapezoidal: Pertence parcialmente a partir de 70 km/h, pertence totalmente (1) acima de 100 km/h
    return np.where(v <= 70, 0, np.where(v <= 100, (v - 70) / 30, 1))

# Valores de velocidade
v = np.linspace(0, 160, 500)

# Plotagem
plt.plot(v, velocidade_lenta(v), label='Lenta')
plt.plot(v, velocidade_moderada(v), label='Moderada')
plt.plot(v, velocidade_rapida(v), label='Rápida')
plt.title('Velocidade de um Carro')
plt.xlabel('Velocidade (km/h)')
plt.ylabel('Grau de Pertinência')
plt.legend()
plt.show()