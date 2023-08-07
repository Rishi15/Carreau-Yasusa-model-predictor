import numpy as np
import matplotlib.pyplot as plt
import math
p=np.linspace(-2,3,50)
p[1]
x=[]
y_data=[]
for i in range(len(p)):
  x.append(10**(p[i]))
  #print(x)

def cy_func(x,l,n,a,eta_n,eta_o):
    y=(eta_n+(eta_o-eta_n)*(1+((l*x)**a))**((n-1)/a))
    return y

for i in range(len(x)):
  y_data.append(cy_func(x[i],l=0.01338,n=0.2585,a=0.4009,eta_n=0.001,eta_o=4.316))

fig, ax = plt.subplots()
ax.plot(x, y_data)
ax.set_xscale('log')
ax.set_yscale('log')

# Set the log-scale limits
ax.set_xlim([1e-2, 1e3])
ax.set_ylim([1e-1, 1e1])
plt.xlabel('Shear Rate [1/s]')
plt.ylabel('Viscosity [Pa-s]')
