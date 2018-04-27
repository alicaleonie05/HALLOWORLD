import numpy as np
import matplotlib.pyplot as plt

arr= np.ones(3)

t = np.linspace(0,2*np.pi,200)
y = np.sin(t)

plt.plot(t,y,label="signal",linewidth=3.0)
plt.legend()
plt.xlabel("t",fontsize=15)
plt.ylabel("sin(t)",fontsize=15)
xticks=[0,0.5*np.pi,np.pi,1.5*np.pi,2*np.pi]
xtickslabels=["0","$\\frac{\pi}{2}$","$\pi$","$\\frac{3\pi}{2}$","$2\pi$"]
plt.xticks(xticks,xtickslabels,fontsize=10)
#hier habe ich ein problem
np.savefig("ersterplot.jpg")