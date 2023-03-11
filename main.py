<<<<<<< HEAD
from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

ball = GameSprite('tenis_ball.png', 100, 200, 25, 50, 50)
player1 = Player('racket.png', 30, 200, 2, 50, 150)
player2 = Player('racket.png', 520, 200, 2, 50, 150)
 
run = True
finish = False
clock = time.Clock()
FPS = 60
 
speed_x = -1
speed_y = -1
 
while run:
    for e in event.get():
        if e.type == QUIT:
           run = False
    window.fill(back)
    ball.reset()
    player1.reset()
    player2.reset()
    player1.update_l()
    player2.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
  
    
    display.update()
    clock.tick(FPS)
=======
from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
run = True
finish = False
clock = time.Clock()
FPS = 60
 
 
while run:
    for e in event.get():
        if e.type == QUIT:
           run = False
  
    
    display.update()
    clock.tick(FPS)
>>>>>>> cead6cd4907a3fd66a88b6d6dc053288b15fcc59
