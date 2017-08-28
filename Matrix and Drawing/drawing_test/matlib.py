# Matrix Stack Library
# Jiazheng Sun
def matrixmul(a, b):
    result = [[0,0,0,0], #initialize a random 4*4 matrix
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for i in range(4): #iterate rows of a matrix
        for j in range(4): #iterate columns of b matrix
            for h in range(4): #iterate rows of b matrix
                tmp = a[i][h]*b[h][j]
                result[i][j] += tmp
    return result

def gtInitialize():
    global stack
    id = [[1,0,0,0],
          [0,1,0,0],
          [0,0,1,0],
          [0,0,0,1]]
    stack = [id]

def gtPushMatrix():
    ctm = stack[-1]
    tmp = ctm[:]
    stack.append(tmp)

def gtPopMatrix():
    if len(stack)==1:
        print('There is only identity matrix on the stack. cannot pop the matrix stack')
    else:
        del stack[-1]

def gtGetCtm():
    return stack[-1]

def gtTranslate(x, y, z):
    old_ctm = stack[-1]
    translateMatrix = [[1,0,0,x],
                       [0,1,0,y],
                       [0,0,1,z],
                       [0,0,0,1]]
    new_ctm = matrixmul(old_ctm, translateMatrix)
    if (len(stack) is not 0):
        stack[-1] = new_ctm
    else:
        println('There is only identity matrix left. Please create a new one to do calculation')

def gtScale(x, y, z):
    old_ctm = stack[-1]
    scaleMatrix = [[x,0,0,0],
                   [0,y,0,0],
                   [0,0,z,0],
                   [0,0,0,1]]
    new_ctm = matrixmul(old_ctm, scaleMatrix)
    if (len(stack) is not 0):
        stack[-1] = new_ctm
    else:
        println('There is only identity matrix left. Please create a new one to do calculation')

def gtRotateX(theta):
    old_ctm = stack[-1]
    r = radians(theta)
    rotateXMatrix = [[1,0,0,0],
                     [0,cos(r),-sin(r),0],
                     [0,sin(r),cos(r),0],
                     [0,0,0,1]]
    new_ctm = matrixmul(old_ctm, rotateXMatrix)
    if (len(stack) is not 0):
        stack[-1] = new_ctm
    else:
        println('There is only identity matrix left. Please create a new one to do calculation')

def gtRotateY(theta):
    old_ctm = stack[-1]
    r = radians(theta)
    rotateYMatrix = [[cos(r),0,sin(r),0],
                     [0,1,0,0],
                     [-sin(r),0,cos(r),0],
                     [0,0,0,1]]
    new_ctm = matrixmul(old_ctm, rotateYMatrix)
    if (len(stack) is not 0):
        stack[-1] = new_ctm
    else:
        println('There is only identity matrix left. Please create a new one to do calculation')

def gtRotateZ(theta):
    old_ctm = stack[-1]
    r = radians(theta)
    rotateZMatrix = [[cos(r),-sin(r),0,0],
                     [sin(r),cos(r),0,0],
                     [0,0,1,0],
                     [0,0,0,1]]
    new_ctm = matrixmul(old_ctm, rotateZMatrix)
    if (len(stack) is not 0):
        stack[-1] = new_ctm
    else:
        println('There is only identity matrix left. Please create a new one to do calculation')