def vertexNormalsGene(vTable,gTable,oTable,fNormals):
    checkList = []
    vNormals = []
    for i in range(len(gTable)):
        vNormals.append(0)
    for corner in range(len(vTable)):
        if vTable[corner] not in checkList:
            triNumber = corner/3
            checkList.append(vTable[corner])
            normalSum = 0
            normalSum = fNormals[triNumber].copy()
            adjacent = adjCorner(corner,oTable)
            while (adjacent != corner):
                normalSum.add(fNormals[adjacent/3])
                adjacent = adjCorner(adjacent,oTable)
            normalSum.normalize()
            vNormals[vTable[corner]] = normalSum
    return vNormals

def surfaceNormalsGene(vTable,gTable):
    fNormals = []
    for i in range(0,len(vTable),3):
        chosenCorner = vTable[i]
        chosenVertex = gTable[chosenCorner]
        chosenNext = nextCorner(i)
        nextVertex = gTable[vTable[chosenNext]]
        chosenPrev = prevCorner(i)
        prevVertex = gTable[vTable[chosenPrev]]
        #clockwise * counterclockwise
        a = PVector(chosenVertex[0],chosenVertex[1],chosenVertex[2])
        b = PVector(nextVertex[0],nextVertex[1],nextVertex[2])
        c = PVector(prevVertex[0],prevVertex[1],prevVertex[2])
        # a top, b left, c right. should be ac * ab
        ac = c.copy()
        ac.sub(a)
        ab = b.copy()
        ab.sub(a)
        surfaceNormal = ac.cross(ab)
        surfaceNormal.normalize()
        fNormals.append(surfaceNormal)
    return fNormals

def oTableGene(vTable):
    oTable = []
    for i in range(len(vTable)):
        oTable.append(0)
    for corner_1 in range(len(vTable)):
        for corner_2 in range(len(vTable)):
            anv = vTable[nextCorner(corner_1)]
            bpv = vTable[prevCorner(corner_2)]
            apv = vTable[prevCorner(corner_1)]
            bnv = vTable[nextCorner(corner_2)]
            if (anv == bpv and apv == bnv):
                oTable[corner_1] = corner_2
                oTable[corner_2] = corner_1
    return oTable
    
        
def faceNum(c):
    return c/3

def nextCorner(c):
    return faceNum(c)*3 + (c+1)%3

def prevCorner(c):
    return nextCorner(nextCorner(c))

def adjCorner(c,oTable):
    p = prevCorner(c)
    op = oTable[p]
    return prevCorner(op)