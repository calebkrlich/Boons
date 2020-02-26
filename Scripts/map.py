
class Map:
    def __init__(self, tilesX, tilesY, tileSize, tileSet):
        self.x = tilesX
        self.y = tilesY
        self.tileSize = tileSize
        self.movePath = []
        self.tileSet = []
        self.mapLayout = [[0 for x in range(tilesX)] for y in range(tilesY)]

    def getMovePath(self):
        return self.movePath

    def getMovePathPosAtIndex(self, index):
        return self.movePath[index]
        
    def getTileSet(self):
        return self.tileSet

    def getMapLayout(self):
        return self.mapLayout

    def getTileAtPosition(self, x, y):
        return self.mapLayout[x][y]
    
    def setTileAtPosition(self, x, y, tile):
        self.mapLayout[x][y] = tile

    