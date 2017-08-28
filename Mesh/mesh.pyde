# Sample code for starting the mesh processing project
import dual
import helper
rotate_flag = True    # automatic rotation of model?
time = 0   # keep track of passing time, for automatic rotation
vTable = []
gTable = []
oTable = []
fNormals = []
vNormals = []
colors = []
mode = True
colorCheck = True
# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()

# draw the current mesh
def draw():
    global time, colors
    
    background(0)    # clear screen to black

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (102, 102, 102)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    fill (200,200,200)            # set polygon color
    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
  
    rotate (time, 1.0, 0.0, 0.0)

    # THIS IS WHERE YOU SHOULD DRAW THE MESH
    for i in range(0,len(vTable),3):
        if colorCheck is True:
            fill(255,255,255)
        else:
            face= colors[i/3]
            fill(face[0],face[1],face[2])
        beginShape()
        if mode is True: #Surface normal
            normal(fNormals[i/3].x,fNormals[i/3].y,fNormals[i/3].z)
            vertex (gTable[vTable[i]][0],gTable[vTable[i]][1],gTable[vTable[i]][2])
            vertex (gTable[vTable[i+1]][0],gTable[vTable[i+1]][1],gTable[vTable[i+1]][2])
            vertex (gTable[vTable[i+2]][0],gTable[vTable[i+2]][1],gTable[vTable[i+2]][2])
        else: #Vertex normal
            normal(vNormals[vTable[i]].x,vNormals[vTable[i]].y,vNormals[vTable[i]].z)
            vertex (gTable[vTable[i]][0],gTable[vTable[i]][1],gTable[vTable[i]][2])
            normal(vNormals[vTable[i+1]].x,vNormals[vTable[i+1]].y,vNormals[vTable[i+1]].z)
            vertex (gTable[vTable[i+1]][0],gTable[vTable[i+1]][1],gTable[vTable[i+1]][2])
            normal(vNormals[vTable[i+2]].x,vNormals[vTable[i+2]].y,vNormals[vTable[i+2]].z)
            vertex (gTable[vTable[i+2]][0],gTable[vTable[i+2]][1],gTable[vTable[i+2]][2])            
        endShape(CLOSE)
    
    popMatrix()
    
    # maybe step forward in time (for object rotation)
    if rotate_flag:
        time += 0.02

# process key presses
def keyPressed():
    global rotate_flag, mode, colorCheck,vTable,gTable,oTable,fNormals,vNormals
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == '5':
        read_mesh ('torus.ply')
    elif key == 'n':
        mode = not mode
    elif key == 'r':
        colorCheck = False
    elif key == 'w':
        colorCheck = True
    elif key == 'd':
        answer = dual.genNewTables(vTable, gTable,oTable)
        vTable = answer[0]
        gTable = answer[1]
        oTable = answer[2]
        fNormals = answer[3]
        vNormals = answer[4]
        randomColor()
    elif key == 'q':
        exit()

# read in a mesh file (THIS NEEDS TO BE MODIFIED !!!)
def read_mesh(filename):
    global vTable,gTable,oTable,fNormals,vNormals,colors
    vTable = []
    gTable = []
    oTable = []
    fNormals = []
    vNormals = []
    colors = []
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex = ", x, y, z
        #Geometry table with vertex coordinates
        gTable.append((x,y,z))
        
    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: this face is not a triangle"
            exit()
        
        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "face =", index1, index2, index3
        # Vertex table with corner -> vertex
        vTable.append(index1)
        vTable.append(index2)
        vTable.append(index3)
        
    # Calculate opposite table
    oTable = helper.oTableGene(vTable)
    # Calculate surface normals
    fNormals = helper.surfaceNormalsGene(vTable,gTable)
    # Calculate vertex normals
    vNormals = helper.vertexNormalsGene(vTable,gTable,oTable,fNormals)
    # Random Colored
    randomColor()

# Color Function
def randomColor():
    global colors
    for i in range(len(fNormals)):
        surfaceColor = (random(255),random(255),random(255))
        colors.append(surfaceColor)