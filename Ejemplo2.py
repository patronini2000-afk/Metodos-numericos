from numpy import *
import matplotlib.pyplot as plt
def f(x):
    return 1 - e**(x) + (e-1)*sin(x*pi/2)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print(f"Función f(x) = 1 - e^x + (e-1)sin((pi/2)x)")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print(f"\nf(-1) = {f(-1)}")
print(f"f(0) = {f(0)}")
print(f"f(1) = {f(1)}")
print("")
X=linspace(0,1,100)
F1=f(X)
plt.plot(X,F1)
plt.title("Función $f(x) = 1 - e^x + (e-1)sin\\left(\\frac{\\pi}{2}x\\right)$")
plt.grid(True)
plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.show()