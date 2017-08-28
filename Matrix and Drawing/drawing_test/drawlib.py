# Drawing Routines, like OpenGL
# Jiazheng Sun
from matlib import *

def gtOrtho(left, right, bottom, top, near, far):
    global check
    check = 1
    global l
    l = left
    global r
    r = right
    global b 
    b = bottom
    global t
    t = top

def gtPerspective(fov, near, far):
    global check
    check = 2
    global k
    k = tan(radians(fov)/2)

def gtBeginShape():
    global coords
    coords = []

def gtEndShape():
    for i in range(0, len(coords), 2):
        line(coords[i][0],coords[i][1],coords[i+1][0],coords[i+1][1])
    print(coords)

def gtVertex(x, y, z):
    original =[[x,0,0,0],
               [y,0,0,0],
               [z,0,0,0],
               [1,0,0,0]]
    m = gtGetCtm()
    final = matrixmul(m, original)
    xtemp = final[0][0]
    ytemp = final[1][0]
    ztemp = final[2][0]
    if check == 1: #Ortho Projection
        newX = (800/(r-l)) * (xtemp-l)
        newY = (800/(b-t)) * (ytemp-t)
    elif check == 2: #Perspective Projection
        x2 = xtemp/abs(ztemp)
        y2 = ytemp/(abs(ztemp)*-1)
        newX = (x2+k)*(800/(2*k))
        newY = (y2+k)*(800/(2*k))
    coords.append((newX, newY))
    
    
        