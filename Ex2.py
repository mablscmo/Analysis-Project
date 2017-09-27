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
#c=Planet(4,0,0,4) 
#print(c.getPeriodAndAxis(30,0.01))
#d=Planet(1,0,0,1)
#print(d.getPeriodAndAxis(100,.0001))
#e=Planet(12,0,0,0.2)
#print(e.getPeriodAndAxis(100,.0001))
#f=Planet(2,0,0,4)
#f.plot(20,0.00001)
#g=Planet(2,0,0,2)
#g.plot(20,0.00001)

class PlanetGR:
    
    k=4.*math.pi**2
    
    def __init__(self,x,y,vx,vy,alpha2):
        self.t=0
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.a2=alpha2
#        self.k=k

        
    # Returns distance in AU from the planet to the Sun.
    def getR(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # Returns the angle between the position of the planet and the positive
    # x-axis in the range [0, 2 pi)
    def getAngle(self):
        x = self.x
        y = self.y
        theta = math.atan2(y,x)
        if theta<0:
            theta += 2.*math.pi
        return theta
        
    # Update the position and velocity of the planet using the Euler-Cramer 
    # scheme taking into account first order corrections from General Relativity
    def doTimeStep(self,dt):
        self.vx+=(-self.k*self.x/(((((self.x)**2)+(self.y)**2))**(3/2)))*(1+2*self.a2/3*sqrt(self.x**2+self.y**2))*dt
        self.vy+=(-self.k*self.y/(((((self.x)**2)+(self.y)**2))**(3/2)))*(1+2*self.a2/3*sqrt(self.x**2+self.y**2))*dt
        self.x+=self.vx*dt
        self.y+=self.vy*dt
        self.t+=dt

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
    


    # Returns the precession rate of the perihelion in units of radians per year    
#    def getPerihelionAngularVelocity(self,dt):
        # Complete in exercise 3.6

alpha2=[0,10**(-4),10**(-3),10**(-2)]

figcount = 1
for a2 in alpha2:
    
    # initialize Mercury
    mercury = PlanetGR(0.47,0.,0.,8.2,a2)

    T=mercury.t #
    
    # coordinates of the planet in each time step
    X = [] 
    Y = []
    
    # coordinates of tthe perihelion
    xph = []
    yph = []
    
    # simulate for 2 earth years
    while T<2:
        # Update planet with doTimeStep, and append the x and y coordinates to X and Y
        # Check if the distance to the Sun in the previus step is smaller than both
        # the current distance and the previous to the previous distance. If so,
        # the planet was in the perihelion in the previus step. Append the previous x 
        # and y coordinates to xph and yph
        
    
    plt.figure(figcount,figsize=(8, 8))
    plt.plot(X,Y)
    plt.plot(xph,yph,'ro')
    plt.plot(0,0,'rx')
    lim=0.5
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)

    plt.xlabel("x [AU]")
    plt.ylabel("y [AU]")
    titlestr = "alpha^2 = "+str(a2)
    plt.title(titlestr)
    figcount += 1
