# Version 7 Beta
# 
# Credits
# Lead Designer - Nathan Gerads
# Lead Programmer - MarkAndrewGerads.Nazgand@Gmail.Com

# Imports
import sys, math, random, time
import pygame, pygame_gui
import Animations, Sprites as sp, Realms as r, Settings
import ExportedRealm0

# Initialzing
pygame.init()

# Setting up FPS
FPS = 9
clock = pygame.time.Clock()

# colors
BlueBorderColor = (3*16, 3*16+14, 5*16+9)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Variables
cr = ExportedRealm0.r
calculateWalls = True

# Fonts
font = pygame.font.SysFont("Fixedsys", 39)

# screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1820, 999
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Fearing!")

# Mouse stuff
EditMouseModes = ["TeleportSelectedSprites", "CenterAtMouse", "SelectSprites"]
EditLeftClickMode = "TeleportSelectedSprites"
EditMiddleClickMode = "CenterAtMouse"
EditRightClickMode = "SelectSprites"
PlayMouseModes = ["TeleportSelectedAllies", "CenterAtMouse", "SelectAllies"]
PlayLeftClickMode = "TeleportSelectedAllies"
PlayMiddleClickMode = "CenterAtMouse"
PlayRightClickMode = "SelectAllies"
selectRect = pygame.Rect(0,0,0,0)
showSelectRect = False

# Sprites Groups
hudSprites = pygame.sprite.Group()
selectedSprites = pygame.sprite.Group()
selectedAllies = pygame.sprite.Group()
clickable = pygame.sprite.Group()

# # hudSprites
PD = sp.AnimatedSprite("Port1", 1468, 862)
hudSprites.add(PD)

