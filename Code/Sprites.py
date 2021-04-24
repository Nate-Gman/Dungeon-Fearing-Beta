import pygame, math, Animations

class AnimatedSprite(pygame.sprite.Sprite):
      def changeAnimation(self, animationName):
            self.animationName = animationName
            self.image = Animations.animations[animationName].frames[0]
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
            currentFrame = math.floor(self.animationTick * Animations.animations[self.animationName].timeSpeed) % Animations.animations[self.animationName].numberOfFrames
            self.image = Animations.animations[self.animationName].frames[currentFrame]

      def draw(self, surf):
            surf.blit(self.image, self.rect)

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
