from enum import Enum
from gameobject import GameObject
from operator import mul

class BoonType(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

class Enemy (GameObject):
    def __init__(self, enemyType, pathToFollow, image, gameLoopCountSpawn):
        self.type = enemyType
        self.movePath = pathToFollow
        self.currentMovePathIndex = 0
        self.image = image
        self.health = 1
        self.pos = (0,0)
        self.gameLoopCountSpawn = gameLoopCountSpawn
        self.currentGameLoop = 0

    def move(self):
        if(self.currentGameLoop >= self.gameLoopCountSpawn):
            self.currentMovePathIndex += 1
            if(len(self.movePath) > self.currentMovePathIndex): 
                #move position to next path position times tile size
                self.pos = tuple(map(mul, self.movePath[self.currentMovePathIndex], (32,32)))
        else:
            self.currentGameLoop += 1


    def getHealth(self):
        return self.health
    
    def damage(self, amount):
        self.health -= amount

