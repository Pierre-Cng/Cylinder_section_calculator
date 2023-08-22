'''
Date: 06/2023
Coder: Saywer
Purpose: Calculate the section of a cylinder in function of the section angle. 
Display cut and section area.
'''
import math
import numpy as np
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
    
    def t_limit(self, semi_major_axis, max_length):
        return np.arccos(max_length / semi_major_axis)
    
    def extrem_point(self, x, y, coef_a, coef_b, semi_minor_axis, semi_major_axis, max_length):
        x.append(coef_a * max_length)
        y.append(coef_b * np.sqrt(1-((max_length/semi_major_axis)**2))*semi_minor_axis)

    def curve(self, x, y, lim, semi_minor_axis, semi_major_axis):
        for i in np.linspace(lim[0], lim[1]):
            x.append(semi_major_axis * np.cos(i))
            y.append(semi_minor_axis * np.sin(i))

    def ellipse_eq(self, semi_minor_axis, semi_major_axis):
        x = []
        y = []
        self.curve(x, y, [0, 2 * np.pi], semi_minor_axis, semi_major_axis)
        return x, y
    
    def tronc_ellipse_eq(self, semi_minor_axis, semi_major_axis, cut_length, max_length):
        x = []
        y = []
        for i in range (2):
            for j in range(2):
                self.extrem_point(x, y, 1 - 2 * i, 1 - 2 * j, semi_minor_axis, cut_length, max_length)
            self.curve(x, y, [self.t_limit(cut_length, max_length) - i * np.pi, (1 - i) * np.pi -self.t_limit(cut_length, max_length)], semi_minor_axis, semi_major_axis)
        return x, y
    
    def rectangle_eq(self, semi_minor_axis, semi_major_axis):
        x = []
        y = []
        for tuple in [(1,-1), (1,1), (-1,1), (-1,-1), (1,-1)]:
                x.append(tuple[0] * semi_major_axis)
                y.append(tuple[1] * semi_minor_axis) 
        return x, y 
           

    def section_dim(self, section_angle, diameter, height):
        '''
        Function to calculate section dimension according to the cut angle.
        '''
        semi_minor_axis = diameter / 2
        opposite = semi_minor_axis * round(math.tan(math.radians(section_angle)), 5)
        if opposite <= height:
            semi_major_axis = semi_minor_axis / round(math.cos(math.radians(section_angle)), 5)
            return self.ellipse_eq(semi_minor_axis, semi_major_axis)
        else:
            cut_length = height / round(math.cos(math.radians(90 - section_angle)), 5)
            semi_major_axis = semi_minor_axis / round(math.cos(math.radians(section_angle)), 5)
            return self.tronc_ellipse_eq(semi_minor_axis, semi_major_axis, cut_length, height)
            '''else: 
            return self.rectangle_eq(semi_minor_axis, height)'''

class Plot:
    '''
    Class Plot to build a figure and show results 
    '''
    diameter = 1
    length = 10

    def section_line(self, axe, angle, diameter):
        '''
        Function to add the section line in the given subplot according to parameters.
        '''
        if angle == 0:
            axe.vlines(x=0, ymin=-diameter/2, ymax=diameter/2, linewidth=2, linestyle = 'dashed', color='r')
        else:
            axe.axline((0 , 0), slope= 1/round(math.tan(math.radians(angle)), 5), linewidth=2, linestyle = 'dashed', color='r')

    def subplot_section(self, axe, angle, diameter, length):
        '''
        Function to draw an ellipse in the given subplot according to parameters.
        '''
        x, y = Cylinder().section_dim(angle, diameter, length)
        axe.axis('square')
        axe.plot(y, x)
        axe.set_title('Section shape')

    def subplot_cylinder(self, axe, angle, diameter, length):
        '''
        Function to draw a rectangle (cylinder side view) and a line (cutting line) to the given subplot according to parameters.
        '''
        cylinder = Rectangle([-length/2, -diameter/2], length, diameter)
        self.set_axe(axe, cylinder)
        self.section_line(axe, angle, diameter)
        axe.set_title('Cylinder side view and section line')

    def set_axe(self, axe, patch):
        '''
        Function to add patch (ellipse, rectangle or other shape) to given subplot.
        '''
        axe.add_patch(patch)
        axe.set_aspect('equal')
        axe.autoscale()  


    def graph(self, angle, diameter = None, length = None):
        '''
        Function to build a figure, add subplot, add a slider and refresh the results in case of change
        '''
        if diameter is None: 
            diameter = self.diameter
        if length is None:
            length = self.length

        figure, axes = plt.subplots(2, figsize=(10,7))
        figure.tight_layout()
        figure.subplots_adjust(bottom=0.1)
        self.subplot_section(axes[0], angle, diameter, length)
        self.subplot_cylinder(axes[1], angle, diameter, length)

        ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03])
        slider = Slider(ax_slider, 'angle', 0.0, 90.0, 1.0)
        def update(val):
            angle = slider.val
            axes[0].clear()
            axes[1].clear()
            self.subplot_section(axes[0], angle, diameter, length)
            self.subplot_cylinder(axes[1], angle, diameter, length)
        slider.on_changed(update)
        plt.show()

Plot().graph(0.1, 1, 10)

'''x, y = Cylinder().tronc_ellipse_eq(8, 8, 8)
plt.plot(x,y)
plt.show()'''