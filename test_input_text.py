# import pygame
# pygame.init()
# window = pygame.display.set_mode((500, 200))
# clock = pygame.time.Clock()

# font = pygame.font.SysFont(None, 100)
# text = ""
# input_active = True

# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             input_active = True
#             text = ""
#         elif event.type == pygame.KEYDOWN and input_active:
#             if event.key == pygame.K_RETURN:
#                 input_active = False
#                 print(text)
#             elif event.key == pygame.K_BACKSPACE:
#                 text =  text[:-1]
#             else:
#                 text += event.unicode

#         window.fill(0)
#         text_surf = font.render(text, True, (255, 255, 0))
#         window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
#         pygame.display.flip()

# pygame.quit()
# exit()

# import pygame

# class TextInputBox(pygame.sprite.Sprite):
#     def __init__(self, x, y, w, font):
#         super().__init__()
#         self.color = (255, 255, 255)
#         self.backcolor = None
#         self.pos = (x, y) 
#         self.width = w
#         self.font = font
#         self.active = False
#         self.text = ""
#         self.render_text()

#     def render_text(self):
#         t_surf = self.font.render(self.text, True, self.color, self.backcolor)
#         self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
#         if self.backcolor:
#             self.image.fill(self.backcolor)
#         self.image.blit(t_surf, (5, 5))
#         pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
#         self.rect = self.image.get_rect(topleft = self.pos)

#     def update(self, event_list):
#         for event in event_list:
#             if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
#                 self.active = self.rect.collidepoint(event.pos)
#             if event.type == pygame.KEYDOWN and self.active:
#                 if event.key == pygame.K_RETURN:
#                     print(self.text)
#                     self.active = False
#                 elif event.key == pygame.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += event.unicode
#                 self.render_text()

# pygame.init()
# window = pygame.display.set_mode((500, 200))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 100)

# text_input_box = TextInputBox(50, 50, 400, font)
# group = pygame.sprite.Group(text_input_box)

# run = True
# while run:
#     clock.tick(60)
#     event_list = pygame.event.get()
#     for event in event_list:
#         if event.type == pygame.QUIT:
#             run = False
#     group.update(event_list)

#     window.fill(0)
#     group.draw(window)
#     pygame.display.flip()

# pygame.quit()
# exit()

import pygame_textinput
import pygame
pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 10))

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(30)