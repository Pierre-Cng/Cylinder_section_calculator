import numpy as np
import matplotlib.pyplot as plt 

semi_major = 10
semi_minor = 5
t = np.linspace(0, 2*np.pi)

def ellipse_eq(semi_minor, semi_major, t):
    x =semi_major * np.cos(t)
    y = semi_minor * np.sin(t)
    return x, y

def tronc_ellipse():
    x = []
    y = []
    t1 = np.linspace(-0.25*np.pi, 0)
    for i in t1:
        x.append(7)
        y.append(-3)
    t2 = np.linspace(0, 0.25*np.pi)
    for i in t2:
        x.append(7)
        y.append(3)
    t3 = np.linspace(0.25*np.pi, 0.75*np.pi)
    for i in t3:
        x.append(semi_major * np.cos(i))
        y.append(semi_minor * np.sin(i))
    t4 = np.linspace(0.75*np.pi, 0)
    for i in t4:
        x.append(-7)
        y.append(3)
    t5 = np.linspace(0, -0.75*np.pi)
    for i in t5:
        x.append(-7)
        y.append(-3)
    t6 = np.linspace(-0.75*np.pi, -0.25*np.pi)
    for i in t6:
        x.append(semi_major * np.cos(i))
        y.append(semi_minor * np.sin(i))

    return x, y

x, y = tronc_ellipse()
plt.plot(x, y)

plt.show()