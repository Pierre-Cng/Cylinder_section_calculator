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
    
    def vertex_parameter(self, semi_minor_axis, semi_major_axis, section_length):
        abs_x = section_length
        abs_y = np.sqrt(1-((abs_x/semi_major_axis)**2))*semi_minor_axis
        polar_r = np.sqrt((abs_x**2) + (abs_y**2))
        vertex_angle = np.arccos(abs_x/polar_r)
        #vertex_angle = np.pi/2.7
        print('vertex print -----------------')
        print(polar_r)
        print(abs_x, abs_y)
        print(vertex_angle)
        return abs_x, abs_y, vertex_angle

    def curve(self, x, y, lim, semi_minor_axis, semi_major_axis):
        lim = [0, 2*np.pi]
        for i in np.linspace(lim[0], lim[1]):
            x.append(semi_major_axis * np.cos(i))
            y.append(semi_minor_axis * np.sin(i))

    def ellipse_eq(self, semi_minor_axis, semi_major_axis):
        x = []
        y = []
        self.curve(x, y, [0, 2 * np.pi], semi_minor_axis, semi_major_axis)
        return x, y
    
    def tronc_ellipse_eq(self, semi_minor_axis, semi_major_axis, section_length, val):
        x = []
        y = []
        abs_x, abs_y, vertex_angle = self.vertex_parameter(semi_minor_axis, semi_major_axis, section_length)
        for i in range(2):
            pos_neg = 1 - 2 * i 
            if val == 1: 
                for tuple in [(pos_neg,-pos_neg), (pos_neg,pos_neg)]:
                    x.append(tuple[0] * abs_x)
                    y.append(tuple[1] * abs_y) 
            if val == 2:
                self.curve(x, y, [vertex_angle - 0 * np.pi, (1 - 0) * np.pi - vertex_angle], semi_minor_axis, semi_major_axis)
            if val == 3:
                return abs_x, abs_y
        return x, y
    '''
     for i in range (2):
            for j in range(2):
                self.extrem_point(x, y, 1 - 2 * i, 1 - 2 * j, semi_minor_axis, cut_length, max_length)
            self.curve(x, y, [self.t_limit(cut_length, max_length) - i * np.pi, (1 - i) * np.pi -self.t_limit(cut_length, max_length)], semi_minor_axis, semi_major_axis)
        return x, y'''
    

    
    def rectangle_eq(self, semi_height, semi_width):
        x = []
        y = []
        for tuple in [(1,-1), (1,1), (-1,1), (-1,-1), (1,-1)]:
                x.append(tuple[0] * semi_width)
                y.append(tuple[1] * semi_height) 
        return x, y 
           

    def section_dim(self, section_angle, diameter, cylinder_length):
        '''
        Function to calculate section dimension according to the cut angle.
        '''
        semi_minor_axis = diameter / 2
        if section_angle < 90:
            semi_major_axis = semi_minor_axis / round(math.cos(math.radians(section_angle)), 5)
        opposite = semi_minor_axis * round(math.tan(math.radians(section_angle)), 5)

        if opposite <= cylinder_length:
            return self.ellipse_eq(semi_minor_axis, semi_major_axis)
        else:
            section_length = cylinder_length / round(math.cos(math.radians(90 - section_angle)), 5)
            if section_angle == 90:
                return self.rectangle_eq(semi_minor_axis, section_length)
            else:
                return self.tronc_ellipse_eq(semi_minor_axis, semi_major_axis, section_length)
            
            

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
        axe.set_xlim(- diameter, diameter)
        axe.plot(y, x)
        axe.set_title('Section shape')

    def subplot_cylinder(self, axe, angle, diameter, length):
        '''
        Function to draw a rectangle (cylinder side view) and a line (cutting line) to the given subplot according to parameters.
        '''
        axe.add_patch(Rectangle([-length/2, -diameter/2], length, diameter))
        axe.set_aspect('equal')
        axe.autoscale()  
        self.section_line(axe, angle, diameter)
        axe.set_title('Cylinder side view and section line')

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

#Plot().graph(0.1, 1, 10)

x, y = Cylinder().tronc_ellipse_eq(5, 25.866528711846872, 10.001900361068603, 1)
plt.plot(x,y)
x, y = Cylinder().tronc_ellipse_eq(5, 25.866528711846872, 10.001900361068603, 2)
plt.plot(x,y)
x, y = Cylinder().tronc_ellipse_eq(5, 25.866528711846872, 10.001900361068603, 3)
print(x, y)

plt.show()