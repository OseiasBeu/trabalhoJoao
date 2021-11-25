import pygame
from pygame.sprite import Sprite
import random


class Word():
    """ Gera uma palavra na parte de cima da tela. """
    def __init__(self, ai_settings,screen):
        super(Word, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a palavra
        self.lista_palavras = ['Bola', 'Areia', 'Sol', 'Água', 'Vento', 'Churrasco', 'Carangueijo'] 
        self.width = 50
        self.word = ''
     
        # Inicia a palavra próximo à parte superior esqueda da tela
        self.x = float(self.width)
        self.y = 10

    def get_length_list_word(self):
        return len(self.lista_palavras)

    def get_random_word(self):
        self.word = random.choice(self.lista_palavras)
        return self.word

    
    def create_word(self, word_number,word_x):
        word = {}
        word['palavra'] = self.get_random_word()
        word['x'] = self.x + word_x
        word['y'] = self.y
        word['width'] = self.width
        word['word_number'] = word_number

        return word


    def blitme(self, x, y):
        """ Adiciona uma palavra em sua posição inicial"""
        self.screen.blit(self.word, (x,y))

