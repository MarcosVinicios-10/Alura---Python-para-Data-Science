import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("C:\\Marcos\\Programação\\Python\\Alura\\Python para Data Science\\NumPy - análise numérica eficiente com Python\\numpy-dados//citrus.csv",delimiter=',', usecols=np.arange(1,6,1),skiprows=1)
dados = dados.T
diâmetroLaranja = dados[0,0:5000]
diâmetroToranja =  dados[0,5000:10001]
PesoLaranja = dados[1,0:5000]
PesoToranja =  dados[1,5000:10001]

def regressão(x,y):
    n = np.size(y)
    a = (n * sum(x*y) - sum(x) * sum(y))/ (n*sum(x**2)-(sum(x)**2)) 
    b = np.mean(y) - (a*np.mean(x))
    return a*x+b

fig, ax = plt.subplots(1,2)
ax[0].plot(PesoLaranja,diâmetroLaranja)
ax[0].plot(PesoLaranja,regressão(PesoLaranja,diâmetroLaranja))
ax[0].set_title('Laranja')
ax[0].legend(['Peso da laranja'])

ax[1].plot(PesoToranja,diâmetroToranja)
ax[1].plot(PesoToranja,regressão(PesoToranja,diâmetroToranja))
ax[1].set_title('Toranja')
ax[1].legend(['Peso da Toranja'])
plt.show()

print(np.linalg.norm(diâmetroLaranja-(regressão(PesoLaranja,diâmetroLaranja))))
print(np.linalg.norm(diâmetroToranja-(regressão(PesoToranja,diâmetroToranja))))
