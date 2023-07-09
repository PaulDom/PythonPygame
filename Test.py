import pygame

# Проверяем правильность подключения библиотеки
pygame.init()

# Создаем цвета в формате rgb
red = [255, 0, 0]
green_spec = [15, 171, 119]
white = [255,255,255]
black = [0,0,0]
grey = [150,150,150]

class TextArea():
    def __init__(self, x=100, y=100, width=100, height=50, color=white):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def set_text(self, text, size=40, color=black):
        font1 = pygame.font.Font(None, size)
        self.text = font1.render(text, True, color)

    def draw_rect(self, shift_x=0, shift_y=0):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, [self.rect.x + shift_x, self.rect.y + shift_y])

# Создаем экран размером 500x500
window = pygame.display.set_mode([500, 500])
# Заливаем экран цветом
window.fill(grey)

# Создаем и настраиваем проямоугольник
question = TextArea(100, 100, 200, 100, white)
question.set_text("Вопрос")
question.draw_rect(80, 30)

# Создаем экземпляр часов
clock = pygame.time.Clock()

'''
# Создаем прямоугольник
rect1 = pygame.Rect(250, 50, 100, 50)
# Рисуем на холсте прямоугольник
pygame.draw.rect(window, red, rect1)

# Создаем шрифт
font1 = pygame.font.Font(None, 30)
# Создаем надпись
text1 = font1.render("Тестируем", True, green_spec)
# Рисуем надпись на холсте
window.blit(text1, [260, 60])
'''

# Создаем игровой цикл
while True:
    pygame.display.update()
    clock.tick(60)
