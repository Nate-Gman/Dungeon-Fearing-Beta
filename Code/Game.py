#Version 6 Beta
#
#Credits
#Lead Designer - Nathan Gerads
#Lead Programmer - MarkAndrewGerads.Nazgand@Gmail.Com

#Imports
import pygame, sys, math, random, time
import Animations, Sprites as sp, Realms as r

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
mouseModes = ["TeleportSelectedSprites", "CenterAtMouse", "SelectSprites"]
leftClickMode = "TeleportSelectedSprites"
middleClickMode = "CenterAtMouse"
rightClickMode = "SelectSprites"
selectRect = pygame.Rect(0,0,0,0)
showSelectRect = False

#Sprites Groups
hudSprites = pygame.sprite.Group()
selectedSprites = pygame.sprite.Group()
clickable = pygame.sprite.Group()

#Sprites
cr = r.Realm()

E1 = sp.Goblin(160,520)
cr.gameSprites.add(E1)
cr.enemies.add(E1)

E2 = sp.Demon(200,720)
cr.gameSprites.add(E2)
cr.enemies.add(E2)

WF = sp.Fountain(800, 800)
cr.gameSprites.add(WF)
cr.Fountains.add(WF)

H1 = sp.HPotion(500, 500)
cr.gameSprites.add(H1)

M1 = sp.MPotion(500, 700)
cr.gameSprites.add(M1)

C1 = sp.Chest(200, 300)
cr.gameSprites.add(C1)

FS = sp.FloorSpike(700,600)
cr.gameSprites.add(FS)

FSS = sp.FloorSpikeSafer(1000,1000)
cr.gameSprites.add(FSS)

#Walls
for k in range(10):
      WL = sp.Wall("Wall",k*80,0)
      cr.gameSprites.add(WL)
      cr.Walls.add(WL)

WL = sp.Wall("WallCL",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WallCR",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WallCLR",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WallLR",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("BWallLR",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("BWallR",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("BWallL",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

for k in range(8):
      WL = sp.Wall("BWallFill",k*80+80,-40)
      cr.gameSprites.add(WL)
      cr.Walls.add(WL)

WL = sp.Wall("BWallCLTR",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

for k in range(8):
      WL = sp.Wall("BWallTop",k*80+80,-80)
      cr.gameSprites.add(WL)
      cr.Walls.add(WL)

WL = sp.Wall("BWallCRT",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("BWallCLT",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("BWallCRB",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("BWallCLB",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("BWallCLRB",0,0)
cr.gameSprites.add(WL)
cr.Walls.add(WL)
##Finished_Walls
WL = sp.Wall("WA1",-1300,400)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA2",-900,-200)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA3",-900,-400)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA4",-500,-1200)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA5",-500,-900)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA6",-500,700)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA7",-200,-200)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA8",-500,-500)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

WL = sp.Wall("WA9",-1000,-1000)
cr.gameSprites.add(WL)
cr.Walls.add(WL)

#
PI = sp.Inventory(1200, 1200)
cr.gameSprites.add(PI)
PS = sp.Skills(-700, -700)
cr.gameSprites.add(PS)
##
XP = sp.Experience(900,760)
cr.gameSprites.add(XP)

HP = sp.HitPoints(900,800)
cr.gameSprites.add(HP)

MP = sp.ManaPoints(920,820)
cr.gameSprites.add(MP)
#Player
MainCharacter = sp.Player(99,99)
cr.gameSprites.add(MainCharacter)
cr.allies.add(MainCharacter)
selectedSprites.add(MainCharacter)

##hudSprites
PD = sp.Displayer(0, 100)
hudSprites.add(PD)

def teleportAllSprites(east, south):
      if east == 0 and south == 0: #Sometimes save computation
            return
      for sprite in cr.gameSprites:
            sprite.rect.left += east
            sprite.rect.top += south

def recenterAt(x, y):
      teleportAllSprites(SCREEN_WIDTH // 2 - x, SCREEN_HEIGHT // 2 - y)

def centerOfSelectedSprites():
      if selectedSprites.__len__() > 0:
            minLeft = min((o.rect.left for o in selectedSprites))
            minTop = min((o.rect.top for o in selectedSprites))
            maxRight = max((o.rect.right for o in selectedSprites))
            maxBottom = max((o.rect.bottom for o in selectedSprites))
            return (maxRight + minLeft) // 2, (maxBottom + minTop) // 2
      else:
            return SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

#Game Loop
while True:
      DISPLAYSURF.fill(FloorColor)
      #Moves and Re-draws all Sprites
      for sprite in cr.gameSprites:
            sprite.draw(DISPLAYSURF)
            sprite.move()
            #Walls push sprites around, thus walls will push walls around
            for wall in cr.Walls:
                  if pygame.sprite.collide_rect(wall, sprite):
                        WX,WY = wall.rect.center
                        sX,sY = sprite.rect.center
                        MoveX=sX-WX
                        MoveY=sY-WY
                        sprite.rect.move_ip(MoveX, MoveY)

      #Fountain
      for ally in cr.allies:
            for Fountain in cr.Fountains:
                  if pygame.sprite.collide_rect(ally, Fountain):
                        ally.heal(Fountain.healBuff)
      #Fighting
      for ally in cr.allies:
            for enemy in cr.enemies:
                  if pygame.sprite.collide_rect(ally, enemy):
                        ally.meleeFight(enemy)
      #Check deaths
      for ally in cr.allies.copy():
            if ally.health <= 0:
                  ally.kill()
      for enemy in cr.enemies.copy():
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
      #Recenter on center of selectedSprites
      if pressed_keys[pygame.key.key_code(" ")]:
            ssX, ssY = centerOfSelectedSprites()
            recenterAt(ssX, ssY)

      #Cycles through all events occuring
      for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                  mx, my = pygame.mouse.get_pos()
                  if event.button == 1: #Left mouse button was pressed
                        if leftClickMode == "TeleportSelectedSprites":
                              ssX, ssY = centerOfSelectedSprites()
                              teleportX = mx - ssX
                              teleportY = my - ssY
                              for sprite in selectedSprites:
                                    sprite.rect.left += teleportX
                                    sprite.rect.top += teleportY
                  if event.button == 2: #Middle mouse button was pressed
                        if middleClickMode=="CenterAtMouse":
                              recenterAt(mx, my)
                  if event.button == 3: #Right mouse button was pressed
                        if rightClickMode=="SelectSprites":
                              showSelectRect=True
                              selectRect.topleft = mx, my
                              selectRect.width, selectRect.height = 1, 1
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
                              for sprite in cr.gameSprites:
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
            sprite.draw(DISPLAYSURF)
      scores = font.render(str(SCORE), True, BLACK)
      DISPLAYSURF.blit(scores, (20, 20))

      #Update display
      pygame.display.update()
      FramePerSec.tick(FPS)
