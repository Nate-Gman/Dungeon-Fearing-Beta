import pygame, Sprites, Settings

class Realm():
    def __init__(self, name):
        self.name = name
        self.gameSprites = pygame.sprite.Group()
        self.Walls = pygame.sprite.Group()
        self.allyFountains = pygame.sprite.Group()
        self.enemyFountains = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.allies = pygame.sprite.Group()

    def export(self):
        exportFile = open('ExportedRealm' + self.name + '.py','w')
        exportFile.write('#Generated by exporting\nimport Sprites as s, Realms\n\n#Sprites\nr = Realms.Realm(\'' + self.name + '\')\n\n')

        for sp in self.gameSprites:
            # Export single sprite
            exportFile.write('#\nsp = s.AnimatedMagicalCreatureSprite(\'' + sp.animationName + '\', ' + str(sp.rect.left) + ', ' + str(sp.rect.top) + ')\n')
            if sp.movementSpeed != Sprites.DefaultMovementSpeed:
                exportFile.write('sp.movementSpeed = ' + str(sp.movementSpeed) + '\n')
            if sp.targetSprite != None:
                exportFile.write('sp.targetSprite = ' + str(sp.targetSprite) + '\n')
            if sp.moveMode != Sprites.DefaultMoveMode:
                exportFile.write('sp.moveMode = ' + str(sp.moveMode) + '\n')
            if sp.maxMana != Sprites.DefaultMaxMana:
                exportFile.write('sp.maxMana = ' + str(sp.maxMana) + '\n')
            if sp.maxMana != sp.mana:
                exportFile.write('sp.mana = ' + str(sp.mana) + '\n')
            if sp.maxHealth != Sprites.DefaultMaxMana:
                exportFile.write('sp.maxHealth = ' + str(sp.maxHealth) + '\n')
            if sp.maxHealth != sp.health:
                exportFile.write('sp.health = ' + str(sp.health) + '\n')
            if sp.meleeDamage != Sprites.DefaultMeleeDamage:
                exportFile.write('sp.meleeDamage = ' + str(sp.meleeDamage) + '\n')
            if sp.healBuff != Sprites.DefaultHealBuff:
                exportFile.write('sp.healBuff = ' + str(sp.healBuff) + '\n')
            if sp.manaBuff != Sprites.DefaultManaBuff:
                exportFile.write('sp.manaBuff = ' + str(sp.manaBuff) + '\n')
            exportFile.write('r.gameSprites.add(sp)\n')
            if self.Walls.has(sp):
                exportFile.write('r.Walls.add(sp)\n')
            if self.allyFountains.has(sp):
                exportFile.write('r.allyFountains.add(sp)\n')
            if self.enemyFountains.has(sp):
                exportFile.write('r.enemyFountains.add(sp)\n')
            if self.enemies.has(sp):
                exportFile.write('r.enemies.add(sp)\n')
            if self.allies.has(sp):
                exportFile.write('r.allies.add(sp)\n')
        exportFile.close()

    def teleportAllSprites(self, east, south):
        if east == 0 and south == 0: # Sometimes save computation
            return
        for sprite in self.gameSprites:
            sprite.rect.left += east
            sprite.rect.top += south

    def PrintRealmToSurface(self):
        AllSpriteRect = Sprites.SpriteGroupRect(self.gameSprites)
        OutSurface = pygame.surface.Surface(AllSpriteRect.size)
        OutSurface.fill(Settings.FloorColor)
        self.teleportAllSprites(-AllSpriteRect.left, -AllSpriteRect.top)
        for sprite in self.gameSprites:
            sprite.draw(OutSurface)
        self.teleportAllSprites(AllSpriteRect.left, AllSpriteRect.top)
        return OutSurface
