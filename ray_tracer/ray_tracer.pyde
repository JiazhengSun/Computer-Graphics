#Jiazheng Sun

def setup():
    global bgg, bgr, bgb, balls, fov, pointlights, surface, polygons, tri
    size(500, 500)
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)
    bgr = 0.0  # First initialize
    bgg = 0.0
    bgb = 0.0
    balls = []
    fov = 0
    pointlights = []
    polygons = []
    tri = None
    surface = None

# read and interpret the appropriate scene description .cli file based on
# key press
def keyPressed():
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        print("6")
        interpreter("i6.cli")
    elif key == '7':
        print("7")
        interpreter("i7.cli")
    elif key == '8':
        print("8")
        interpreter("i8.cli")
    elif key == '9':
        print("9")
        interpreter("i9.cli")
    elif key == '0':
        print("10")
        interpreter("i10.cli")

def interpreter(fname):
    global balls, fov, bgr, bgg, bgb, pointlights, surface, polygons, tri
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            ball = create_sphere(radius, x, y, z, surface)
            balls.append(ball)
            # call your sphere creation routine here
            # for example: create_sphere(radius,x,y,z)
        elif words[0] == 'fov':
            angle = float(words[1])
            fov = radians(angle)
        elif words[0] == 'background':
            bgr = float(words[1])
            bgg = float(words[2])
            bgb = float(words[3])
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            light = create_light(x, y, z, r, g, b)
            pointlights.append(light)
        elif words[0] == 'surface':
            cdr = float(words[1])
            cdg = float(words[2])
            cdb = float(words[3])
            car = float(words[4])
            cag = float(words[5])
            cab = float(words[6])
            csr = float(words[7])
            csg = float(words[8])
            csb = float(words[9])
            p = float(words[10])
            krefl = float(words[11])
            surface = create_surface(
                cdr, cdg, cdb, car, cag, cab, csr, csg, csb, p, krefl)
        elif words[0] == 'begin':
            global vxs  # A list stores vertices as tuples
            vxs = []
        elif words[0] == 'vertex':
            # vxs = [(xa,ya,za),(xb,yb,cb),(xc,yc,zc)]
            vxs.append((float(words[1]), float(words[2]), float(words[3])))
        elif words[0] == 'end':
            newTriangle = triangleShape(vxs[0][0], vxs[0][1], vxs[0][2],
                                        vxs[1][0], vxs[1][1], vxs[1][2],
                                        vxs[2][0], vxs[2][1], vxs[2][2], surface)
            # polygons = [[vxs1,surface],[vxs2],[vxs3]] Each vxs is a triangle
            polygons.append(newTriangle)
        elif words[0] == 'write':
            print("Start Excecuting!!!")
            render_scene()    # render the scene
            print("Finish Excecuting!!!")

            save(words[1])    # write the image to a file

# render the ray tracing scene
def render_scene():
    global balls, fov, bgr, bgg, bgb, pointlights,polygons
    for j in range(height):  # j - y
        for i in range(width):  # i - x
            intersectionList = []
            # create an eye ray for pixel (i,j) and cast it into the scene
            k = tan(fov / 2)
            eyeRay = create_ray(0.0, 0.0, 0.0, i, j, k)
#------------Triangle collision detection------#
            for tri in polygons:
                hitPoint = triHitDection(eyeRay, tri)
                if hitPoint[1] is True:
                    intersectionList.append((hitPoint[0], tri))
#------------Sphere collision detection-------#
            for ball in balls:
                # hitPoint = [(x,y,z),boolean]
                hitPoint = ballHitDection(eyeRay, ball)
                if hitPoint[1] is True:
                    intersectionList.append((hitPoint[0], ball))
