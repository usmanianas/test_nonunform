import numpy as np
import pylab as plt
from scipy import integrate

Nx = 100

xi = np.linspace(0, 1, Nx, endpoint=True)

beta = 1.0e0

x = 0.5*(1.0 - np.tanh(beta*(1.0 - 2*xi))/np.tanh(beta))

#fxi = xi**2 #np.random.random_sample(Nx)
fxi = np.random.random_sample(Nx)


dx_dxi = beta*(1.0/np.cosh(beta*(1.0-2*xi)))**2/np.tanh(beta)
dxi_dx = 1.0/dx_dxi

Axi = integrate.simpson(fxi, xi)
print("Axi = ", Axi)

Ax = integrate.simpson(fxi*dxi_dx, x)
print("Ax = ", Ax)

print("%error = ", ((Axi-Ax)/Ax)*100)



#print(xi)
#print(x)
#print(fx)
#print(dx_dxi)
