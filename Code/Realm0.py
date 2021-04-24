import Sprites as s, Realms

#Sprites
r = Realms.Realm()

E1 = s.Goblin(160,520)
r.gameSprites.add(E1)
r.enemies.add(E1)

E2 = s.Demon(200,720)
r.gameSprites.add(E2)
r.enemies.add(E2)

WF = s.Fountain(800, 800)
r.gameSprites.add(WF)
r.Fountains.add(WF)

H1 = s.HPotion(500, 500)
r.gameSprites.add(H1)

M1 = s.MPotion(500, 700)
r.gameSprites.add(M1)

C1 = s.Chest(200, 300)
r.gameSprites.add(C1)

FS = s.FloorSpike(700,600)
r.gameSprites.add(FS)

FSS = s.FloorSpikeSafer(1000,1000)
r.gameSprites.add(FSS)

#Walls
for k in range(10):
      WL = s.Wall("Wall",k*80,0)
      r.gameSprites.add(WL)
      r.Walls.add(WL)

WL = s.Wall("WallCL",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WallCR",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WallCLR",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WallLR",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("BWallLR",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("BWallR",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("BWallL",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

for k in range(8):
      WL = s.Wall("BWallFill",k*80+80,-40)
      r.gameSprites.add(WL)
      r.Walls.add(WL)

WL = s.Wall("BWallCLTR",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

for k in range(8):
      WL = s.Wall("BWallTop",k*80+80,-80)
      r.gameSprites.add(WL)
      r.Walls.add(WL)

WL = s.Wall("BWallCRT",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("BWallCLT",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("BWallCRB",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("BWallCLB",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("BWallCLRB",0,0)
r.gameSprites.add(WL)
r.Walls.add(WL)
##Finished_Walls
WL = s.Wall("WA1",-1300,400)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA2",-900,-200)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA3",-900,-400)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA4",-500,-1200)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA5",-500,-900)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA6",-500,700)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA7",-200,-200)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA8",-500,-500)
r.gameSprites.add(WL)
r.Walls.add(WL)

WL = s.Wall("WA9",-1000,-1000)
r.gameSprites.add(WL)
r.Walls.add(WL)

#
PI = s.Inventory(1200, 1200)
r.gameSprites.add(PI)
PS = s.Skills(-700, -700)
r.gameSprites.add(PS)
##
XP = s.Experience(900,760)
r.gameSprites.add(XP)

HP = s.HitPoints(900,800)
r.gameSprites.add(HP)

MP = s.ManaPoints(920,820)
r.gameSprites.add(MP)
#Player
MainCharacter = s.Player(99,99)
r.gameSprites.add(MainCharacter)
r.allies.add(MainCharacter)