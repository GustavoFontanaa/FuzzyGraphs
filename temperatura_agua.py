import numpy as np
import matplotlib.pyplot as plt

# Funções de pertinência
def temperatura_baixa(T):
    # Trapezoidal: Pertence totalmente (1) até 10°C, depois decresce linearmente até 30°C
    return np.where(T <= 10, 1, np.where(T <= 30, (30 - T) / 20, 0))

def temperatura_media(T):
    # Triangular: Aumenta linearmente de 20°C a 40°C, depois decresce até 60°C
    return np.where(T <= 20, 0, np.where(T <= 40, (T - 20) / 20, np.where(T <= 60, (60 - T) / 20, 0)))

def temperatura_alta(T):
    # Trapezoidal: Pertence parcialmente a partir de 50°C, pertence totalmente (1) acima de 70°C
    return np.where(T <= 50, 0, np.where(T <= 70, (T - 50) / 20, 1))

# Valores de temperatura
T = np.linspace(0, 100, 500)

# Plotagem
plt.plot(T, temperatura_baixa(T), label='Baixa')
plt.plot(T, temperatura_media(T), label='Média')
plt.plot(T, temperatura_alta(T), label='Alta')
plt.title('Temperatura da Água')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Grau de Pertinência')
plt.legend()
plt.show()