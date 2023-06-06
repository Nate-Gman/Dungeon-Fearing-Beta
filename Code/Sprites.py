import pygame, math, Animations, random

DefaultMovementSpeed = 1
DefaultMoveMode = 'Stay'
DefaultMaxMana = 100
DefaultMaxHealth = 100
DefaultMeleeDamage = 1.5
DefaultHealBuff = 1
DefaultManaBuff = 1

class AnimatedMagicalCreatureSprite(pygame.sprite.Sprite):
      def changeAnimation(self, animationName):
            self.animationName = animationName
            self.image = Animations.animations[animationName].frames[0]
            self.surf = pygame.Surface((self.image.get_width(), self.image.get_height()))

      def __init__(self, animationName, spawnX, spawnY):
            super().__init__()
            self.animationName = animationName
            self.spawnX = spawnX
            self.spawnY = spawnY
            self.movementSpeed = DefaultMovementSpeed
            self.targetSprite = None
            self.moveMode = DefaultMoveMode
            self.animationTick = 0
            self.changeAnimation(animationName)
            self.rect = self.surf.get_rect(topleft=(spawnX, spawnY))
            self.mana = DefaultMaxMana
            self.maxMana = DefaultMaxMana
            self.health = DefaultMaxHealth
            self.maxHealth = DefaultMaxHealth
            self.meleeDamage = DefaultMeleeDamage
            self.healBuff = DefaultHealBuff
            self.manaBuff = DefaultManaBuff

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
            self.rect = self.surf.get_rect(center=(X, Y))

      def updateImage(self):
            self.animationTick += 1
            currentFrame = math.floor(self.animationTick * Animations.animations[self.animationName].timeSpeed) % Animations.animations[self.animationName].numberOfFrames
            self.image = Animations.animations[self.animationName].frames[currentFrame]

      def draw(self, surf):
            surf.blit(self.image, self.rect)

      # Health bar, mana bar types
      def drawWithDuplicatesToRight(self, surf, amount):
            if amount < 1:
                  return
            self.draw(surf)
            # Gremlins were defeated in the making of this code
            for chunk in range(amount - 1):
                  self.rect.x += self.rect.width
                  self.draw(surf)
            self.rect.x -= self.rect.width * (amount - 1)

      def move(self):
            match self.moveMode:
                  case 'Stay':
                        pass
                  case 'RandomWalk':
                        match random.randint(1,3):
                              case 1:
                                    self.moveLeft()
                              case 3:
                                    self.moveRight()
                        match random.randint(1,3):
                              case 1:
                                    self.moveUp()
                              case 3:
                                    self.moveDown()
                  case 'MoveToFixedDirection':
                        pass
                  case 'MoveToTarget':
                        pass
                  case 'MoveAndTeleportToTarget':
                        pass

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

      def copy(self):
            mc = AnimatedMagicalCreatureSprite(self.animationName, self.rect.left, self.rect.top)
            mc.mana = self.mana
            mc.maxMana = self.maxMana
            mc.health = self.health
            mc.maxHealth = self.maxHealth
            mc.meleeDamage = self.meleeDamage
            return mc

##hudSprites
class Displayer(AnimatedMagicalCreatureSprite):
      def __init__(self, spawnX, spawnY):
            super().__init__("Port1",spawnX,spawnY)
            self.manaBar = AnimatedMagicalCreatureSprite('ManaP', self.rect.left + 140, self.rect.top + 57)
            self.manaRatio = 1.0
            self.healthBar = AnimatedMagicalCreatureSprite('Life', self.rect.left + 140, self.rect.top + 77)
            self.healthRatio = 1.0

      def draw(self, surf):
            super().draw(surf)
            self.manaBar.drawWithDuplicatesToRight(surf, math.ceil(10*self.manaRatio))
            self.healthBar.drawWithDuplicatesToRight(surf, math.ceil(10*self.healthRatio))

# Returns the smallest rectangle surrounding a group of sprites
def SpriteGroupRect(sg : pygame.sprite.Group):
      if sg.__len__() > 0:
            minLeft = min((o.rect.left for o in sg))
            minTop = min((o.rect.top for o in sg))
            maxRight = max((o.rect.right for o in sg))
            maxBottom = max((o.rect.bottom for o in sg))
            return pygame.rect.Rect(minLeft, minTop, maxRight - minLeft, maxBottom - minTop)
      else:
            return pygame.rect.Rect(0, 0, 0, 0)

# Returns the total mana over the total maximum mana of a sprite group
def SpriteGroupManaPercant(sg : pygame.sprite.Group):
      return sum((o.mana for o in sg)) / sum((o.maxMana for o in sg))

# Returns the total health over the total maximum health of a sprite group
def SpriteGroupHealthPercant(sg : pygame.sprite.Group):
      return sum((o.health for o in sg)) / sum((o.maxHealth for o in sg))
