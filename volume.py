'''
Date: 06/2023
Coder: Saywer
Purpose: Calculate the section of a cylinder in function of the section angle. 
Display cut and section area.
'''
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
from matplotlib.widgets import Slider

class Circle:
    '''
    Class circle / elipse
    '''
    def area(self, semi_minor_axis, semi_major_axis = None):
        '''
        Area calculation for elipse and circle.
        '''
        if semi_major_axis is None:
            semi_major_axis = semi_minor_axis
        area = math.pi * semi_major_axis * semi_minor_axis
        return area

class Cylinder:
    '''
    Class Cylinder
    '''
    def circle_base_area(self, diameter):
        '''
        Function base area calculation.
        '''
        return Circle().area(diameter/2)

    def volume(self, diameter, height):
        '''
        Function cylinder volume calculation.
        '''
        volume = self.circle_base_area(diameter) * height
        return volume

    def section_dim(self, diameter, section_angle):
        '''
        Function to calculate section dimension according to the cut angle.
        '''
        semi_minor_axis = diameter / 2
        semi_major_axis = semi_minor_axis / round(math.cos(math.radians(section_angle)), 5)
        return semi_minor_axis * 2, semi_major_axis * 2

class Plot:
    '''
    Class Plot to show results 
    '''
    diameter = 1
    length = 10

    def subplot_section(self, axe, angle, diameter):
        width, height = Cylinder().section_dim(diameter, angle)
        ellipse= Ellipse([0.0, 0.0], width, height)
        self.set_axe(axe, ellipse)

    def subplot_cylinder(self, axe, angle, diameter, length):
        cylinder = Rectangle([0.0, 0.0], length, diameter)
        self.set_axe(axe, cylinder)
        axe.axline((length /2 , diameter / 2), slope= 1/round(math.tan(math.radians(angle)), 5), linewidth=4, color='r')

    def set_axe(self, axe, patch):
        axe.add_patch(patch)
        axe.set_aspect('equal')
        axe.autoscale()  

    def figure_content(self, figure):
        axes = figure.subplots(2)
        
        

    def graph(self, angle, diameter = None, length = None):
        '''
        Function Docstring
        '''
        if diameter is None: 
            diameter = self.diameter
        if length is None:
            length = self.length

        figure, axes = plt.subplots(2)
        
        plt.title('Cylinder and section')
        self.subplot_section(axes[0], angle, diameter)
        self.subplot_cylinder(axes[1], angle, diameter, length)

        ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03])
        slider = Slider(ax_slider, 'angle', 0.0, 90.0, 1.0)
        def update(val):
            angle = slider.val
            axes[0].clear()
            axes[1].clear()
            self.subplot_section(axes[0], angle, diameter)
            self.subplot_cylinder(axes[1], angle, diameter, length)
        slider.on_changed(update)
        
        plt.show()

cy = Cylinder()
Plot().graph(80, 10, 2)



'''
    def line (self, t, angle):
        
        l = plt.axline((length /2 , diameter / 2), slope= t /round(math.tan(math.radians(angle)), 5), linewidth=4, color='r')
        l = plt.axline((length /2 , diameter / 2), slope= 1 /round(math.tan(math.radians(angle)), 5), linewidth=4, color='r')
        return amplitude * np.sin(2 * np.pi * frequency * t)
'''

  


