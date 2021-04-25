import pygame

class Animation():
      def __init__(self, imagePath, numberOfFrames, timeSpeed):
            loadedImage = pygame.image.load(imagePath)
            frameX, frameY = loadedImage.get_width() // numberOfFrames, loadedImage.get_height()
            self.numberOfFrames = numberOfFrames
            self.timeSpeed = timeSpeed
            self.frames=[]
            for k in range(numberOfFrames):
                  self.frames.append(loadedImage.subsurface((k * frameX, 0, frameX, frameY)))

animations = {
      #hudSprites
      "Port1": Animation("../Graphics/Images/PlayerDisplay352x137.png",1,0),
      #
      "PInvt": Animation("../Graphics/Images/InventorySheet384x384.png",1,0),
      "PSkill": Animation("../Graphics/Images/SkillsLevelsTile142x270.png",1,0),
      #Player
      "Player1": Animation("../Graphics/Images/MainCharRIdolTile75x66.png",6,0.4),
      "ExpP": Animation("../Graphics/Images/XPBarTile20x10.png",10,1),
      "Life": Animation("../Graphics/Images/HealthBarTile 20x18.png",10,0.3),
      "ManaP": Animation("../Graphics/Images/ManaBarTile20x18.png",10,0.3),
      #NPC
      "NPC_HPD": Animation("../Graphics/Images/EnemyHealthDisplay84x8.png",1,0),
      "NPC_HP": Animation("../Graphics/Images/EnemyHealth82x6.png",4,0.3),
      #Shop
      "ShopKeep": Animation("../Graphics/Images/ShopKeepStand39x61.png",4,0.2),
      #Enemy
      "GoblinR": Animation("../Graphics/Images/GoblinR.png",5,0.3),
      "DemonL": Animation("../Graphics/Images/DemonLTile43x32.png",6,0.3),
      "GhostDeath": Animation("../Graphics/Images/GhostDeath43x56.png",9,0.4),
      #Misc
      "HPOT": Animation("../Graphics/Images/LessHealPotTile14x23.png",9,0.4),
      "MPOT": Animation("../Graphics/Images/LessManaPotTile 14x23.png",9,0.4),
      #Interactive
      "RedFountain": Animation("../Graphics/Images/RedFountainTile142x111.png",4,0.2),
      "Fountain": Animation("../Graphics/Images/Fountain.png",5,0.3),
      "Chest": Animation("../Graphics/Images/ChestClosed 20x20.png",1,0),
      "Spike": Animation("../Graphics/Tile_set/Floor_Spike.png",8,0.08),
      "SSafer": Animation("../Graphics/Tile_set/Floor_Spike_Safer.png",12,0.08),
      #WallTILES
      "Wall": Animation("../Graphics/Tile_set/Wall.png",1,0),
      "WallCL": Animation("../Graphics/Tile_set/WallCL.png",1,0),
      "WallCR": Animation("../Graphics/Tile_set/WallCR.png",1,0),
      "WallCLR": Animation("../Graphics/Tile_set/WallCLR.png",1,0),
      "WallLR": Animation("../Graphics/Tile_set/WallLR.png",1,0),
      "BWallLR": Animation("../Graphics/Tile_set/BWallLR.png",1,0),
      "BWallR": Animation("../Graphics/Tile_set/BWallR.png",1,0),
      "BWallL": Animation("../Graphics/Tile_set/BWallL.png",1,0),
      "BWallFill": Animation("../Graphics/Tile_set/BWallFill.png",1,0),
      "BWallTop": Animation("../Graphics/Tile_set/BWallTop.png",1,0),
      "BWallCRT": Animation("../Graphics/Tile_set/BWallCRT.png",1,0),
      "BWallCLT": Animation("../Graphics/Tile_set/BWallCLT.png",1,0),
      "BWallCRB": Animation("../Graphics/Tile_set/BWallCRB.png",1,0),
      "BWallCLB": Animation("../Graphics/Tile_set/BWallCLB.png",1,0),
      "BWallCLRB": Animation("../Graphics/Tile_set/BWallCLRB.png",1,0),
      "BWallCLTR": Animation("../Graphics/Tile_set/BWallCLTR.png",1,0),
      #Finished Walls
      "WA1": Animation("../Graphics/Finished_walls/EmptyWallPillar80x80.png",1,0),
      "WA2": Animation("../Graphics/Finished_walls/WallPillar80x80.png",1,0),
      "WA3": Animation("../Graphics/Finished_walls/StrongWallPillar80x120.png",1,0),
      "WA4": Animation("../Graphics/Finished_walls/SmallRectWall320x80.png",1,0),
      "WA5": Animation("../Graphics/Finished_walls/MediumRectWall320x120.png",1,0),
      "WA6": Animation("../Graphics/Finished_walls/LargeRectWall320x160.png",1,0),
      "WA7": Animation("../Graphics/Finished_walls/LargeSquareWall320x279.png",1,0),
      "WA8": Animation("../Graphics/Finished_walls/Virtical160x279.png",1,0),
      "WA9": Animation("../Graphics/Finished_walls/LongVerticalWall160x879.png",1,0),
      "WA10": Animation("../Graphics/Finished_walls/CliffHole1280X400.png",1,0),
      "WA11": Animation("../Graphics/Finished_walls/HugeTallWall1280X400.png",1,0),
      "WA12": Animation("../Graphics/Finished_walls/UWallLower1120x72.png",1,0),
      "WA13": Animation("../Graphics/Finished_walls/HugeSquareWall1280X400.png",1,0),
      #Connect A Wall
      "HWA6A": Animation("../Graphics/Finished_walls/HorizontalWall1 160x559.png",1,0),
      "WA2AB": Animation("../Graphics/Finished_walls/HorizontalWall1 559x232.png",1,0),
      "HWA4C": Animation("../Graphics/Finished_walls/LowerLeftWall1 1120x160.png",1,0),
      "HWA4D": Animation("../Graphics/Finished_walls/LowerRightWall1 1120x160.png",1,0),
      "HWA4E": Animation("../Graphics/Finished_walls/UpperLeftWall1 1120x160.png",1,0),
      "HWA4F": Animation("../Graphics/Finished_walls/UpperRightWall1 1120x160.png",1,0),
      "VWA4G": Animation("../Graphics/Finished_walls/VerticalWall1 160x559.png",1,0),
      "VWA6H": Animation("../Graphics/Finished_walls/VerticalWallLeft 129x 1120.png",1,0),
      "VWA6I": Animation("../Graphics/Finished_walls/VerticalWallRight 129x 1120.png",1,0),
      "VWA2J": Animation("../Graphics/Finished_walls/VerticalWallTopLeft 129x 1120.png",1,0),
      "VWA2K": Animation("../Graphics/Finished_walls/VerticalWallTopRight 129x 1120.png",1,0),
      }
