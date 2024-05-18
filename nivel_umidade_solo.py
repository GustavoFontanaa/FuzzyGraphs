import numpy as np
import matplotlib.pyplot as plt

# Funções de pertinência
def umidade_seco(U):
    # Trapezoidal: Pertence totalmente (1) até 10%, depois decresce linearmente até 30%
    return np.where(U <= 10, 1, np.where(U <= 30, (30 - U) / 20, 0))

def umidade_umido(U):
    # Triangular: Aumenta linearmente de 20% a 40%, depois decresce até 60%
    return np.where(U <= 20, 0, np.where(U <= 40, (U - 20) / 20, np.where(U <= 60, (60 - U) / 20, 0)))

def umidade_saturado(U):
    # Trapezoidal: Pertence parcialmente a partir de 50%, pertence totalmente (1) acima de 70%
    return np.where(U <= 50, 0, np.where(U <= 70, (U - 50) / 20, 1))

# Valores de umidade
U = np.linspace(0, 100, 500)

# Plotagem
plt.plot(U, umidade_seco(U), label='Seco')
plt.plot(U, umidade_umido(U), label='Úmido')
plt.plot(U, umidade_saturado(U), label='Saturado')
plt.title('Nível de Umidade do Solo')
plt.xlabel('Umidade (%)')
plt.ylabel('Grau de Pertinência')
plt.legend()
plt.show()
