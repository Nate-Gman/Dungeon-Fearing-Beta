#Generated by exporting
import Sprites as s, Realms

#Sprites
r = Realms.Realm('0')

#
sp = s.MagicalCreature('GoblinR', 912, 980)
r.gameSprites.add(sp)
r.enemies.add(sp)
#
sp = s.MagicalCreature('DemonL', 847, 972)
r.gameSprites.add(sp)
r.enemies.add(sp)
#
sp = s.Fountain('Fountain', 1011, 567)
r.gameSprites.add(sp)
r.allyFountains.add(sp)
#
sp = s.AnimatedSprite('HPOT', 1252, 960)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('MPOT', 1219, 957)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('Chest', 952, 760)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('Spike', 1348, 848)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('SSafer', 1288, 848)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('WA1', 82, 927)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA2', -88, 661)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA3', 109, 331)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA4', 451, 13)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA5', 680, 130)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA6', 252, 1160)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA7', 552, 260)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA8', 252, -40)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('WA9', -248, -540)
r.gameSprites.add(sp)
r.Walls.add(sp)
#
sp = s.AnimatedSprite('PInvt', 437, 582)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('PSkill', 231, 621)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('ExpP', 1328, 591)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('Life', 1328, 614)
r.gameSprites.add(sp)
#
sp = s.AnimatedSprite('ManaP', 1328, 645)
r.gameSprites.add(sp)
#
sp = s.MagicalCreature('Player1', 1003, 405)
sp.meleeDamage = 2
r.gameSprites.add(sp)
r.allies.add(sp)
#
sp = s.MagicalCreature('Player1', 867, 590)
sp.meleeDamage = 2
r.gameSprites.add(sp)
r.allies.add(sp)
