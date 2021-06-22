# player game character sprite created by Free Game Assets
# https://free-game-assets.itch.io/free-tiny-hero-sprites-pixel-art, https://craftpix.net

# enemies sprites created by bevouliin.com ----PUBLIC DOMAIN-----
# https://opengameart.org/content/bevouliin-free-ingame-items-spike-monsters

# Heart sprites by 'NicoleMarieProductions' ----License CC-BY 3.0----
# https://opengameart.org/content/heart-1616

# Background Image:
# https://64.media.tumblr.com/84887b8a233b9a7c94425f6656ef3870/tumblr_panmkjE7Jf1wvcbfqo1_1280.png


import pygame
import engine
import araclar
# import camera  Kamera Hazır Olunca Aktive et


#------ Player Bilgi Ekranı Fonksiyon---------#
def drawText(t, x, y):
    text = font.render(t, True,_Yellow, _Dark_Grey)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x,y)  
    ekran.blit(text,text_rectangle)


#------ADIMLAR------#

# constant değişkenler

Screen_Size = (700,500)
_Dark_Grey = (177, 150, 255)
_Pink = (255, 159, 243)
_Yellow = (251, 197, 49)

# init
pygame.init()
ekran = pygame.display.set_mode(Screen_Size) 
pygame.display.set_caption("Pink Dojo's Adventures")
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(),24)
#pygame.font.get_default_font()

# Oyun Durumu = playing |Kazandı | Kaybetti
game_durum = "playing"

entities = []

#--- IMAGES ---
heart_image = pygame.image.load("character-sheets\heart.png")
coin_image = pygame.image.load("items\coin_0.png")
player_image = pygame.image.load("character-sheets\pink-dojo\main-pink-dojo.png")
background_image = pygame.image.load("character-sheets\ibackground2.png")

# Player

player_x = 300
player_y = 0
player_speed = 0
player_ivme = 0.15
player_genislik = 38
player_yukseklik = 63
player_yon = "right"
player_state = "idle" # ya da yurume

player_animations = {
    "idle": engine.Animation([
        pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_0.png"),
        pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_1.png"),
        pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_2.png"),
        pygame.image.load("character-sheets\pink-dojo-idle\dojo_idle_3.png")
    ]), 
    "walking":engine.Animation([
        pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_0.png"),
        pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_1.png"),
        pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_2.png"),
        pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_3.png"),
        pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_4.png"),
        pygame.image.load("character-sheets\pink-dojo-walk\pink-dojo_5.png"),
    ])    
}



# Platforms
platforms = [ # x ekseni soldan , y-ekseni en yukarıdan uzaklık, uzunluk, genişlik
    # Orta
    pygame.Rect(100,300,400,50),
    # Sol
    pygame.Rect(100,250,50,50),
    # Sağ
    pygame.Rect(450,250,50,50),
    
]




"""-------------------------------
   coin_animation = engine.Animation([
     pygame.image.load("items\coin_0.png"),
     pygame.image.load("items\coin_1.png"),
     pygame.image.load("items\coin_2.png"), (Yedek)
     pygame.image.load("items\coin_3.png"),
     pygame.image.load("items\coin_4.png"),
     pygame.image.load("items\coin_5.png")
 ])

coins = [
    pygame.Rect(100,200,23,23),
    pygame.Rect(200,250,23,23)
]---------------------------------
"""
""" Entity Coin nesneleri (eski)(yedek)
coin1 = engine.Entity()
coin1.position = engine.Position(100,200,23,23)
coin1Animation = engine.Animation([
     pygame.image.load("items\coin_0.png"),
     pygame.image.load("items\coin_1.png"),
     pygame.image.load("items\coin_2.png"),
     pygame.image.load("items\coin_3.png"),
     pygame.image.load("items\coin_4.png"),
     pygame.image.load("items\coin_5.png")
])
coin1.animations = engine.Animations()
coin1.animations.add("idle",coin1Animation)
coin1.type = "toplanilabilir"

coin2 = engine.Entity()
coin2.position = engine.Position(200,250,23,23)
coin2Animation = engine.Animation([
     pygame.image.load("items\coin_0.png"),
     pygame.image.load("items\coin_1.png"),
     pygame.image.load("items\coin_2.png"),
     pygame.image.load("items\coin_3.png"),
     pygame.image.load("items\coin_4.png"),
     pygame.image.load("items\coin_5.png")
])
coin2.animations = engine.Animations()
coin2.animations.add("idle",coin2Animation)
coin2.type = "toplanilabilir"
"""

