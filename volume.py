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

    def section_dim(self, section_angle, diameter, height):
        '''
        Function to calculate section dimension according to the cut angle.
        '''
        semi_minor_axis = diameter / 2
        opposite = semi_minor_axis * round(math.tan(math.radians(section_angle)), 5)
        if opposite <= height:
            semi_major_axis = semi_minor_axis / round(math.cos(math.radians(section_angle)), 5)
        elif:
            semi_major_axis = height / round(math.cos(math.radians(90 - section_angle)), 5)

        return semi_minor_axis * 2, semi_major_axis * 2

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
        width, height = Cylinder().section_dim(angle, diameter, length)
        ellipse= Ellipse([0.0, 0.0], width, height)
        self.set_axe(axe, ellipse)
        axe.set_xlim(-height, height)
        axe.set_ylim(-height, height)
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



