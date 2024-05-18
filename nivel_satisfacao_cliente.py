import numpy as np
import matplotlib.pyplot as plt

# Funções de pertinência
def satisfacao_baixa(S):
     # Trapezoidal: Pertence totalmente (1) até 10 pontos, depois decresce linearmente até 30 pontos
    return np.where(S <= 10, 1, np.where(S <= 30, (30 - S) / 20, 0))

def satisfacao_media(S):
    # Triangular: Aumenta linearmente de 20 pontos a 40 pontos, depois decresce até 70 pontos
    return np.where(S <= 20, 0, np.where(S <= 40, (S - 20) / 20, np.where(S <= 70, (70 - S) / 20, 0)))

def satisfacao_alta(S):
    # Trapezoidal: Pertence parcialmente a partir de 60 pontos, pertence totalmente (1) acima de 80 pontos
    return np.where(S <= 60, 0, np.where(S <= 80, (S - 60) / 20, 1))

# Valores de satisfação
S = np.linspace(0, 100, 500)

# Plotagem
plt.plot(S, satisfacao_baixa(S), label='Baixa')
plt.plot(S, satisfacao_media(S), label='Média')
plt.plot(S, satisfacao_alta(S), label='Alta')
plt.title('Nível de Satisfação do Cliente')
plt.xlabel('Satisfação (pontos)')
plt.ylabel('Grau de Pertinência')
plt.legend()
plt.show()
