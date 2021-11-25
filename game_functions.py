import sys
import pygame
from words import Word

def check_events(ai_settings,screen):
    """ Responde a eventos de pressionamento de teclas e de mouse. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen)

def check_keydown_events(event, ai_settings, screen):
    """ Responde a pressionamento de teclas."""
    if event.key == pygame.K_q:
        sys.exit()
    
def update_screen(ai_settings, screen,word):
    """ Atualiza as imagens da tela."""
    # Adiciona imagem de fundo
    fundo = pygame.image.load('assets/img/praia.png').convert()
    screen.blit(fundo,(0,0))

    # Deixa a tela mais recente visivel
    word.blitme((word.x,word.y)) 
    pygame.display.flip()

def get_number_words_x(ai_settings, word_width):
    """ Determina o número de palavras que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - 2 * word_width
    number_words_x = int(available_space_x/(2* word_width))
    return number_words_x


def create_word(ai_settings, screen, words, number_words):
    word = Word(ai_settings, screen)
    word_width = word.width
    word.x = word.x +2 * word_width * number_words
    # word.y = word.y 
    words.add(word)
    return words

def create_list_word(ai_settings, screen, words):
    """ Cria a lista de palavras na tela. """
    word = Word(ai_settings, screen)
    number_words_x = get_number_words_x(ai_settings, word.width)

    for word_number in range(number_words_x):
        create_word(ai_settings, screen, words,word_number)


