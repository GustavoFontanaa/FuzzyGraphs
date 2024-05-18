import numpy as np
import matplotlib.pyplot as plt

# Funções de pertinência
def poluicao_baixa(P):
    # Trapezoidal: Pertence totalmente (1) até 30 µg/m³, depois decresce linearmente até 100 µg/m³
    return np.where(P <= 30, 1, np.where(P <= 100, (100 - P) / 70, 0))

def poluicao_moderada(P):
    # Triangular: Aumenta linearmente de 50 µg/m³ a 100 µg/m³, depois decresce até 200 µg/m³
    return np.where(P <= 50, 0, np.where(P <= 100, (P - 50) / 50, np.where(P <= 200, (200 - P) / 50, 0)))

def poluicao_alta(P):
    # Trapezoidal: Pertence parcialmente a partir de 150 µg/m³, pertence totalmente (1) acima de 200 µg/m³
    return np.where(P <= 150, 0, np.where(P <= 200, (P - 150) / 50, 1))

# Valores de poluição
P = np.linspace(0, 500, 500)

# Plotagem
plt.plot(P, poluicao_baixa(P), label='Baixa')
plt.plot(P, poluicao_moderada(P), label='Moderada')
plt.plot(P, poluicao_alta(P), label='Alta')
plt.title('Nível de Poluição do Ar')
plt.xlabel('Poluição (µg/m³)')
plt.ylabel('Grau de Pertinência')
plt.legend()
plt.show()
