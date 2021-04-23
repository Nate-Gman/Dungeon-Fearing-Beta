#Version 6 Beta
#
#Credits
#Lead Designer - Nathan Gerads
#Lead Programmer - MarkAndrewGerads.Nazgand@Gmail.Com

#Imports
import pygame, sys, math
import random, time

#Initialzing
pygame.init()

#Setting up FPS
FPS = 22
FramePerSec = pygame.time.Clock()

#colors
BLUE = (0, 255, 0)
FLOOR = (117, 85, 85)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 120, 120)
#light shade of the button 
LIGHT = (170,170,170)
DARK = (100,100,100) 

#Variables
SCORE = 10

#Fonts
font = pygame.font.SysFont("Fixedsys", 60)
font_small = pygame.font.SysFont("Fixedsys", 25)
regularfont = pygame.font.SysFont('Corbel',25) 
text = font.render('LOAD' , True , LIGHT)


#screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1820, 999
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Dungeon Fearing!")

#Sprites Groups
Realm = 0
numberOfRealms = 5

all_sprites = []
Walls = []
Fountains = []
enemies = []
allies = []

for k in range(numberOfRealms):
      all_sprites.append(pygame.sprite.Group())
      Walls.append(pygame.sprite.Group())
      Fountains.append(pygame.sprite.Group())
      enemies.append(pygame.sprite.Group())
      allies.append(pygame.sprite.Group())

class Animation(object):
      def __init__(self, imagePath, numberOfFrames, frameX, frameY, timeSpeed):
            loadedImage = pygame.image.load(imagePath)
            self.numberOfFrames = numberOfFrames
            self.timeSpeed = timeSpeed
            self.frames=[]
            for k in range(numberOfFrames):
                  self.frames.append(loadedImage.subsurface((k * frameX, 0, frameX, frameY)))

animations = {
      #Player
      "Player1": Animation("../Graphics/Images/MainCharRIdolTile75x66.png",6,75,66,0.4),
      "Life": Animation("../Graphics/Images/HealthBarTile 20x16.png",10,20,16,0.08),
      "ManaP": Animation("../Graphics/Images/ManaBarTile20x16.png",10,20,16,0.08),
      #NPC
      "GoblinR": Animation("../Graphics/Images/GoblinR.png",5,32,32,0.4),
      "DemonL": Animation("../Graphics/Images/DemonLTile43x32.png",6,43,32,0.4),
      #Misc
      "HPOT": Animation("../Graphics/Images/LessHealPotTile14x23.png",9,14,23,0.4),
      "MPOT": Animation("../Graphics/Images/LessManaPotTile 14x23.png",9,14,23,0.4),
      #Interactive
      "Fountain": Animation("../Graphics/Images/Fountain.png",5,143,112,0.3),
      "Chest": Animation("../Graphics/Images/ChestClosed 20x20.png",1,20,20,0),
      "Spike": Animation("../Graphics/Tile_set/Floor_Spike.png",8,32,32,0.08),
      #WALLS
      "Wall": Animation("../Graphics/Tile_set/Wall.png",1,80,40,1),
      "WallCL": Animation("../Graphics/Tile_set/WallCL.png",1,80,40,1),
      "WallCR": Animation("../Graphics/Tile_set/WallCR.png",1,80,40,1),
      "WallCLR": Animation("../Graphics/Tile_set/WallCLR.png",1,80,40,1),
      "WallLR": Animation("../Graphics/Tile_set/WallLR.png",1,80,40,1),
      "WallL": Animation("../Graphics/Tile_set/WallL.png",1,80,40,1),
      "WallR": Animation("../Graphics/Tile_set/WallR.png",1,80,40,1),
      "BWallLR": Animation("../Graphics/Tile_set/BWallLR.png",1,80,40,1),
      "BWallR": Animation("../Graphics/Tile_set/BWallR.png",1,80,40,1),
      "BWallL": Animation("../Graphics/Tile_set/BWallL.png",1,80,40,1),
      "BWallFill": Animation("../Graphics/Tile_set/BWallFill.png",1,80,40,1),
      "BWallTop": Animation("../Graphics/Tile_set/BWallTop.png",1,80,40,1),
      "BWallCRT": Animation("../Graphics/Tile_set/BWallCRT.png",1,80,40,1),
      "BWallCLT": Animation("../Graphics/Tile_set/BWallCLT.png",1,80,40,1),
      "BWallCRB": Animation("../Graphics/Tile_set/BWallCRB.png",1,80,40,1),
      "BWallCLB": Animation("../Graphics/Tile_set/BWallCLB.png",1,80,40,1),
      "BWallCLRB": Animation("../Graphics/Tile_set/BWallCLRB.png",1,80,40,1),
      "BWallCLTR": Animation("../Graphics/Tile_set/BWallCLTR.png",1,80,40,1),
      #
      }