#-----------------rendering with color-------------------#
            closestSet = minPointWithSurfaceNormal(intersectionList)
            theColor = getColor(closestSet,eyeRay)
            if closestSet[0] is None:
                pix_color = color(bgr,bgg,bgb)
            else:
                chosenObject = closestSet[3]   
                chosenSurface = closestSet[2]
                surface_normal = closestSet[1]
                temp = closestSet[0]
                negativeEye = PVector(-eyeRay.directionArray[0],-eyeRay.directionArray[1],-eyeRay.directionArray[2])
                rsum = theColor[0]
                gsum = theColor[1]
                bsum = theColor[2]
        #------------------------------------------Implement reflections-------------------------------------------#
                depth = 0
                krefl = chosenSurface.krefl
                reflectedColor = reflect(
                    depth, krefl, temp, negativeEye, surface_normal,chosenObject,rsum,gsum,bsum)
                # you should calculate the correct pixel color here
                rsum = reflectedColor[0]
                gsum = reflectedColor[1]
                bsum = reflectedColor[2]
                pix_color = color(rsum, gsum, bsum)
            #fill the pixel with the calculated color
            set(i, j, pix_color)

#--------------clear to get ready for next render--------------#
    bgr = 0.0
    bgg = 0.0
    bgb = 0.0
    balls = []
    fov = 0
    pointlights = []
    polygons = []
    tri = None
    surface = None

def draw():
    pass
#--------------------------Routine methods-------------------------#
def reflect(depth, krefl, temp, negativeEye, surface_normal,chosenObject,rr,rg,rb):
    global balls, polygons,bgr,bgg,bgb
    reflectIntersectionList = []
    starting_object = chosenObject
    initialR = rr
    initialG = rg
    initialB = rb
    current_krefl = krefl
    if depth < 10 and krefl > 0:
        direction = PVector.sub(PVector.mult(surface_normal, (negativeEye.dot(surface_normal)*2)), negativeEye).normalize()
        epl = 0.01
        ox = temp[0]+surface_normal.x*epl
        oy = temp[1]+surface_normal.y*epl
        oz = temp[2]+surface_normal.z*epl
        reflectionRay = create_secondRay(ox,oy,oz,ox+direction.x, oy+direction.y, oz+direction.z)
        for poly in polygons:
            hitPoint = triHitDection(reflectionRay, poly)
            if hitPoint[1] is True and poly is not chosenObject:
                reflectIntersectionList.append((hitPoint[0], poly))
        for ball in balls:               # hitPoint = [(x,y,z),boolean]
            hitPoint = ballHitDection(reflectionRay, ball)
            if hitPoint[1] is True and ball is not chosenObject:
                reflectIntersectionList.append((hitPoint[0], ball))
        reflectedResult = minPointWithSurfaceNormal(reflectIntersectionList)
        #reflectedResult = [(intersectedPoint,surface_normal,intersectedSurface,intersectedObject)]
        #or [None,None]
        if reflectedResult[0] is None:
            return (krefl*bgr+initialR,krefl*bgg+initialG,krefl*bgb+initialB)
        else:
            depth += 1
            chosenObject = reflectedResult[3]
            surface_normal = reflectedResult[1]
            temp = reflectedResult[0]
            krefl = chosenObject.surface.krefl
            negateRay = PVector(-reflectionRay.directionVector.x,-reflectionRay.directionVector.y,-reflectionRay.directionVector.z)
            negateRay.normalize()
            interceptedColor = getColor(reflectedResult,reflectionRay)
            reflectedColor = reflect(depth, krefl, temp, negateRay, surface_normal,chosenObject,interceptedColor[0],interceptedColor[1],interceptedColor[2])
            #Krefl should multiply with reflected color
            reflectedRed = interceptedColor[0] + reflectedColor[0]* krefl + initialR
            reflectedGreen = interceptedColor[1] + reflectedColor[1]* krefl + initialG
            reflectedBlue = interceptedColor[2]  + reflectedColor[2]* krefl + initialB
            return (reflectedRed,reflectedGreen,reflectedBlue)
    return(initialR,initialG,initialB)

