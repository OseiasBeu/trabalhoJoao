import pygame
from settings import Settings
import game_functions as gf
from gun import Gun
from text_input import TextInputBox
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
    
    # Entrada de texto
    font = pygame.font.SysFont(None, 100)
    text_input_box = TextInputBox(50, 50, 400, font)
    text_input_box_group = pygame.sprite.Group(text_input_box)


    """ Criar classe nível"""

    # ===== Loop principal =====
    while True:
        gf.check_events(ai_settings,screen,text_input_box_group)
        # group.update(event_list)
        gf.update_screen(ai_settings,screen,list_words, gun,text_input_box_group)
run_game()