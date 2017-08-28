# draw initials in perspective
# Jiazheng Sun
from matlib import *
from drawlib import *

def initials():
    gtBeginShape()
    gtVertex(0,20,10)
    gtVertex(40,20,10)
    
    gtVertex(20,20,10)
    gtVertex(20,60,10)
    
    gtVertex(20,60,10)
    gtVertex(0,60,10)
    
    gtVertex(40,20,10)
    gtVertex(80,20,10)
    
    gtVertex(40,20,10)
    gtVertex(40,40,10)
    
    gtVertex(40,40,10)
    gtVertex(80,40,10)
    
    gtVertex(80,40,10)
    gtVertex(80,60,10)
    
    gtVertex(80,60,10)
    gtVertex(40,60,10)

    gtEndShape()

def persp_initials():
    gtInitialize()
    gtPerspective (60, -100, 100)
    gtPushMatrix()
    gtTranslate(0,0,-4)
    gtRotateX(120)
    gtScale(0.01,0.01,0.01)
    initials()
    gtPopMatrix()