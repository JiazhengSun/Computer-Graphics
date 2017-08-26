#Jiazheng Sun
# Animation Example
time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    global img
    img = loadImage("body2.png")
    
def draw():
    global time
    time += 0.01
    
    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    rotateY(time*3)
    rotateX(time)
    poliwhirl()
    
def poliwhirl(): #Comebine everything
    pushMatrix()
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
    
    pushMatrix() #left arm
    translate(-22,2,0)
    rotateZ(-0.5)
    arm()
    popMatrix()
    
    pushMatrix() #right arm
    translate(22,2,0)
    rotateZ(0.5)
    arm()
    popMatrix()
    
    pushMatrix() #left hand
    translate(-30,6,0)
    hand()
    popMatrix()
    
    pushMatrix() #right hand
    translate(30,6,0)
    hand()
    popMatrix()
    
    pushMatrix() #left leg
    translate(-10,19,0)
    leg()
    popMatrix()
    
    pushMatrix() #right leg
    translate(10,19,0)
    leg()
    popMatrix()
    
    pushMatrix() #left foot
    translate(-10,25,3)
    foot()
    popMatrix()
    
    pushMatrix() #right foot
    translate(10,25,3)
    foot()
    popMatrix()

def customSphere(lon = 64):
    global img
    w = 280
    h = 130
    #latitude can be anything, but half the longitude makes the most sense
    lat = lon/2
    r = 20
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

def eye(): #draw a small blue sphere serves as an eye
    fill (51, 153, 255)
    pushMatrix()
    sphereDetail(60)
    sphere(6)
    popMatrix()
    
def foot(): #draw a ellpsoid serves as one foot
    fill(51, 153, 255)
    pushMatrix()
    rotateY(80)
    scale(1,0.5,0.5)
    sphereDetail(60)
    sphere(8)
    popMatrix()

def arm():
    fill(51, 153, 255)
    pushMatrix()
    rotateY(PI/2)
    scale(4,4,6)
    cylinder()
    popMatrix()

def leg():
    fill(51, 153, 255)
    pushMatrix()
    rotateX(PI/2)
    scale(3,3,6)
    cylinder()
    popMatrix()

def hand():
    fill (224,224,224)
    pushMatrix()
    sphereDetail(60)
    sphere(7)
    popMatrix()

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