# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Ellipse, Rectangle
 
# Create subplot
fig, ax = plt.subplots(2)
plt.subplots_adjust(bottom=0.35)
ax[0].axvline(x=0, ymin=0.1, ymax=0.9, linestyle = 'dashed', color='r')
 
# Create and plot sine wave
angle = 0.0
t = np.arange(-4.0, 4.0, 0.001)
s = t /round(np.tan(np.radians(angle)), 5)
l, = ax[0].plot(t, s, color='r')
 
ax[0].add_patch(Rectangle([-5.0, -1.0], 10, 2))

ax[1].add_patch(Ellipse([0.0, 0.0], 2, 2))
# Create axes for frequency and amplitude sliders
axfreq = plt.axes([0.25, 0.15, 0.65, 0.03])
 
# Create a slider from 0.0 to 20.0 in axes axfreq
# with 3 as initial value
freq = Slider(axfreq, 'Frequency', 0.0, 90.0, 0.0)
 

 
# Create function to be called when slider value is changed
 
def update(val):
    f = freq.val
    l.set_ydata(t /round(np.tan(np.radians(f)), 5))
    ax[1].clear()
    ax[1].set_aspect('equal')
    ax[1].autoscale()
    ax[1].add_patch(Ellipse([0.0, 0.0], 2, f/10))
 
# Call update function when slider value is changed
freq.on_changed(update)
 
# display graph
plt.show()