class AnimatedSprite(pygame.sprite.Sprite):
      def changeAnimation(self, animationName):
            self.animationName = animationName
            self.image = animations[animationName].frames[0]
            self.surf = pygame.Surface((self.image.get_width(), self.image.get_height()))

      def __init__(self, animationName, spawnX, spawnY):
            super().__init__()
            self.animationName = animationName
            self.spawnX = spawnX
            self.spawnY = spawnY
            self.animationTick = 0
            self.changeAnimation(animationName)
            self.rect = self.surf.get_rect(center=(spawnX, spawnY))

      def updateImage(self):
            self.animationTick += 1
            currentFrame = math.floor(self.animationTick * animations[self.animationName].timeSpeed) % animations[self.animationName].numberOfFrames
            self.image = animations[self.animationName].frames[currentFrame]

      def move(self):
            self.updateImage()

class MagicalCreature(AnimatedSprite):
      def __init__(self, animationName, spawnX, spawnY):
            super().__init__(animationName,spawnX,spawnY)
            self.mana = 100
            self.maxMana = 100
            self.health = 100
            self.maxHealth = 100
            self.meleeDamage = 1

      def refillMana(self, amount):
            self.mana = min(self.maxMana, self.mana + amount)

      def consumeMana(self, amount):
            self.refillMana(-amount)

      def heal(self, amount):
            self.health = min(self.maxHealth, self.health + amount)

      def damage(self, amount):
            self.heal(-amount)

      def meleeFight(self, opponent):
            opponent.damage(self.meleeDamage)
            self.damage(opponent.meleeDamage)

class Goblin(MagicalCreature):
      def __init__(self, spawnX, spawnY):
            super().__init__("GoblinR",spawnX,spawnY)

