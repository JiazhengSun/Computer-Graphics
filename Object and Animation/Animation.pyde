#Jiazheng Sun
#903131864
# Animation Example
time = 0   # use time to move objects from one frame to the next
time_2 = 0
def setup():
    size (800,800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    global img, pb,hrhw, angle, vec, angle_2, check, wall, water, misty, pink, grass, ice
    check = False
    vec = (PI/180) 
    angle = -(PI/4)
    angle_2 = (PI/4)
    img = loadImage("body2.png")
    pb = loadImage("pokeball.jpg")
    hrhw = loadImage("hrhw.jpg")
    wall = loadImage("wall.png")
    water = loadImage("water.png")
    misty = loadImage("misty.png")
    pink = loadImage("pink.png")
    grass = loadImage("grass.png")
    ice = loadImage("ice.png")
    
def draw():
    global time,time_2, angle, vec, angle_2
    
    time += 1
    if time >= 350:
        time_2 += 1 #event two won't happen until 350s of first event
    if (time % 90) == 89: #all rotation handling
        vec *= -1
    angle += vec
    angle_2 -= vec
    cameraMovements() #Camera movements, background changes, background light reflection using directional light

    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    pointLight(200, 200, 200, 0, -500, 0)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    animation_1()
    if time_2 is not 0:
        animation_2()
        animation_3()
    print(time)
    # All events end at around 780 secs


#-------------Camera moves + BG change + BG reflection light using directionlight-----------------------------------#
#DirectionLight(R,G,B, targetX, targetY, targetZ)
def cameraMovements():
    if  time <= 100: #
        directionalLight(51,255,255, 0,0,-100)
        background(water)
        camera (100,-100, 300, 0, 0, 0, 0,  1, 0)  # position the virtual camera
    elif time <= 200:
        directionalLight(255,204,229, 0,0,-200)
        background(pink)
        camera (-200,-200,100, 0, 0, 100*-3.1415926/6 , 0,  1, 0)
    elif time <= 350:
        directionalLight(15,15,15, 0,0,-300)
        background(ice)
        camera (100,-100,-200, 0, 0, 200*-3.1415926/6, 0,  1, 0)
    elif time <= 400:
        directionalLight(178,102,255, 0,0,200)
        background(misty)
        camera (10,-100,-100,  0,0,0,  0,1,0)
    elif time <= 500:
        directionalLight(255,255,153, 0,0,100)
        background(wall)
        camera (100,-200,-400, 0,0,400*-3.1415926/6, 0,1,0)
    elif time <= 600: #500 -- 600
        directionalLight(255,255,153, 0,-100,-300)
        background(wall)
        camera (100,-200,300, 0,0,0,  0,1,0)
    elif time <= 780: #600 -- 700
        directionalLight(255,255,153, 0,-200,100)
        background(wall)
        camera (-100,-200,-300, 0,0,0,  0,1,0)
    else: #Events end. Left rotating camera
        directionalLight(204,255,229, 0,0,400*-3.1415926/6)
        background(grass)
        theta = 60 * PI / 180 #angle of view
        #ratio 1 : sqrt3 : 2, y = 100, so longSide = 200
        camera(400*sin(theta + 0.01* time),-200,-400*cos(theta+0.01 * time), 0,0,-120, 0,1,0)

#--------------------------Animations----------------------------------------------#

def animation_1():
    pushMatrix()
    if time <= 400:
        translate(0,0,time * (-3.1415926/6))
    else:
        translate(0,8 * sin(0.3 * time),400 *(-3.1415926/6) )
    together()
    popMatrix()
    
def animation_2():#Electrode dance for t.length()= 400
    pushMatrix()
    if time <= 780:
        translate (0, 8 * sin(0.15 * time_2), -0.5 * time_2) #y for jump, z for moving forward
        wanpidanMovement()
    else:
        translate(0, 8 * sin(0.15 * time_2), (-0.5 *430)+200) #y for jump, z for set location
        wanpidanTogether()
    popMatrix()

def animation_3(): #Two other Electrodes came after the frist one, to satisfy object instancing.
    pushMatrix()
    if time <= 780:
        pushMatrix() #xiaodi No1 jump
        translate(0, 8 * sin(0.3 * time_2), -0.5 * time_2)
        xiaodi_1_movement()
        popMatrix()
        
        pushMatrix() #xiaodo No2 jump
        translate(0, 8 * sin(0.5 * time_2), -0.5 * time_2)
        xiaodi_2_movement()
        popMatrix()
    else:
        pushMatrix() #xiaodi NO1
        translate(100, 8 * sin(0.3 * time_2), (-0.5 *430)+300)
        wanpidanTogether()
        popMatrix()
        
        pushMatrix() #xiao di NO2
        translate(-100, 8 * sin(0.5 * time_2), (-0.5 *430)+300)
        wanpidanTogether()
        popMatrix()
    popMatrix()

def xiaodi_1_movement():
    pushMatrix()
    translate(100,0,300)
    rotateX(angle_2)
    wanpidanTogether()
    popMatrix()

def xiaodi_2_movement():
    pushMatrix()
    translate(-100,0,300)
    rotateX(time/10)
    wanpidanTogether()
    popMatrix()
#------------Section ends here-----------------------------------------------------#

#------------Below this line is the working electrode with movements---------------#

def wanpidanMovement():
    pushMatrix()
    translate(0,0,200)
    rotateX(angle)
    wanpidanTogether()
    popMatrix()

def wanpidanTogether():
    pushMatrix() #body
    wanpidan()
    popMatrix()
    
    pushMatrix() #right eye
    translate(-5,-5,-29)
    wanpidanEye()
    popMatrix()
    
    pushMatrix() #left eye
    translate(5,-5,-29)
    wanpidanEye()
    popMatrix()
    
    pushMatrix() #left mid eyebrow
    rotateZ(-10*(PI/180))
    translate(4,-10,-30)
    wanpidanMidEyeBrow()
    popMatrix()
    
    pushMatrix() #right mid eyebrow
    rotateZ(10*(PI/180))
    translate(-3,-10,-30)
    scale(1,1.1,1)
    wanpidanMidEyeBrow()
    popMatrix()
    
    pushMatrix() #left upper eyebrow
    translate(8,-13,-30)
    wanpidanUpperEyeBrow()
    popMatrix()
    
    pushMatrix() #right upper eyebrow
    translate(-7.5,-12.5,-30)
    rightUpper()
    popMatrix()
    
    pushMatrix() #Mouth
    translate(0,6.5,-30)
    wanpidanMouth()
    popMatrix()

def wanpidanMouth():
    pushMatrix()
    rotateZ(2.3*PI/4)
    scale(0.05,5,0.05)
    blackball()
    popMatrix()

def rightUpper():
    pushMatrix()
    rotateX(3*(PI/180))
    rotateZ(-PI/4)
    scale(0.15,2.7,0.15)
    blackball()
    popMatrix()

def wanpidanUpperEyeBrow():
    pushMatrix()
    rotateX(2*(PI/180))
    rotateZ(PI/4)
    scale(0.15,2.5,0.15)
    blackball()
    popMatrix()
    
def wanpidanMidEyeBrow():
    pushMatrix()
    scale(0.1,1.01,0.1)
    blackball()
    popMatrix()

def wanpidanEye():
    pushMatrix()
    scale(0.25,0.75,0.25)
    blackball()
    popMatrix()

def wanpidan():
    pushMatrix()
    rotateX(PI/2)
    translate(0,0,-30)
    wanpidanBody()
    popMatrix()

def wanpidanBody(lon = 32):
    global hrhw
    w = 1025
    h = 1025
    #latitude can be anything, but half the longitude makes the most sense
    lat = lon/2
    r = 30
    # assume circle radius of .5
    # t and b are short for top and bottom (lesser or greater z, respectively)
    for j in range(lat):
        #z is in range of 0 to 1 (where 2r = 1)
        phit = float(j)/lat * PI
        phib = float(j+1)/lat * PI 
        #z = (r- cos(phi))/2
        zt = r * (1 - cos(phit))
        zb = r * (1 - cos(phib))
        # radius for each longitude circle is a function of the vertical angle, phi
        rt = r * sin(phit)
        rb = r * sin(phib)
        for i in range(lon):
            theta1 = (i) * 2 * PI / lon
            theta2 = (i + 1) * 2 * PI / lon
            #left side of quad
            x1t = rt*cos(theta1)
            y1t = rt*sin(theta1)
            x1b = rb*cos(theta1)
            y1b = rb*sin(theta1)
            
            #right side of quad
            x2t = rt*cos(theta2)
            y2t = rt*sin(theta2)
            x2b = rb*cos(theta2)
            y2b = rb*sin(theta2)
            
            beginShape(QUADS)
            texture(hrhw)

            u1 = (w/lon) * i
            vt = (h/lat) * j
            u2 = (w/lon) * (i+1)
            vb = (h/lat) * (j+1)
            vertex (x1t, y1t, zt, u1, vt)
            vertex (x1b, y1b, zb, u1, vb)
            vertex (x2b, y2b, zb, u2, vb)
            vertex (x2t, y2t, zt, u2, vt)
            
            endShape(CLOSE)
#---------------Section ends here-----------------------------------------------------------#

        
#----------Below this line, Working poliwhirl on pokeball, time [0-400], move on z axis----------
#----------From z = 0 to z = - 400 * (PI/6)-------------------------------------------------#

def together():
    pushMatrix()
    translate(0,36,0)
    pokeroll()
    popMatrix()
    
    pushMatrix()
    translate(0,-30,0)
    poliwhirl()
    popMatrix()

    
def poliwhirl(): #Comebine everything
    
    pushMatrix() #body
    rotateX(37*PI/180)
    translate(0,-6,0)
    rotateY(-8*PI/180)
    translate(1.1,-10,10)
    rotateZ(183*PI/180)
    rotateX(120*PI/180)
    customSphere()
    popMatrix()    
    
    pushMatrix() #left eye
    translate(-13,-15,5)
    eye()
    popMatrix()
    
    pushMatrix() #left white eye ball
    translate(-13,-15,8)
    whiteball()
    popMatrix()
    
    pushMatrix() #left black eye ball
    translate(-13,-15,10)
    blackball()
    popMatrix()
    
    pushMatrix() #right eye
    translate(13,-15,5)
    eye()
    popMatrix()
    
    pushMatrix() #right white eye ball
    translate(13,-15,8)
    whiteball()
    popMatrix()
    
    pushMatrix() #right black eye ball
    translate(13,-15,10)
    blackball()
    popMatrix()
    
    #intending moving sections

    pushMatrix() #left arm and hand
    translate(-15,3,0)
    rotateZ(-PI/5)
    leftLimb()
    popMatrix()
    
    pushMatrix() #right arm and hand
    translate(15,3,0)
    rotateZ(PI/5)
    rightLimb()
    popMatrix()
    
    pushMatrix() #left leg and foot
    translate(-9.5,18.5,0)
    leftLow()
    popMatrix()
    
    pushMatrix() #right leg and foot
    translate(9.5,18.5,0)
    rightLow()
    popMatrix()


def customSphere(lon = 64): #body
    global img
    w = 280
    h = 130
    #latitude can be anything, but half the longitude makes the most sense
    lat = lon/2
    r = 20
    # t and b are short for top and bottom (lesser or greater z, respectively)
    for j in range(lat):
        #z is in range of 0 to 1 (where 2r = 1)
        phit = float(j)/lat * PI
        phib = float(j+1)/lat * PI 
        #z = (r- cos(phi))/2
        zt = r * (1 - cos(phit))
        zb = r * (1 - cos(phib))
        # radius for each longitude circle is a function of the vertical angle, phi
        rt = r * sin(phit)
        rb = r * sin(phib)
        for i in range(lon):
            theta1 = (i) * 2 * PI / lon
            theta2 = (i + 1) * 2 * PI / lon
            #left side of quad
            x1t = rt*cos(theta1)
            y1t = rt*sin(theta1)
            x1b = rb*cos(theta1)
            y1b = rb*sin(theta1)
            
            #right side of quad
            x2t = rt*cos(theta2)
            y2t = rt*sin(theta2)
            x2b = rb*cos(theta2)
            y2b = rb*sin(theta2)
            
            # specifying quads makes the code more efficient
            beginShape(QUADS)
            texture(img)
            # to add texture, write the vertex call like this:
            # vertex(x, y, z, u, v)
            # where u and v are the x and y locations of a particular point in 
            # your texture image.
            #
            # u should be a function of the latitude, j, and v should
            # be a function of the longitude, i.
            #
            # specifically, 
            # u1 = (width_of_image/lon) * i
            # and 
            # vt = (height_of_image/lat) * j
            #
            # u2 and vb are the same, but with i+1 and j+1 substituted for i and j
            u1 = (w/lon) * i
            vt = (h/lat) * j
            u2 = (w/lon) * (i+1)
            vb = (h/lat) * (j+1)
            vertex (x1t, y1t, zt, u1, vt)
            vertex (x1b, y1b, zb, u1, vb)
            vertex (x2b, y2b, zb, u2, vb)
            vertex (x2t, y2t, zt, u2, vt)
            
            endShape(CLOSE)

def pokeball(lon = 64): #body
    global pb
    w = 1025
    h = 1025
    #latitude can be anything, but half the longitude makes the most sense
    lat = lon/2
    r = 40
    # assume circle radius of .5
    # t and b are short for top and bottom (lesser or greater z, respectively)
    for j in range(lat):
        #z is in range of 0 to 1 (where 2r = 1)
        phit = float(j)/lat * PI
        phib = float(j+1)/lat * PI 
        #z = (r- cos(phi))/2
        zt = r * (1 - cos(phit))
        zb = r * (1 - cos(phib))
        # radius for each longitude circle is a function of the vertical angle, phi
        rt = r * sin(phit)
        rb = r * sin(phib)
        for i in range(lon):
            theta1 = (i) * 2 * PI / lon
            theta2 = (i + 1) * 2 * PI / lon
            #left side of quad
            x1t = rt*cos(theta1)
            y1t = rt*sin(theta1)
            x1b = rb*cos(theta1)
            y1b = rb*sin(theta1)
            
            #right side of quad
            x2t = rt*cos(theta2)
            y2t = rt*sin(theta2)
            x2b = rb*cos(theta2)
            y2b = rb*sin(theta2)
            
            beginShape(QUADS)
            texture(pb)

            u1 = (w/lon) * i
            vt = (h/lat) * j
            u2 = (w/lon) * (i+1)
            vb = (h/lat) * (j+1)
            vertex (x1t, y1t, zt, u1, vt)
            vertex (x1b, y1b, zb, u1, vb)
            vertex (x2b, y2b, zb, u2, vb)
            vertex (x2t, y2t, zt, u2, vt)
            
            endShape(CLOSE)

def pokeroll():
    pushMatrix()
    if time <= 400:
        rotateX(0.01*time)
    translate(0,-40,0)
    rotateZ(PI/2)
    rotateY(PI/2)
    pokeball()
    popMatrix()

def eye(): #draw a small blue sphere serves as an eye
    fill (51, 153, 255)
    pushMatrix()
    sphereDetail(60)
    sphere(6)
    popMatrix()

def arm():
    fill(51, 153, 255)
    pushMatrix()
    rotateY(PI/2)
    scale(4,4,6)
    cylinder()
    popMatrix()

def hand():
    fill (224,224,224)
    pushMatrix()
    sphereDetail(60)
    sphere(7)
    popMatrix()

def rightLimb():
    pushMatrix()
    if time <= 400:
        rotateY(angle_2)
    translate(5,0,0)
    arm()
    translate(10,0,0)
    hand()
    popMatrix()   

def leftLimb():
    pushMatrix()
    if time <= 400:
        rotateY(angle_2)
    translate(-5,0,0)
    arm()
    translate(-10,0,0)
    hand()
    popMatrix()

def leg():
    fill(51, 153, 255)
    pushMatrix()
    rotateX(PI/2)
    scale(3,3,6)
    cylinder()
    popMatrix()

def foot(): #draw a ellpsoid serves as one foot
    fill(51, 153, 255)
    pushMatrix()
    rotateY(80)
    scale(1,0.5,0.5)
    sphereDetail(60)
    sphere(8)
    popMatrix()

def low():
    pushMatrix()
    leg()
    translate(0,6,3)
    foot()
    popMatrix()

def leftLow():
    pushMatrix()
    if time <= 400:
        rotateX(angle)
    low()
    popMatrix()
    
def rightLow():
    pushMatrix()
    if time <= 400:
        rotateX(angle_2)
    low()
    popMatrix()

#------------------------------Section ends here---------------------------------------------------#


#------------------------------Below this line are primitive objects-------------------------------#
def whiteball():
    fill (255,255,255)
    pushMatrix()
    sphereDetail(60)
    sphere(4)
    popMatrix()

def blackball():
    fill (0,0,0)
    pushMatrix()
    sphereDetail(60)
    sphere(3)
    popMatrix()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2