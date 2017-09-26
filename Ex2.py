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

    def __repr__(self):
        return'x={}, y={}, vx={}, vy={}'.format(self.x,self.y,self.vx,self.vy)

    def doTimeStep(self,dt):
        # Complete in exercise 2.2
        self.vx+=-self.k*self.x/(((((self.x)**2)+(self.y)**2))**(3/2))*dt
        self.vy+=-self.k*self.y/(((((self.x)**2)+(self.y)**2))**(3/2))*dt
        self.x+=self.vx*dt
        self.y+=self.vy*dt
        self.t+=dt
#        return(array([self.x,self.y],[self.vx,self.vy]))
    def plot(self, maxt, dt):
        (x,y,vx,vy)=(self.x,self.y,self.vx,self.vy)
        xvalues=[self.x]
        yvalues=[self.y]
        for i in linspace(dt, maxt, maxt/dt):
            self.doTimeStep(dt)
            xvalues.append(self.x)
            yvalues.append(self.y)
        (self.x,self.y,self.vx,self.vy)=(x,y,vx,vy)
        return(plot(xvalues, yvalues, 'bx', markersize=1))
        
    def getPeriodAndAxis(self,maxt,dt):
        xstart=self.x
        (x,y,vx,vy)=(self.x,self.y,self.vx,self.vy)
        self.t=0
        for i in linspace(dt, maxt, maxt/dt):
            self.doTimeStep(dt)
            if self.x<0 and self.y<0:
                break
            else:
                continue
        T=(round(2*self.t, 3))
        a=(round((abs(xstart)+abs(self.x))/2, 3))
        (self.x,self.y,self.vx,self.vy)=(x,y,vx,vy)
        return('Period is {} units, semi-major axis has a length of {} units, quotient is {}'.format(T,a,T**2/(a**3)))
        
#Tested with these planets    
c=Planet(4,0,0,4) 
print(c.getPeriodAndAxis(30,0.01))
d=Planet(1,0,0,1)
print(d.getPeriodAndAxis(100,.0001))