def recenterAt(x, y):
      cr.teleportAllSprites(SCREEN_WIDTH // 2 - x, SCREEN_HEIGHT // 2 - y)

def OutputRealmToPNG():
      rs = cr.PrintRealmToSurface()
      pygame.image.save(rs, 'Realm' + cr.name + '.png')

# Game Loop
isRunning = True
gameModes = ['Edit','Play','Settings']
gameMode = 'Edit'
gameModeDrop = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(gameModes, gameMode, pygame.rect.Rect(0,0,100,39), manager)
while isRunning:
      gameMode = gameModeDrop.selected_option
      time_delta = clock.tick(FPS) / 1000.0
      DISPLAYSURF.fill(Settings.FloorColor)
      # User interface events
      events = pygame.event.get()
      for event in events:
            manager.process_events(event)
            if event.type == pygame.QUIT:
                  isRunning = False
      # Action Keys
      pressed_keys = pygame.key.get_pressed()
      mx, my = pygame.mouse.get_pos()
      if gameMode == 'Edit' or gameMode == 'Play':
            # Re-draws all gameSprites
            for sprite in cr.gameSprites:
                  sprite.draw(DISPLAYSURF)
            # Draw select rectangle
            if showSelectRect:
                  pygame.draw.rect(DISPLAYSURF,GREEN,selectRect,1)
            if pressed_keys[pygame.K_p]:
                  OutputRealmToPNG()
      if gameMode == 'Play':
            # Draw border rectangles
            for selected in selectedAllies:
                  pygame.draw.rect(DISPLAYSURF,BlueBorderColor,selected.rect,1)
            # WASD movement of selected sprites
            if pressed_keys[pygame.K_w]:
                  for selected in selectedAllies:
                        selected.moveUp()
            if pressed_keys[pygame.K_a]:
                  for selected in selectedAllies:
                        selected.moveLeft()
            if pressed_keys[pygame.K_s]:
                  for selected in selectedAllies:
                        selected.moveDown()
            if pressed_keys[pygame.K_d]:
                  for selected in selectedAllies:
                        selected.moveRight()
            # Recenter on center of selectedSprites
            if pressed_keys[pygame.K_SPACE]:
                  ssX, ssY = sp.SpriteGroupRect(selectedSprites).center
                  recenterAt(ssX, ssY)
            # Moves all Sprites
            for sprite in cr.gameSprites:
                  sprite.updateImage()
                  sprite.move()
                  # Walls push sprites around, thus walls will push walls around
                  for wall in cr.Walls:
                        if pygame.sprite.collide_rect(wall, sprite):
                              WX,WY = wall.rect.center
                              sX,sY = sprite.rect.center
                              WallForceRatio = 0.15 # Slow down wall force
                              MoveX = math.ceil((sX - WX) * WallForceRatio)
                              MoveY = math.ceil((sY - WY) * WallForceRatio)
                              sprite.rect.move_ip(MoveX, MoveY)
            # Fountain
            for ally in cr.allies:
                  for Fountain in cr.allyFountains:
                        if pygame.sprite.collide_rect(ally, Fountain):
                              ally.heal(Fountain.healBuff)
            for enemy in cr.enemies:
                  for Fountain in cr.enemyFountains:
                        if pygame.sprite.collide_rect(enemy, Fountain):
                              enemy.heal(Fountain.healBuff)
            # Fighting
            for ally in cr.allies:
                  for enemy in cr.enemies:
                        if pygame.sprite.collide_rect(ally, enemy):
                              ally.meleeFight(enemy)
            # Check deaths
            for ally in cr.allies.copy():
                  if ally.health <= 0:
                        ally.kill()
            for enemy in cr.enemies.copy():
                  if enemy.health <= 0:
                        enemy.kill()
            # Cycles through all events occuring for mouse events
            for event in events:
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # Left mouse button was pressed
                              if PlayLeftClickMode == "TeleportSelectedAllies":
                                    saX, saY = sp.SpriteGroupRect(selectedAllies).center
                                    teleportX = mx - saX
                                    teleportY = my - saY
                                    for sprite in selectedAllies:
                                          sprite.rect.left += teleportX
                                          sprite.rect.top += teleportY
                        if event.button == 2: # Middle mouse button was pressed
                              if PlayMiddleClickMode == "CenterAtMouse":
                                    recenterAt(mx, my)
                        if event.button == 3: # Right mouse button was pressed
                              if PlayRightClickMode == "SelectAllies":
                                    showSelectRect = True
                                    selectRect.topleft = mx, my
                                    selectRect.width, selectRect.height = 1, 1
                  if event.type == pygame.MOUSEMOTION:
                        if showSelectRect: # Update selectRect
                              selectRect.width = mx - selectRect.left
                              selectRect.height = my - selectRect.top
                  if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 3: # Right mouse button was released
                              if PlayRightClickMode == "SelectAllies":
                                    showSelectRect = False
                                    newSelectedAllies = pygame.sprite.Group()
                                    for ally in cr.allies:
                                          if selectRect.colliderect(ally.rect):
                                                newSelectedAllies.add(ally)
                                    if not pressed_keys[pygame.K_LCTRL]:
                                          selectedAllies = newSelectedAllies
                                    else:
                                          for ally in newSelectedAllies:
                                                if selectedAllies.has(ally):
                                                      selectedAllies.remove(ally)
                                                else:
                                                      selectedAllies.add(ally)
            # Heads Up Display
            for sprite in hudSprites:
                  sprite.draw(DISPLAYSURF)

      if gameMode == 'Edit':
            # Export current realm
            if pressed_keys[pygame.K_e]:
                  cr.export()
            # WASD movement of selected sprites
            if pressed_keys[pygame.K_w]:
                  for selected in selectedSprites:
                        selected.moveUp()
            if pressed_keys[pygame.K_a]:
                  for selected in selectedSprites:
                        selected.moveLeft()
            if pressed_keys[pygame.K_s]:
                  for selected in selectedSprites:
                        selected.moveDown()
            if pressed_keys[pygame.K_d]:
                  for selected in selectedSprites:
                        selected.moveRight()
            # Copy selectedSprites
            if pressed_keys[pygame.K_c]:
                  for selected in selectedSprites:
                        copiedSprite = selected.copy()
                        for group in selected.groups():
                              if group != selectedSprites:
                                    group.add(copiedSprite)
                  pygame.time.wait(500) # Wait a bit so multiple copies are not made
            # Delete selected sprites
            if pressed_keys[pygame.K_DELETE]:
                  for selected in selectedSprites:
                        selected.kill()
            # Recenter on center of selectedSprites
            if pressed_keys[pygame.K_SPACE]:
                  ssX, ssY = sp.SpriteGroupRect(selectedSprites).center
                  recenterAt(ssX, ssY)
            # Draw border rectangles
            for selected in selectedSprites:
                  pygame.draw.rect(DISPLAYSURF,BlueBorderColor,selected.rect,1)
            # Cycles through all events occuring for mouse events
            for event in events:
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # Left mouse button was pressed
                              if EditLeftClickMode == "TeleportSelectedSprites":
                                    ssX, ssY = sp.SpriteGroupRect(selectedSprites).center
                                    teleportX = mx - ssX
                                    teleportY = my - ssY
                                    for sprite in selectedSprites:
                                          sprite.rect.left += teleportX
                                          sprite.rect.top += teleportY
                        if event.button == 2: # Middle mouse button was pressed
                              if EditMiddleClickMode == "CenterAtMouse":
                                    recenterAt(mx, my)
                        if event.button == 3: # Right mouse button was pressed
                              if EditRightClickMode == "SelectSprites":
                                    showSelectRect = True
                                    selectRect.topleft = mx, my
                                    selectRect.width, selectRect.height = 1, 1
                  if event.type == pygame.MOUSEMOTION:
                        if showSelectRect: # Update selectRect
                              selectRect.width = mx - selectRect.left
                              selectRect.height = my - selectRect.top
                  if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 3: # Right mouse button was released
                              if EditRightClickMode == "SelectSprites":
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

      # Update display
      manager.update(time_delta)
      manager.draw_ui(DISPLAYSURF)
      pygame.display.update()
