import sys
import pygame
from words import Word

def check_events(ai_settings,screen,text_input_box_group):
    """ Responde a eventos de pressionamento de teclas e de mouse. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,text_input_box_group)



def check_keydown_events(event, ai_settings, screen, text_input_box_group):
    """ Responde a pressionamento de teclas."""
    if event.key == pygame.K_q:
        sys.exit()
    else:
        text_input_box_group.update(pygame.event.get())


    
def update_screen(ai_settings, screen,list_words, gun,text_input_box_group):
    """ Atualiza as imagens da tela."""
    #------ Inicia Musicas
    ai_settings.sound

    # Adiciona imagem de fundo
    fundo = pygame.image.load('assets/img/praia.png').convert()
    screen.blit(fundo,(0,0))

    # Adiciona palavras na tela
    for word in list_words:
        screen.blit(ai_settings.fonte.render(word['palavra'], True,(0,0,0)),(word['x'],word['y']))
    gun.blitme()

    text_input_box_group.draw(screen)
    pygame.display.flip()


def get_number_words_x(ai_settings, word_width):
    """ Determina o número de palavras que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - 2 * word_width
    number_words_x = int(available_space_x/(2* word_width))
    return number_words_x

def create_list_word(ai_settings, screen):
    """ Cria a lista de palavras na tela. """
    word = Word(ai_settings, screen)

    number_words_x = get_number_words_x(ai_settings, word.width)
    list_words = []

    for word_number in range(number_words_x):
        word_x, word_y = word.word_coords(word_number)
        list_words.append(word.create_word(word_number,word_x,word_y))
    
    return list_words