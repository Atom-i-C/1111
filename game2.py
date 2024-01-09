from pygame import *

# Задаем размеры экрана
screen_width = 640
screen_height = 480

# Задаем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создаем класс для платформ
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_wight,player_height,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_wight,player_height))
        self.size_x = player_wight
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect. y= player_y

    
    def update(self):
        # Устанавливаем скорость платформы
        speed = 5
        keys = key.get_pressed()
        
        # Двигаем платформу влево или вправо в зависимости от нажатой клавиши
        if keys[K_LEFT]:
            self.rect.x -= speed
        if keys[K_RIGHT]:
            self.rect.x += speed
        
        # Устанавливаем границы для платформы
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

# Создаем класс для мячика
class Ball(GameSprite):
    def __init__(self, player_image,player_x,player_y,player_wight,player_height,player_speed, dy, dx):
        super().__init__(player_image,player_x,player_y,player_wight,player_height,player_speed)
        self.dx = dx
        self.dy = dy
    
    def update(self):
        # Двигаем мячик по горизонтали и вертикали
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        # Отскакиваем от границ экрана
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.dy *= -1


# Создаем экран
screen = display.set_mode((screen_width, screen_height))
display.set_caption("хахах.jpg")

# Инициализируем группы спрайтов
all_sprites = sprite.Group()
platforms = sprite.Group()
balls = sprite.Group()

# Создаем платформы
platform1 = GameSprite('пратформа.png',300, 450, 70, 30, 6)
platform2 = GameSprite('пратформа.png',300, 20, 70, 30, 6)

# Создаем мячики
ball = Ball('дёрн.jpg', 320, 240, 45, 45, 10, 2,2 )

# Добавляем платформы и мячики в группы спрайтов
all_sprites.add(platform1)
all_sprites.add(platform2)
all_sprites.add(ball)
platforms.add(platform1)
platforms.add(platform2)
balls.add(ball)


# Задаем частоту обновления экрана


# Создаем игровой цикл
running = True
while running:
    # Ограничиваем частоту обновления экрана
    time.delay(30)
    
    # Обрабатываем события
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    # Обновляем платформы и мячики
    all_sprites.update()
    
    # Проверяем столкновение мячиков с платформами
    for ball in balls:
        if sprite.spritecollide(ball, platforms, dokill=False):
            ball.dy *= -1
    
    # Очищаем экран
    screen.fill(BLACK)
    
    # Рисуем все спрайты на экране
    all_sprites.draw(screen)
    
    # Обновляем содержимое экрана
    display.flip()

# Завершаем программу
quit()