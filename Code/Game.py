#Version 6 Beta
#
#Credits
#Lead Designer - Nathan Gerads
#Lead Programmer - MarkAndrewGerads.Nazgand@Gmail.Com

#Imports
import pygame, sys, math, random, time
import Animations

#Initialzing
pygame.init()

#Setting up FPS
FPS = 22
FramePerSec = pygame.time.Clock()

#colors
BlueBorderColor = (3*16, 3*16+14, 5*16+9)
FloorColor = (117, 85, 85)
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

#Mouse stuff
mouseModes = ["TeleportSelectedSprites","CenterAtMouse","SelectSprites"]
leftClickMode = "TeleportSelectedSprites"
middleClickMode = "CenterAtMouse"
rightClickMode = "SelectSprites"
selectRect = pygame.Rect(0,0,0,0)
showSelectRect = False

#Sprites Groups
Realm = 0
numberOfRealms = 5

hudSprites = pygame.sprite.Group()
selectedSprites = pygame.sprite.Group()
clickable = pygame.sprite.Group()

gameSprites = []
Walls = []
Fountains = []
enemies = []
allies = []

for k in range(numberOfRealms):
      gameSprites.append(pygame.sprite.Group())
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
      #hudSprites
      "Port1": Animation("../Graphics/Images/PlayerDisplay352x137.png",1,352,137,0.4),
      #
      "PInvt": Animation("../Graphics/Images/InventorySheet384x384.png",1,384,384,0.4),
      "PSkill": Animation("../Graphics/Images/SkillsLevelsTile142x270.png",1,142,270,0.4),
      #Player
      "Player1": Animation("../Graphics/Images/MainCharRIdolTile75x66.png",6,75,66,0.4),
      "ExpP": Animation("../Graphics/Images/XPBarTile20x10.png",10,20,10,1),
      "Life": Animation("../Graphics/Images/HealthBarTile 20x18.png",10,20,18,0.3),
      "ManaP": Animation("../Graphics/Images/ManaBarTile20x18.png",10,20,18,0.3),
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
      "SSafer": Animation("../Graphics/Tile_set/Floor_Spike_Safer.png",12,32,32,0.08),
      #WALLTILES
      "Wall": Animation("../Graphics/Tile_set/Wall.png",1,80,40,1),
      "WallCL": Animation("../Graphics/Tile_set/WallCL.png",1,80,40,1),
      "WallCR": Animation("../Graphics/Tile_set/WallCR.png",1,80,40,1),
      "WallCLR": Animation("../Graphics/Tile_set/WallCLR.png",1,80,40,1),
      "WallLR": Animation("../Graphics/Tile_set/WallLR.png",1,80,40,1),
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
      #Finished Walls
      "WA1": Animation("../Graphics/Finished_walls/EmptyWallPillar80x80.png",1,80,80,1),
      "WA2": Animation("../Graphics/Finished_walls/WallPillar80x80.png",1,80,80,1),
      "WA3": Animation("../Graphics/Finished_walls/StrongWallPillar80x120.png",1,80,120,1),
      "WA4": Animation("../Graphics/Finished_walls/SmallRectWall320x80.png",1,320,80,1),
      "WA5": Animation("../Graphics/Finished_walls/MediumRectWall320x120.png",1,320,120,1),
      "WA6": Animation("../Graphics/Finished_walls/LargeRectWall320x160.png",1,320,160,1),
      "WA7": Animation("../Graphics/Finished_walls/LargeSquareWall320x279.png",1,320,279,1),
      "WA8": Animation("../Graphics/Finished_walls/Virtical160x279.png",1,160,279,1),
      "WA9": Animation("../Graphics/Finished_walls/LongVerticalWall160x879.png",1,160,879,1),
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
            self.movementSpeed = 1 #default movement 1 pixel per movement
            self.animationTick = 0
            self.changeAnimation(animationName)
            self.rect = self.surf.get_rect(topleft=(spawnX, spawnY))

      def setMovementSpeed(self,speed):
            self.movementSpeed = speed

      def moveRight(self):
            self.rect.x += self.movementSpeed

      def moveLeft(self):
            self.rect.x -= self.movementSpeed

      def moveDown(self):
            self.rect.y += self.movementSpeed

      def moveUp(self):
            self.rect.y -= self.movementSpeed

      def recenterAt(self,X,Y):
            self.rect = self.surf.get_rect(center=(spawnX, spawnY))

      def updateImage(self):
            self.animationTick += 1
            currentFrame = math.floor(self.animationTick * animations[self.animationName].timeSpeed) % animations[self.animationName].numberOfFrames
            self.image = animations[self.animationName].frames[currentFrame]

      def draw(self):
            global DISPLAYSURF
            DISPLAYSURF.blit(self.image, self.rect)

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
##hudSprites
class Displayer(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Port1",spawnX,spawnY)

class Inventory(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("PInvt",spawnX,spawnY)

class Skills(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("PSkill",spawnX,spawnY)
##MapBuild
class Wall(AnimatedSprite):
      def __init__(self, animationName, spawnX, spawnY):
            super().__init__(animationName,spawnX,spawnY)
##Foes
class Goblin(MagicalCreature):
      def __init__(self, spawnX, spawnY):
            super().__init__("GoblinR",spawnX,spawnY)

class Demon(MagicalCreature):
      def __init__(self, spawnX, spawnY):
            super().__init__("DemonL",spawnX,spawnY)
## Interactive
class FloorSpike(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Spike",spawnX,spawnY)

class FloorSpikeSafer(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("SSafer",spawnX,spawnY)

class Fountain(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Fountain",spawnX,spawnY)
            self.healBuff = 10

class Chest(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Chest",spawnX,spawnY)
##Misc
class HPotion(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("HPOT",spawnX,spawnY)

class MPotion(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("MPOT",spawnX,spawnY)

class Experience(AnimatedSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("ExpP",spawnX,spawnY)

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

#Sprites
E1 = Goblin(160,520)
gameSprites[0].add(E1)
enemies[0].add(E1)

E2 = Demon(200,720)
gameSprites[0].add(E2)
enemies[0].add(E2)

WF = Fountain(800, 800)
gameSprites[0].add(WF)
Fountains[0].add(WF)

H1 = HPotion(500, 500)
gameSprites[0].add(H1)

M1 = MPotion(500, 700)
gameSprites[0].add(M1)

C1 = Chest(200, 300)
gameSprites[0].add(C1)

FS = FloorSpike(700,600)
gameSprites[0].add(FS)

FSS = FloorSpikeSafer(1000,1000)
gameSprites[0].add(FSS)

#Walls
for k in range(10):
      WL = Wall("Wall",k*80,0)
      gameSprites[0].add(WL)
      Walls[0].add(WL)

WL = Wall("WallCL",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallCR",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallCLR",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WallLR",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallLR",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallR",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallL",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

for k in range(8):
      WL = Wall("BWallFill",k*80+80,-40)
      gameSprites[0].add(WL)
      Walls[0].add(WL)

WL = Wall("BWallCLTR",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

for k in range(8):
      WL = Wall("BWallTop",k*80+80,-80)
      gameSprites[0].add(WL)
      Walls[0].add(WL)

WL = Wall("BWallCRT",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCLT",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCRB",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCLB",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("BWallCLRB",0,0)
gameSprites[0].add(WL)
Walls[0].add(WL)
##Finished_Walls
WL = Wall("WA1",-1300,400)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA2",-900,-200)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA3",-900,-400)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA4",-500,-1200)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA5",-500,-900)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA6",-500,700)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA7",-200,-200)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA8",-500,-500)
gameSprites[0].add(WL)
Walls[0].add(WL)

WL = Wall("WA9",-1000,-1000)
gameSprites[0].add(WL)
Walls[0].add(WL)

##hudSprites
PD = Displayer(0, 100)
hudSprites.add(PD)
#
PI = Inventory(1200, 1200)
gameSprites[0].add(PI)
PS = Skills(-700, -700)
gameSprites[0].add(PS)
##
XP = Experience(900,760)
gameSprites[0].add(XP)

HP = HitPoints(900,800)
gameSprites[0].add(HP)

MP = ManaPoints(920,820)
gameSprites[0].add(MP)
#Player
MainCharacter = Player(99,99)
MainCharacter.setMovementSpeed(15)
gameSprites[0].add(MainCharacter)
allies[0].add(MainCharacter)
selectedSprites.add(MainCharacter)

#Game Loop
while True:
      DISPLAYSURF.fill(FloorColor)
      #Moves and Re-draws all Sprites
      for sprite in gameSprites[Realm]:
            sprite.draw()
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
 
      #Action Keys
      pressed_keys = pygame.key.get_pressed()
      #Quit game
      if pressed_keys[pygame.key.key_code("Q")]:
            pygame.quit()
            sys.exit()
      #WASD movement of selected sprites
      if pressed_keys[pygame.key.key_code("W")]:
            for selected in selectedSprites:
                  selected.moveUp()
      if pressed_keys[pygame.key.key_code("A")]:
            for selected in selectedSprites:
                  selected.moveLeft()
      if pressed_keys[pygame.key.key_code("S")]:
            for selected in selectedSprites:
                  selected.moveDown()
      if pressed_keys[pygame.key.key_code("D")]:
            for selected in selectedSprites:
                  selected.moveRight()
      #Recenter on MainCharacter
      if pressed_keys[pygame.key.key_code(" ")]:
            teleportX = SCREEN_WIDTH//2-MainCharacter.rect.centerx
            teleportY = SCREEN_HEIGHT//2-MainCharacter.rect.centery
            for sprite in gameSprites[Realm]:
                  sprite.rect.left += teleportX
                  sprite.rect.top += teleportY

      #Cycles through all events occuring
      for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                  mx, my = pygame.mouse.get_pos()
                  if event.button == 1: #Left mouse button was pressed
                        if leftClickMode == "TeleportSelectedSprites" and selectedSprites.__len__() > 0:
                              minLeft = min((o.rect.left for o in selectedSprites))
                              minTop = min((o.rect.top for o in selectedSprites))
                              teleportX = mx - minLeft
                              teleportY = my - minTop
                              for sprite in selectedSprites:
                                    sprite.rect.left += teleportX
                                    sprite.rect.top += teleportY
                  if event.button == 2: #Middle mouse button was pressed
                        if middleClickMode=="CenterAtMouse":
                              teleportX = SCREEN_WIDTH//2-mx
                              teleportY = SCREEN_HEIGHT//2-my
                              for sprite in gameSprites[Realm]:
                                    sprite.rect.left += teleportX
                                    sprite.rect.top += teleportY
                  if event.button == 3: #Right mouse button was pressed
                        if rightClickMode=="SelectSprites":
                              showSelectRect=True
                              selectRect.topleft = mx, my
                              selectRect.width, selectRect.height = 0, 0
            if event.type == pygame.MOUSEMOTION:
                  if showSelectRect: #Update selectRect
                        mx, my = pygame.mouse.get_pos()
                        selectRect.width = mx - selectRect.left
                        selectRect.height = my - selectRect.top
            if event.type == pygame.MOUSEBUTTONUP:
                  mx, my = pygame.mouse.get_pos()
                  if event.button == 3: #Right mouse button was released
                        if rightClickMode == "SelectSprites":
                              showSelectRect = False
                              newSelectedSprites = pygame.sprite.Group()
                              for sprite in gameSprites[Realm]:
                                    if selectRect.colliderect(sprite.rect):
                                          newSelectedSprites.add(sprite)
                              if not pressed_keys[pygame.K_LCTRL]:
                                    selectedSprites = newSelectedSprites
                              else:
                                    for sprite in newSelectedSprites:
                                          if selectedSprites.has(sprite):
                                                selectedSprites.remove(sprite)
                                          else:
                                                selectedSprites.add(sprite)

      #Draw border rectangles
      if showSelectRect:
            pygame.draw.rect(DISPLAYSURF,GREEN,selectRect,1)
      for selected in selectedSprites:
            pygame.draw.rect(DISPLAYSURF,BlueBorderColor,selected.rect,1)
      #Heads Up Display
      for sprite in hudSprites:
            sprite.draw()
      scores = font.render(str(SCORE), True, BLACK)
      DISPLAYSURF.blit(scores, (20, 20))

      #Update display
      pygame.display.update()
      FramePerSec.tick(FPS)
