import pygame

class Animation():
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
