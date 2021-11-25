import pygame

class Settings():
    """Uma classe para armazenar todas as configurações do jogo."""
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 920
        self.screen_height = 690
        self.bg_color = (230, 230, 230)
        self.fonte = pygame.font.SysFont('arial',30,True,True)
        # self.fundo = pygame.image.load('assets/img/praia.png').convert()
        # self.background_image_level1 = pygame.image.load('assets/img/praia.png').convert()

        # Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5
    