import pygame

class Position():
    def __init__(self, x ,y , w, h):
        self.rect = pygame.Rect( x, y, w, h)
        

class Animations():
    def __init__(self):
        self.animationList = {}

    def add(self,state,animation):
        self.animationList[state] = animation

class Animation():
    def __init__(self, imageList):
        self.imageList = imageList
        self.imageIndex = 0  # 0,1,2,3,... diye başlayan resimlerin sırasıyla başlayıp başa dönüşü için Index
        self.animationZamanlayici = 0
        self.animationSpeed = 9
    
    def update(self):
        # zamanlayiciyi da artis
        self.animationZamanlayici += 1
        # eger zamanlayici cok yuksekse
        if self.animationZamanlayici >= self.animationSpeed:
            # zamanlayiciyi resetle
            self.animationZamanlayici = 0
            self.imageIndex += 1
            # ilk gorsele donme dongusu
            if self.imageIndex > len(self.imageList) -1: # not: -1 sebebi sprite'lar 0 dan baslıyor
                self.imageIndex = 0

    def draw(self, ekran, x, y, flipX, flipY):
        #ekran.blit(self.imageList[self.imageIndex], (x,y))
        ekran.blit(pygame.transform.flip(self.imageList[self.imageIndex], flipX, flipY), (x,y))


class Entity():     # Oyun ici varlik sistemi
    def __init__(self):
        self.state = "idle"
        self.type = "normal"
        self.position = None
        self.animations = Animations()
        self.direction = "right"

