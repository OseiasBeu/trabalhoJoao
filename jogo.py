import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from words import Word


import random

def run_game():
    """ Classe responsável por executar o jogo"""
    pygame.init()
    ai_settings = Settings()

    #Criando tela priincipal
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Shot word!")

    # Cria canhão de tiro
    
    # Cria Palavras
    # word = Word(ai_settings,screen)
    word = Group()
    gf.create_list_word(ai_settings,screen,word)
   
    """ Criar classe nível"""

    #------ Inicia Musicas
    musica = pygame.mixer.music.load('assets/snd/theme.mp3')
    volume = pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    # ===== Loop principal =====
    while True:
        gf.check_events(ai_settings,screen)
        gf.update_screen(ai_settings,screen,word)

run_game()