def getColor(closestSet,eyeRay):
    global pointlights
    temp = closestSet[0]
    redSum = 0.0
    blueSum = 0.0
    greenSum = 0.0
    tr = 0.0
    tg = 0.0
    tb = 0.0
    negativeEye = PVector(-eyeRay.directionVector.x,-eyeRay.directionVector.y,-eyeRay.directionVector.z)
    if temp is None:
        return (bgr,bgg,bgb)
    else:
        surface_normal = closestSet[1]
        chosenSurface = closestSet[2]
        beta = closestSet[3] #chosen object
#Shading----------------------------------#
        for pl in pointlights:
            plVec = PVector(
                pl.position[0] - temp[0], pl.position[1] - temp[1], pl.position[2] - temp[2])
            plVec.normalize()
            h = plVec.copy()
            negativeEye = PVector(-eyeRay.directionVector.x, -eyeRay.directionVector.y, -eyeRay.directionVector.z)
            h.add(negativeEye)
            h.normalize()
            negativeEye.normalize()
            p = chosenSurface.phong

            # implement Shadow rays here to determine diffuse and
            # specular
            finalColor = shadowRay(
                surface_normal, temp, beta, pl, chosenSurface, plVec, h, p, redSum, greenSum, blueSum)
            tr += finalColor[0]
            tg += finalColor[1]
            tb += finalColor[2]
        redSum = chosenSurface.ambient_color[0] + tr
        greenSum = chosenSurface.ambient_color[1] + tg
        blueSum = chosenSurface.ambient_color[2] + tb
        return (redSum,greenSum,blueSum)

def minPointWithSurfaceNormal(reflectIntersectionList):
    global bgr,bgg,bgb
    tmin = float("inf")
    intersectedPoint = None
    intersectedObject = None
    intersectedSurface = None
    for p in reflectIntersectionList:
        if p[0][3] > 0 and p[0][3] < tmin:
            tmin = p[0][3]  # update tmin
            intersectedPoint = p[0]
            intersectedObject = p[1]
            intersectedSurface = intersectedObject.surface
    if intersectedPoint is None:
        return (None,False)
    else:
        if (intersectedObject.sp is False):  # sphere
            surface_normal = PVector(
                intersectedPoint[0] - intersectedObject.center[0], intersectedPoint[1] - intersectedObject.center[1], intersectedPoint[2] - intersectedObject.center[2])
        elif(intersectedObject.sp is True):  # Triangle
            bc = PVector(intersectedObject.pointC[0] - intersectedObject.pointB[0], intersectedObject.pointC[1] - intersectedObject.pointB[1], intersectedObject.pointC[2] - intersectedObject.pointB[2])
            ac = PVector(intersectedObject.pointC[0] - intersectedObject.pointA[0], intersectedObject.pointC[1] - intersectedObject.pointA[1], intersectedObject.pointC[2] - intersectedObject.pointA[2])
            surface_normal = bc.cross(ac)
        surface_normal.normalize()
        return (intersectedPoint,surface_normal,intersectedSurface,intersectedObject)



