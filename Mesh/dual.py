import helper
def genNewTables(oldvTable, oldgTable, oldoTable):
    newvTable = []
    newgTable = []
    newoTable = []
    newSurfaceNormals = []
    newVertexNormals = []
    
    # New Geometry Table 
    for corner in range(0,len(oldvTable),3):
        nextCorner = helper.nextCorner(corner)
        prevCorner = helper.prevCorner(corner)
        currVertex = oldgTable[oldvTable[corner]]
        nextVertex = oldgTable[oldvTable[nextCorner]]
        prevVertex = oldgTable[oldvTable[prevCorner]]
        currPos = PVector(currVertex[0],currVertex[1],currVertex[2])
        nextPos = PVector(nextVertex[0],nextVertex[1],nextVertex[2])
        prevPos = PVector(prevVertex[0],prevVertex[1],prevVertex[2])
        centroid = currPos.copy()
        centroid.add(nextPos)
        centroid.add(prevPos)
        centroid.div(3)
        newgTable.append((centroid.x,centroid.y,centroid.z)) #New Geometry Table is almost done
        
    #Only drawing triangles. So if there are polygons, keep dividing them into triangles
    checkList = []
    for corner in range(len(oldvTable)):
        if (oldvTable[corner] not in checkList):
            checkList.append(oldvTable[corner])
            faceNum = corner/3
            currentVertex = newgTable[faceNum]
            tempCentroids = [faceNum] #this list will store all the centroids for the current corner->vertex, for later vTable add
            center = PVector(currentVertex[0],currentVertex[1],currentVertex[2])
            adjC = helper.adjCorner(corner,oldoTable)
            while adjC != corner:
                adjFaceNum = adjC/3
                adjVertex = newgTable[adjFaceNum]
                tempCentroids.append(adjFaceNum)
                adjPos = PVector(adjVertex[0],adjVertex[1],adjVertex[2])
                center.add(adjPos)
                adjC = helper.adjCorner(adjC, oldoTable)
            center.div(len(tempCentroids))
            newgTable.append((center.x, center.y,center.z)) # New Geometry table is done
            
            l = len(tempCentroids)
            for i in range(l): # Add new vTable with centroids in the centroids list
                newvTable.append(tempCentroids[i%l])
                newvTable.append(tempCentroids[(i+1)%l])
                newvTable.append(len(newgTable)-1)
    newoTable = helper.oTableGene(newvTable) #New opposite table is done 
    newSurfaceNormals = helper.surfaceNormalsGene(newvTable,newgTable) 
    newVertexNormals = helper.vertexNormalsGene(newvTable,newgTable,newoTable,newSurfaceNormals)
    return (newvTable,newgTable,newoTable,newSurfaceNormals,newVertexNormals)                       
            
            
            