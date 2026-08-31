from numpy import *
import matplotlib.pyplot as plt
def f(x):
    return x - 3**(-x)
encabezado="Función $f(x) = x - 3^{-x}$"
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Función f(x) = x - 3^(-x)")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print(f"\nf(-1) = {f(-1)}")
print(f"f(0) = {f(0)}")
print(f"f(1) = {f(1)}")
print("")
X=linspace(-5,5,100)
F1=f(X)
plt.plot(X,F1)
plt.title(encabezado)
plt.grid(True)
plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.show()