class FloorSpike(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Spike",spawnX,spawnY)

class Demon(MagicalCreature):
      def __init__(self, spawnX, spawnY):
            super().__init__("DemonL",spawnX,spawnY)

class Wall(AnimatedSprite):
      def __init__(self, animationName, spawnX, spawnY):
            super().__init__(animationName,spawnX,spawnY)

class Fountain(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Fountain",spawnX,spawnY)
            self.healBuff = 10

class HPotion(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("HPOT",spawnX,spawnY)

class MPotion(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("MPOT",spawnX,spawnY)

class Chest(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Chest",spawnX,spawnY)

class HitPoints(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Life",spawnX,spawnY)

class ManaPoints(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("ManaP",spawnX,spawnY)

class Player(MagicalCreature):
      def __init__(self,spawnX,spawnY):
            super().__init__("Player1",spawnX,spawnY)
            self.meleeDamage = 2

      def move(self):
            self.updateImage()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.key.key_code("W")]:
                  self.rect.move_ip(0, -10)
            if pressed_keys[pygame.key.key_code("S")]:
                  self.rect.move_ip(0, 10)
            if pressed_keys[pygame.key.key_code("A")]:
                  self.rect.move_ip(-10, 0)
            if pressed_keys[pygame.key.key_code("D")]:
                  self.rect.move_ip(10, 0)
            edgeTouch=(self.rect.left<0) or (self.rect.top<0) or (self.rect.right>SCREEN_WIDTH) or (self.rect.bottom>SCREEN_HEIGHT)
            if edgeTouch or pressed_keys[pygame.key.key_code(" ")]:
                  teleportX = SCREEN_WIDTH//2-self.rect.left
                  teleportY = SCREEN_HEIGHT//2-self.rect.top
                  for sprite in all_sprites[Realm]:
                        sprite.rect.left += teleportX
                        sprite.rect.top += teleportY

#Sprites
E1 = Goblin(160,520)
all_sprites[0].add(E1)
enemies[0].add(E1)

E2 = Demon(200,720)
all_sprites[0].add(E2)
enemies[0].add(E2)

WF = Fountain(800, 800)
all_sprites[0].add(WF)
Fountains[0].add(WF)

H1 = HPotion(500, 500)
all_sprites[0].add(H1)

M1 = MPotion(500, 700)
all_sprites[0].add(M1)

C1 = Chest(200, 300)
all_sprites[0].add(C1)

HP = HitPoints(900,800)
all_sprites[0].add(HP)

MP = ManaPoints(920,820)
all_sprites[0].add(MP)

FS = FloorSpike(700,600)
all_sprites[0].add(FS)

#Walls
for k in range(10):
      WL = Wall("Wall",k*80,0)
      all_sprites[0].add(WL)
      Walls[0].add(WL)

WL = Wall("WallCL",-100,-100)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallCR",-100,-100)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallCLR",-80,320)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallLR",-80,280)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallL",-160,80)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallR",-80,80)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallLR",-80,40)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallR",720,-40)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallL",0,-40)
all_sprites[0].add(WL)
Walls[0].add(WL)

for k in range(8):
      WL = Wall("BWallFill",k*80+80,-40)
      all_sprites[0].add(WL)
      Walls[0].add(WL)

WL = Wall("BWallCLTR",-80,240)
all_sprites[0].add(WL)
Walls[0].add(WL)

for k in range(8):
      WL = Wall("BWallTop",k*80+80,-80)
      all_sprites[0].add(WL)
      Walls[0].add(WL)

WL = Wall("BWallCRT",720,-80)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCLT",0,-80)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCRB",0,-160)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCLB",-80,-160)
all_sprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCLRB",160,-160)
all_sprites[0].add(WL)
Walls[0].add(WL)
##

#Player
MainCharacter = Player(99,99)
all_sprites[0].add(MainCharacter)
allies[0].add(MainCharacter)

#Game Loop
while True:
      DISPLAYSURF.fill(FLOOR)
      for sprite in all_sprites[Realm]:
            DISPLAYSURF.blit(sprite.image, sprite.rect)
            sprite.move()
            #Walls push sprites around, thus walls will push walls around
            for wall in Walls[Realm]:
                  if pygame.sprite.collide_rect(wall, sprite):
                        WX,WY = wall.rect.center
                        sX,sY = sprite.rect.center
                        MoveX=sX-WX
                        MoveY=sY-WY
                        sprite.rect.move_ip(MoveX, MoveY)

      #Fountain
      for ally in allies[Realm]:
            for Fountain in Fountains[Realm]:
                  if pygame.sprite.collide_rect(ally, Fountain):
                        ally.heal(Fountain.healBuff)
      #Fighting
      for ally in allies[Realm]:
            for enemy in enemies[Realm]:
                  if pygame.sprite.collide_rect(ally, enemy):
                        ally.meleeFight(enemy)
      #Check deaths
      for ally in allies[Realm].copy():
            if ally.health <= 0:
                  ally.kill()
      for enemy in enemies[Realm].copy():
            if enemy.health <= 0:
                  enemy.kill()
      #Cycles through all events occuring
      for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                  mx, my = pygame.mouse.get_pos()
                  MainCharacter.rect.left=mx
                  MainCharacter.rect.top=my
      pressed_keys = pygame.key.get_pressed()
      if pressed_keys[pygame.key.key_code("Q")]:
            pygame.quit()
            sys.exit()
      scores = font.render(str(SCORE), True, BLACK)
      DISPLAYSURF.blit(scores, (20, 20))

      #Moves and Re-draws all Sprites
      pygame.display.update()
      FramePerSec.tick(FPS)
