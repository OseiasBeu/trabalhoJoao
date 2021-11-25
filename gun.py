import pygame

class Gun():
    def __init__(self,ai_settings, screen):
        """ Inicializa canhão na tela"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega canhão e obtem o rect
        self.image = pygame.image.load('assets/img/Canhão.bmp')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializa o canhão na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """ Desenha cannhão no centro da tela"""
        self.screen.blit(self.image, self.rect)
