import pygame
from settings import Settings
import game_functions as gf
from gun import Gun

def run_game():
    """ Classe responsável por executar o jogo"""
    pygame.init()
    ai_settings = Settings()

    #Criando tela priincipal
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Shot word!")

    # Cria canhão de tiro
    gun = Gun(ai_settings, screen)

    # Cria lista Palavras
    list_words = gf.create_list_word(ai_settings,screen)
   
    """ Criar classe nível"""

    # ===== Loop principal =====
    while True:
        gf.check_events(ai_settings,screen)
        gf.update_screen(ai_settings,screen,list_words, gun)
run_game()