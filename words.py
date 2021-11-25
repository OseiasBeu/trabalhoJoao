import pygame
from pygame.sprite import Sprite
import random


class Word(Sprite):
    """ Gera uma palavra na parte de cima da tela. """
    def __init__(self, ai_settings,screen):
        super(Word, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a palavra
        self.lista_palavras = ['Bola', 'Areia', 'Sol', 'Água', 'Vento', 'Churrasco', 'Carangueijo']
        self.word =  random.choice(self.lista_palavras)
        # self.rect = (0,0)
        self.width = 50
        self.word = self.ai_settings.fonte.render(self.word, True,(0,0,0))
        
        # Inicia a palavra próximo à parte superior esqueda da tela
        self.x = float(self.width)
        self.y = 0

        # Armazena a posição da palavra
        # self.x = float(self.rect.x)

    def get_length_list_word(self):
        return len(self.lista_palavras)

    def blitme(self, x, y):
        """ Adiciona uma palavra em sua posição inicial"""
        self.screen.blit(self.word, (x,y))