#<----NESNELER---->
entities.append(araclar.coinUret(100,200))  # coin1 ve coin2 nesnesini ekler
entities.append(araclar.coinUret(200,250))
entities.append(araclar.coinUret(500,200))
entities.append(araclar.coinUret(500,250))
entities.append(araclar.dusmanUret(150,272))
#player = araclar.PlayerOlustur(300,0)
#entities.append(player)



score = 0

lives = 3
# dusman (eski kod)
#enemies_image = pygame.image.load("enemies\orange_monster.png")
#enemies = [
#    pygame.Rect(150,272,48,27),         #x,y, yukseklik(px),genislik(px)
#]


running = True
while running:
# game loop


    # <---------INPUT--------->

    # Oyundan Cikis icin kontrolleme
    for event in pygame.event.get():
        #print(event)  ----> Ekran üzerindeki eventleri görmek istiyorsan aktive et!
        if event.type == pygame.QUIT:
            running = False

    if game_durum == "playing":

        new_player_x = player_x
        new_player_y = player_y
        

        # player input
        keys = pygame.key.get_pressed()
        # sola hareket
        if keys[pygame.K_a]:
            new_player_x -= 2  # Player koordinatını 2 px sola kaydırır
            player_yon = "left"
            player_state = "walking"

        # sağa hareket
        if keys[pygame.K_d]:
            new_player_x += 2 # Player koordinatını 2 px sağa kaydırır
            player_yon = "right"
            player_state = "walking"

        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            player_state = "idle"

        # zıplama hareketi (eğer yerde ise)
        if keys[pygame.K_w] and player_yerdeyse:
            player_speed = -5

    #print(player_state)
    # update

    if game_durum == "playing":

        # ---ESKI player animation---
        player_animations[player_state].update()
        # ---update animation---
        for entity in entities:
            entity.animations.animationList[entity.state].update()

        #coin_animation.update() # (Eski Kod)

        # Horizontal hareket
        new_player_rect = pygame.Rect(new_player_x,player_y,player_genislik,player_yukseklik)
        x_collusion = False

        # ... her platform'da kontrol et
        for p in platforms:
            if p.colliderect(new_player_rect):
                x_collusion = True
                break
        # set x_collision to true

        if x_collusion == False:
            player_x = new_player_x
        # player_x = new_player_x

        # ----------vertical hareket---------------
        player_speed += player_ivme
        new_player_y += player_speed

        new_player_rect = pygame.Rect(player_x,new_player_y,player_genislik,player_yukseklik)
        y_collusion = False
        player_yerdeyse = False

        # ... her platform'da kontrol et
        for p in platforms:
            if p.colliderect(new_player_rect):
                y_collusion = True
                player_speed = 0
                # eğer platform karakterden asağıdaysa
                if p[1] > new_player_y:
                    # player'ı platforma yapıstırır
                    player_y = p[1] - player_yukseklik
                    player_yerdeyse = True
                break

        # set x_collision to true
        # print(player_yerdeyse) ---> yere değip değmediğini konsolda kontrol ettim
        if y_collusion == False:
            player_y = new_player_y

        # eğer herhangi bir coin'e denk gelirse
        player_rect = pygame.Rect(player_x,player_y,player_genislik,player_yukseklik)
        #---eski coin toplama kodu (yedek)---
        #for c in coins:
        #    if c.colliderect(player_rect):
        #        coins.remove(c)
        #        score += 1
                # score 2 ise kazan
        #        if score >= 2:
        #            game_durum = "win"

        # ---Toplanabilirlik Sistemi--- (Guncellenmis Coin Sistemi)
        for entity in entities:
            if entity.type == "toplanilabilir":
                if entity.position.rect.colliderect(player_rect):
                    entities.remove(entity)
                    score += 1
                    # score 3 ise kazan
                    if score >= 3:
                        game_durum = "win"

        # --- Dusman Sistemi ---- (Guncellendi)
        for entity in entities:
            if entity.type == "tehlikeli":
                if entity.position.rect.colliderect(player_rect):
                    lives -= 1
                    # player pozisyon resetler
                    player_x = 300
                    player_y = 0
                    player_speed = 0
                    # oyun durumunu değiştirir
                    # eğer hiç can puanı kalmadıysa
                    if lives <= 0 :
                        game_durum = "lose"

        """# player herhangi bir düşmana çarparsa
        for e in enemies:
            if e.colliderect(player_rect):
                lives -= 1
                # player pozisyon resetler
                player_x = 300
                player_y = 0
                player_speed = 0
                # oyun durumunu değiştirir
                # eğer hiç can puanı kalmadıysa
                if lives <= 0 :
                    game_durum = "lose" 
            """

    

    #print(score) terminalde test icin skor yazdırdım

    # <---DRAWING--->


    # arka-plan
    ekran.fill(_Dark_Grey)
    ekran.blit(background_image,(0,0))

    #platform

    for p in platforms:
        pygame.draw.rect(ekran, _Pink, p)

    # coins(eski kod) # silme herhangi bir durum icin dursun
    #for c in coins:
    #    ekran.blit(coin_image, (c.x,c.y))
    #    coin_animation.draw(ekran, c.x,c.y, False, False)

    # ---Ekrana Cizdirme (draw) Sistemi---

    for entity in entities:
        s = entity.state
        a = entity.animations.animationList[s]
        a.draw(ekran, entity.position.rect.x, entity.position.rect.y, False, False)
    #   coin_animation.draw(ekran, entity.position.rect.x, entity.position.rect.y, False, False)

    # enemies
    #for e in enemies:
    #    ekran.blit(enemies_image, (e.x,e.y))

    #--player-- (Eski Kodum)
    if player_yon == "right":
        #ekran.blit(player_image, (player_x,player_y)) #characters, x-koordinat, y-koordinat
        player_animations[player_state].draw(ekran, player_x,player_y, False, False )

    elif player_yon == "left":
        ekran.blit( pygame.transform.flip(player_image, True, False), (player_x,player_y))
        # Karakter Sprite'ını döndürür, flip(player_image, Horizontal Flip, Vertical Flip)
        player_animations[player_state].draw(ekran, player_x,player_y, True, False )



    #---player bilgileri---

    # score UPDATED!
    ekran.blit(coin_image, (10,10))
    drawText(str(score),50,10)

    #score (eski kod)
    #score_text = font.render("Score: "+ str(score), True,_Yellow, _Dark_Grey)
    #score_text_rectangle = score_text.get_rect()
    #score_text_rectangle.topleft = (10,10)      #Score bilgisi konumu
    #ekran.blit(score_text,score_text_rectangle)

    #can puanları
    for l in range(lives):
        ekran.blit(heart_image, (200 + (l*50),10))

    if game_durum == "win":
        # win text yazdır
        drawText("KAZANDIN!", 50, 50)
        
    if game_durum == "lose":
        # lose text yazdır
        drawText("KAYBETTIN:( ", 50, 50)

    # mevcut ekran
    
    pygame.display.flip()
    clock.tick(100) # Saniye başı kare sınırlaması (FPS)

# cikis
pygame.quit()