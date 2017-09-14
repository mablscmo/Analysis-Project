# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:11:07 2017
@author: monte
"""
from scipy import *
from pylab import *
import sys    

import math 
import numpy as np

class Planet:
    
    
    
    def __init__(self,x,y,vx,vy,k=4*math.pi**2):
        # Complete in exercise 2.2
        self.t=0
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.k=k
#        self.coord=array([[self.x],[self.y]],[[self.vx],[self.vy]])

    def __repr__(self):
        return'x={}, y={}, vx={}, vy={}'.format(self.x,self.y,self.vx,self.vy)

    def doTimeStep(self,dt):
        # Complete in exercise 2.2
        self.vx+=-self.k*self.x/(((((self.x)**2)+(self.y)**2))**(3/2))
        self.vy+=-self.k*self.y/(((((self.x)**2)+(self.y)**2))**(3/2))
        self.x+=self.vx*dt
        self.y+=self.vy*dt
        self.t+=dt
#        return(array([self.x,self.y],[self.vx,self.vy]))
    def plot(self, maxt, dt):
        (x,y,vx,vy)=(self.x,self.y,self.vx,self.vy)
        xvalues=[self.x]
        yvalues=[self.y]
        for i in linspace(0, maxt, maxt/dt):
            self.doTimeStep(dt)
            xvalues.append(self.x)
            yvalues.append(self.y)
        (self.x,self.y,self.vx,self.vy)=(x,y,vx,vy)
        return(plot(xvalues, yvalues))
        
#    def getPeriodAndAxis(self,dt):
        # COmplete in exercise 2.4
