import pygame
import os, sys
from map import Map
from enemy import Enemy
from gameobject import GameObject

os.chdir(os.getcwd() + "\\Scripts")

gameObjects = []
movePath = []
playerX = 0
playerY = 0

def move(self, position):
        self.pos = position

def getMovePath():
    movePath = [(0,1), (1,1), (1,2), (1,3), (1,4), (2,4), (2,5), (2,6), (3,6), (4,6), (4,5), (4,4),
    (4,3), (4,2), (4,1), (5,1), (6,1), (7,1), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6),
    (8,7), (8,8), (8,9), (8,10), (9,10), (10,10), (11,10)]

    return movePath

def setupMap(mapObject):
    for x in getMovePath():
        mapObject.setTileAtPosition(x[0], x[1], tileSet[1])

    #mapObject.setTileAtPosition(0,1, tileSet[1])
    #mapObject.setTileAtPosition(1,1, tileSet[1])
    #mapObject.setTileAtPosition(1,2, tileSet[1])
    #mapObject.setTileAtPosition(1,3, tileSet[1])
    #mapObject.setTileAtPosition(1,4, tileSet[1])
    #mapObject.setTileAtPosition(2,4, tileSet[1])
    #mapObject.setTileAtPosition(2,5, tileSet[1])
    #mapObject.setTileAtPosition(2,6, tileSet[1])
    #mapObject.setTileAtPosition(3,6, tileSet[1])
    #mapObject.setTileAtPosition(4,6, tileSet[1])
    #mapObject.setTileAtPosition(4,5, tileSet[1])
    #mapObject.setTileAtPosition(4,4, tileSet[1])
    
    #mapObject.setTileAtPosition(4,3, tileSet[1])
    #mapObject.setTileAtPosition(4,2, tileSet[1])
    #mapObject.setTileAtPosition(4,1, tileSet[1])
    #mapObject.setTileAtPosition(5,1, tileSet[1])
    #mapObject.setTileAtPosition(6,1, tileSet[1])
    #mapObject.setTileAtPosition(7,1, tileSet[1])
    #mapObject.setTileAtPosition(8,1, tileSet[1])
    #mapObject.setTileAtPosition(8,2, tileSet[1])
    #mapObject.setTileAtPosition(8,3, tileSet[1])
    #mapObject.setTileAtPosition(8,4, tileSet[1])
    #mapObject.setTileAtPosition(8,5, tileSet[1])
    #mapObject.setTileAtPosition(8,6, tileSet[1])
    #mapObject.setTileAtPosition(8,7, tileSet[1])
    #mapObject.setTileAtPosition(8,8, tileSet[1])
    #mapObject.setTileAtPosition(8,9, tileSet[1])
    #mapObject.setTileAtPosition(8,10, tileSet[1])

    #mapObject.setTileAtPosition(9,10, tileSet[1])
    #mapObject.setTileAtPosition(10,10, tileSet[1])
    #mapObject.setTileAtPosition(11,10, tileSet[1])

def loadMap(mapObject):
    for x in range (mapObject.x):
        for y in range(mapObject.y):
            if(mapObject.getTileAtPosition(x,y) == 0):
                tile = pygame.image.load('..\\Art\\Grass.png').convert()
            else:
                tile = mapObject.getTileAtPosition(x,y)
            screen.blit(tile,(x*mapObject.tileSize, y*mapObject.tileSize))

def initGameObjects():
    screen.blit(player, (100, 100))
    gameObjects.append(object)

def redrawGameobjects(objectsToRedraw):
    for object in objectsToRedraw:
        screen.blit(object.image, object.pos)

def drawEnemy(enemyList):
    for enemy in enemyList:
        enemy.move()

#SETUP 
pygame.init()
screen =  pygame.display.set_mode([384,384])
tileSet = [pygame.image.load('..\\Art\\Grass.png').convert(), pygame.image.load('..\\Art\\Dirt.png').convert()]
map = Map(12,12,32, tileSet)
setupMap(map)

player = GameObject(pygame.image.load('..\\Art\\WhiteBoon.png').convert(), (playerX, playerY))
enemy = Enemy(1,getMovePath(), pygame.image.load('..\\Art\\RedBoon.png').convert(), 1)
enemy2 = Enemy(1,getMovePath(), pygame.image.load('..\\Art\\BlueBoon.png').convert(), 10)

gameObjects.append(player)
gameObjects.append(enemy)
gameObjects.append(enemy2)

pygame.display.set_caption("Boons")

#Game Settings
clockRate = pygame.time.Clock()
enemyUpdateTime = 2
currentEnemyUpdateCount = 0
done = False
loadMap(map)

#GAME LOOP
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_RIGHT):
                playerX += 10

            if(event.key == pygame.K_LEFT):
                playerX -= 10

            if(event.key == pygame.K_UP):
                playerY -= 10

            if(event.key == pygame.K_DOWN):
                playerY += 10

    loadMap(map)
    player.move((playerX, playerY))
    redrawGameobjects(gameObjects)

    if(currentEnemyUpdateCount > enemyUpdateTime):
        enemy.move()
        enemy2.move()
        currentEnemyUpdateCount = 0

    currentEnemyUpdateCount += 1
    pygame.display.update()
    pygame.time.delay(100)
    screen.fill((0,0,0))

#END OF GAME LOOP
pygame.quit()