def shadowRay(surface_normal, pt, obj, pl, chosenSurface, plVec, h, p, redSum, greenSum, blueSum):
    global balls, polygons
    epl = 0.01
    ox = pt[0] + surface_normal.x * epl
    oy = pt[1] + surface_normal.y * epl
    oz = pt[2] + surface_normal.z * epl
    blocked = False
    secondRay = create_secondRay(
        ox, oy, oz, pl.position[0], pl.position[1], pl.position[2])
    shadowIntersectionList = []
    for indiball in balls:
        hitResult = ballHitDection(secondRay,indiball)
        if hitResult[1] is True and indiball is not obj:
            shadowIntersectionList.append((hitResult[0],indiball))
    for polygon in polygons:
        hitResult = triHitDection(secondRay,polygon)
        if hitResult[1] is True and polygon is not obj:
            shadowIntersectionList.append((hitResult[0],polygon))
    closestHit = minPointWithSurfaceNormal(shadowIntersectionList)
    if closestHit[0] is not None:
        hp = closestHit[0] #hp is hitpoint
        hpx = hp[0]
        hpy = hp[1]
        hpz = hp[2]
        vectHit = PVector(hpx,hpy,hpz)
        vectRay = PVector(ox,oy,oz)
        vectLight = PVector(pl.position[0], pl.position[1], pl.position[2])
        distBetweenRayAndHit = vectRay.dist(vectHit)
        distBetweenRayAndLight = vectRay.dist(vectLight)
        if distBetweenRayAndHit <= distBetweenRayAndLight:
            blocked = True
    if blocked is False:  # Not blocked, add in specular and diffuse color
        redSum += (chosenSurface.diffuse_color[0] * max(0, surface_normal.dot(plVec))
                   + chosenSurface.specular_color[0] * max(0, surface_normal.dot(h)) ** p) * pl.color_of_light[0]
        greenSum += (chosenSurface.diffuse_color[1] * max(0, surface_normal.dot(plVec))
                     + chosenSurface.specular_color[1] * max(0, surface_normal.dot(h)) ** p) * pl.color_of_light[1]
        blueSum += (chosenSurface.diffuse_color[2] * max(0, surface_normal.dot(plVec))
                    + chosenSurface.specular_color[2] * max(0, surface_normal.dot(h)) ** p) * pl.color_of_light[2]
    return (redSum, greenSum, blueSum)

def triHitDection(ray, tri):
    xd = ray.directionArray[0]
    yd = ray.directionArray[1]
    zd = ray.directionArray[2]
    xe = ray.centerX
    ye = ray.centerY
    ze = ray.centerZ

    xa = tri.pointA[0]
    xb = tri.pointB[0]
    xc = tri.pointC[0]
    ya = tri.pointA[1]
    yb = tri.pointB[1]
    yc = tri.pointC[1]
    za = tri.pointA[2]
    zb = tri.pointB[2]
    zc = tri.pointC[2]

    matrixBeta = [[xa - xe, xa - xc, xd],
                  [ya - ye, ya - yc, yd],
                  [za - ze, za - zc, zd]]

    matrixGamma = [[xa - xb, xa - xe, xd],
                   [ya - yb, ya - ye, yd],
                   [za - zb, za - ze, zd]]

    matrixT = [[xa - xb, xa - xc, xa - xe],
               [ya - yb, ya - yc, ya - ye],
               [za - zb, za - zc, za - ze]]

    matrixA = [[xa - xb, xa - xc, xd],
               [ya - yb, ya - yc, yd],
               [za - zb, za - zc, zd]]

    dtmA = dtm(matrixA)
    if dtmA == 0.0:
        return [None, False]
    else:
        betaa = dtm(matrixBeta) / dtmA
        gamma = dtm(matrixGamma) / dtmA
        t = dtm(matrixT) / dtmA
        ipx = xe + t * ray.directionArray[0]  # hitpoint
        ipy = ye + t * ray.directionArray[1]
        ipz = ze + t * ray.directionArray[2]
        hitpoint = (ipx, ipy, ipz, t)
        if betaa >= 0 and gamma >= 0 and (betaa + gamma) <= 1 and t>0:  # check
            return [hitpoint, True]
        else:
            return [None, False]

