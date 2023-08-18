import numpy as np
import matplotlib.pyplot as plt 

semi_major = 10
semi_minor = 5
t = np.linspace(0, 2*np.pi)

def ellipse_eq(semi_minor, semi_major, t):
    x =semi_major * np.cos(t)
    y = semi_minor * np.sin(t)
    return x, y

def t_lim():
    max_l = 8 
    semi_major = 10
    semi_minor = 5
    t_lim = np.arccos(max_l / semi_major)
    print(np.rad2deg(t_lim))
    return t_lim

def tronc_ellipse():
    x = []
    y = []
    semi_major = 10
    semi_minor = 5
    max_l = 8
    t1 = np.linspace(-t_lim(), 0)
    for i in t1:
        x.append(max_l)
        y.append(-np.sqrt(1-((max_l/semi_major)**2))*semi_minor)
    t2 = np.linspace(0, t_lim())
    for i in t2:
        x.append(max_l)
        y.append(np.sqrt(1-((max_l/semi_major)**2))*semi_minor)
    t3 = np.linspace(t_lim(), np.pi - t_lim())
    for i in t3:
        x.append(semi_major * np.cos(i))
        y.append(semi_minor * np.sin(i))
    t4 = np.linspace(np.pi - t_lim(), np.pi)
    for i in t4:
        x.append(-max_l)
        y.append(np.sqrt(1-(max_l/semi_major)**2)*semi_minor)
    t5 = np.linspace(np.pi, np.pi + t_lim())
    for i in t5:
        x.append(-max_l)
        y.append(-np.sqrt(1-(max_l/semi_major)**2)*semi_minor)
    t6 = np.linspace(-np.pi + t_lim(), -t_lim())
    for i in t6:
        x.append(semi_major * np.cos(i))
        y.append(semi_minor * np.sin(i))
    print(x)
    print(y)
    return x, y

x, y = tronc_ellipse()
plt.plot(x, y)

plt.show()