import pygame
from settings import Settings
import game_functions as gf
from gun import Gun
import text_input

def run_game():
    """ Classe responsável por executar o jogo"""
    pygame.init()
    ai_settings = Settings()

    #Criando tela principal
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Shot word!")

    # Cria canhão de tiro
    gun = Gun(ai_settings, screen)

    # Cria lista Palavras
    list_words = gf.create_list_word(ai_settings,screen)

    # Create TextInput-object
    textinput = text_input.inicialize_text_input()

    """ Criar classe nível"""

    # ===== Loop principal =====
    while True:
        gf.check_events(ai_settings,screen, textinput)
        gf.update_screen(ai_settings,screen,list_words, gun,textinput)
run_game()