def ballHitDection(ray, ball):
    dx = ray.directionArray[0]
    dy = ray.directionArray[1]
    dz = ray.directionArray[2]
    x0 = ray.centerX
    y0 = ray.centerY
    z0 = ray.centerZ
    cx = ball.center[0]
    cy = ball.center[1]
    cz = ball.center[2]
    r = ball.r
    a = dx ** 2 + dy ** 2 + dz ** 2
    b = 2.0 * ((x0 * dx - cx * dx) + (y0 * dy - cy * dy) + (z0 * dz - cz * dz))
    c = (x0 - cx) ** 2 + (y0 - cy) ** 2 + (z0 - cz) ** 2 - r ** 2
    root_check = b ** 2 - 4 * a * c
    if root_check > 0:  # two intersects
        t_1 = (-1 * b + sqrt(root_check)) / (2 * a)
        t_2 = (-1 * b - sqrt(root_check)) / (2 * a)
        x_t_1 = (x0 + t_1 * dx)
        y_t_1 = (y0 + t_1 * dy)
        z_t_1 = (z0 + t_1 * dz)
        x_t_2 = (x0 + t_2 * dx)
        y_t_2 = (y0 + t_2 * dy)
        z_t_2 = (z0 + t_2 * dz)
        point_1 = (x_t_1, y_t_1, z_t_1, t_1)
        point_2 = (x_t_2, y_t_2, z_t_2, t_2)
        if t_1 < 0 and t_2 < 0:
            return [None, False]
        elif t_1 < 0 and t_2 > 0:
            return [point_2, True]
        elif t_1 > 0 and t_2 < 0:
            return [point_1, True]
        else:
            if t_1 < t_2:
                return [point_1, True]
            else:
                return [point_2, True]
    elif root_check == 0:  # one intersect
        t = (-1 * b + sqrt(root_check)) / (2 * a)
        x_t = (x0 + t * dx)
        y_t = (y0 + t * dy)
        z_t = (z0 + t * dz)
        point_t = (x_t, y_t, z_t, t)
        if t <0:
            return (None,False)
        return [point_t, True]
    else:
        return [None, False]

def dtm(m):
    # matrix=[[x1,y1,z1],
    #         [x2,y2,z2],
    #         [x3,y3,z3]]
    x = (m[0][0] * m[1][1] * m[2][2]) + \
        (m[0][1] * m[1][2] * m[2][0]) + (m[0][2] * m[1][0] * m[2][1])
    y = (m[0][2] * m[1][1] * m[2][0]) + \
        (m[0][1] * m[1][0] * m[2][2]) + (m[0][0] * m[1][2] * m[2][1])
    return x - y

#------Class files---------#
class create_sphere:

    def __init__(self, r, x, y, z, s):
        self.r = r  # radius of the sphere
        self.center = (x, y, z)
        self.surface = s
        self.sp = False

class create_light:

    def __init__(self, x, y, z, r, g, b):
        self.position = (x, y, z)
        self.color_of_light = (r, g, b)

class create_surface:

    def __init__(self, cdr, cdg, cdb, car, cag, cab, csr, csg, csb, p, krefl):
        self.diffuse_color = (cdr, cdg, cdb)
        self.ambient_color = (car, cag, cab)
        self.specular_color = (csr, csg, csb)
        self.phong = p
        self.krefl = krefl

class triangleShape:

    def __init__(self, xa, ya, za, xb, yb, zb, xc, yc, zc, surface):
        self.pointA = (xa, ya, za)
        self.pointB = (xb, yb, zb)
        self.pointC = (xc, yc, zc)
        self.surface = surface
        self.sp = True

class create_secondRay:

    def __init__(self, ox, oy, oz, ex, ey, ez):
        self.center = (ox, oy, oz)
        self.centerX = ox
        self.centerY = oy
        self.centerZ = oz
        self.center = (ox, oy, oz)
        # direction = vector(dest - origin)
        dirt = PVector(ex - ox, ey - oy, ez - oz)
        dirt.normalize()
        self.directionArray = dirt.array()
        self.directionVector = dirt
        self.directionTuple = (ex - ox, ey - oy, ez - oz)


class create_ray:

    def __init__(self, ox, oy, oz, i, j, k):
        self.center = (ox, oy, oz)
        self.centerX = ox
        self.centerY = oy
        self.centerZ = oz
        i_1 = i / abs(-1.0)
        j_1 = (height - j) / abs(-1)
        i_2 = (i_1 - (width / 2)) * ((2 * k) / width)
        j_2 = (j_1 - (height / 2)) * ((2 * k) / height)
        z_2 = -1.0
        rawDict = PVector(i_2, j_2, z_2)
        rawDict.normalize()
        self.directionArray = rawDict.array()
        self.directionVector = rawDict
        self.directionTuple = (i_2, j_2, z_2)