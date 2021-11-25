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
        self.fundo = 'assets/img/praia.png'
        # self.background_image_level1 = pygame.image.load('assets/img/praia.png').convert()
        self.music = pygame.mixer.music.load('assets/snd/theme.mp3')
        self.volume = pygame.mixer.music.set_volume(0.1)
        self.sound = pygame.mixer.music.play(-1)

        # Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3


    