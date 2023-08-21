import numpy as np
import matplotlib.pyplot as plt 

def ellipse_eq(semi_minor_axis, semi_major_axis, t):
    x =semi_major_axis * np.cos(t)
    y = semi_minor_axis * np.sin(t)
    return x, y

def t_limit(semi_major_axis, max_length):
    return np.arccos(max_length / semi_major_axis)

def t_lim():
    semi_major_axis = 10
    max_length = 8
    return np.arccos(max_length / semi_major_axis)

def extrem_point(x, y, a, b, semi_minor, semi_major, max_l):
        x.append(a * max_l)
        y.append(b * np.sqrt(1-((max_l/semi_major)**2))*semi_minor)

def curve(x, y, lim, semi_minor, semi_major):
    for i in np.linspace(lim[0], lim[1]):
        x.append(semi_major * np.cos(i))
        y.append(semi_minor * np.sin(i))

def tronc_ellipse():
    x = []
    y = []
    max_l = 8
    semi_major = 10 
    semi_minor = 5
    for i in range (2):
        extrem_point(x, y, 1 - 2 * i, 2 * i - 1, semi_minor, semi_major, max_l)
        extrem_point(x, y, 1 - 2 * i, 1 - 2 * i, semi_minor, semi_major, max_l)
        curve(x, y, [t_lim() - i * np.pi, (1 - i) * np.pi -t_lim()], semi_minor, semi_major)
    return x, y
   

x, y = tronc_ellipse()
plt.plot(x, y)

plt.show()