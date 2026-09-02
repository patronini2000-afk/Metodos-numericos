import numpy as np
import matplotlib.pyplot as plt

print("Vamos a graficar la función f(x)=e^(x^2)")
def f(x):
    return np.exp(x**2)
print(f"f(1)={f(1)}")

xx=np.linspace(0,1,100)
F1=f(xx)
plt.plot(xx,F1)
plt.title("Función $f(x) = e^{x^2}$")
plt.grid(True)
plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.show()