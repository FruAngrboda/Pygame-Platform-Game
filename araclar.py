import pygame
import engine

#--------- COIN SPRITE KARELERI -----------#
coin0 = pygame.image.load("items\coin_0.png")
coin1 = pygame.image.load("items\coin_1.png")
coin2 = pygame.image.load("items\coin_2.png")
coin3 = pygame.image.load("items\coin_3.png")
coin4 = pygame.image.load("items\coin_4.png")
coin5 = pygame.image.load("items\coin_5.png")

def coinUret(x, y): # Coin Uretme Fonksiyonu
    entity = engine.Entity()
    entity.position = engine.Position(x, y,23,23)
    entityAnimation = engine.Animation([
       coin0,
       coin1,
       coin2,
       coin3,
       coin4,
       coin5 
    ])
    entity.animations.add("idle",entityAnimation)
    entity.type = "toplanilabilir"
    return entity

# Dusman Sprite Karesi
dusman0 = pygame.image.load("enemies\orange_monster.png")
def dusmanUret(x, y): # Dusman Uretme Fonksiyonu
    entity = engine.Entity()
    entity.position = engine.Position(x, y,48,27)
    entityAnimation = engine.Animation([
       dusman0 
    ])
    entity.animations.add("idle",entityAnimation)
    entity.type = "tehlikeli"
    return entity


"""
idle0 = pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_0.png"),
idle1 = pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_1.png"),
idle2 = pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_2.png")
idle3 = pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_3.png")

walking0 = pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_0.png")
walking1 = pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_1.png")
walking2 = pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_2.png")
walking3 = pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_3.png")
walking4 = pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_4.png")
walking5 = pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_5.png")


def PlayerOlustur(x, y): # Player Uretme Fonksiyonu
    entity = engine.Entity()
    entity.position = engine.Position(x, y,38,63)
    entityIdleAnimation = engine.Animation([idle0,idle1,idle2,idle3 ])
    entityWalkingAnimation = engine.Animation([walking0,walking1,walking2,walking3,walking4,walking5 ])
    entity.animations.add("idle",entityIdleAnimation)
    entity.animations.add("walking",entityWalkingAnimation)
    entity.type = "player"
    return entity"""