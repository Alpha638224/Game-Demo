import pygame
import time

screen_width = 1400
screen_height = 750
a = 0
level = 0

class Player(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load(filename)  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.vel_y = 0
        self.jumped = False
    def update(self,filename,location):
        x_move = 0
        y_move = 0
        # 获取按键，并进行相应的移动
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped is False:
            self.vel_y = -18
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            x_move -= 6
        if key[pygame.K_RIGHT]:
            x_move += 6
        # 添加角色重力（跳跃之后自然下落）
        self.vel_y += 1.5
        if self.vel_y > 18:
            self.vel_y = 18
        y_move += self.vel_y
        self.rect.x += x_move
        self.rect.y += y_move
        # 控制人物的最低位置
        if level == 0 or level == 1 or level == 2:
            if self.rect.bottom > screen_height - 157 and (self.rect.x < 528 or (self.rect.x > 688 and self.rect.x < 952) or self.rect.x > 1100):
                self.rect.bottom = screen_height - 157
            screen.blit(self.image, self.rect)
        if level == 3:
            if self.rect.bottom > screen_height - 157 and self.rect.x < 430:
                self.rect.bottom = screen_height - 157
            elif self.rect.bottom > screen_height - 250 and self.rect.x > 430:
                self.rect.bottom = screen_height - 250
            elif self.rect.bottom > screen_height - 270 and self.rect.x > 700:
                self.rect.bottom = screen_height - 270
            elif self.rect.bottom > screen_height - 157 and self.rect.x > 800:
                self.rect.bottom = screen_height - 157
            screen.blit(self.image, self.rect)
        
class Ground(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load(filename)  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.jumped = False
    def update(self,filename,location):
        screen.blit(self.image, self.rect)

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Radish 0.0')  # 设置窗口名称
screen.fill((255,255,255))  # 填充为白色屏幕
player = Player("Radish.jpg",(100,300))
ground = Ground("Level3.png",(-290,593))
ground2 = Ground("ground3.png",(756,593))
ground3 = Ground("ground3.png",(1165,593))
ground4 = Ground("platform.png",(1500,600))
ground5 = Ground("platform.png",(1500,600))
ground6 = Ground("platform.png",(1500,600))
flag = Ground("flag.png",(1185,302))
space = pygame.image.load("space.png").convert()
level_completed = pygame.image.load("level_completed.png").convert()
clock = pygame.time.Clock()
level = 1

while True:
    screen.blit(space, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
while True:
    clock.tick(60)
    screen.fill((255,255,255))
    flag.update("0.jpg",(0,0))
    screen.blit(player.image,player.rect)  # 绘制精灵到屏幕上
    screen.blit(ground.image,ground.rect)
    player.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground2.update("0.jpg",(0,0))
    ground3.update("0.jpg",(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if player.rect.x > 1150:
        break
    pygame.display.update()  # 刷新显示屏幕
    
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
player.rect.x = 100
player.rect.y = 520
ground.rect.x = -500
ground4.rect.x = 500
ground4.rect.y = 592
ground5.rect.x = 766
ground5.rect.y = 592
ground6.rect.x = 911
ground6.rect.y = 592
ground2.rect.x = 1175
level = 2
        
while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    flag.update("0.jpg",(0,0))
    player.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground2.update("0.jpg",(0,0))
    ground4.update("0.jpg",(0,0))
    ground5.update("0.jpg",(0,0))
    ground6.update("0.jpg",(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if player.rect.x > 1150:
        break
    
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
player.rect.x = 100
player.rect.y = 520
ground4.rect.y = 500
ground5.rect.y = 480
ground6.rect.y = 480
level = 3

while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    flag.update("0.jpg",(0,0))
    player.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground2.update("0.jpg",(0,0))
    ground4.update("0.jpg",(0,0))
    ground5.update("0.jpg",(0,0))
    ground6.update("0.jpg",(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if player.rect.x > 1150:
        break
    
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01