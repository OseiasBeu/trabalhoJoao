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
        ## Colocar essa lista de palavras em um arquivo
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

    
    def create_word(self, word_number,word_x,word_y):
        word = {}
        word['palavra'] = self.get_random_word()
        word['x'] = self.x + word_x
        word['y'] = self.y + word_y
        word['width'] = self.width
        word['word_number'] = word_number

        return word

    def word_coords(self,word_number):
        word_x =  word_number * 100
        pixel_number = random.randint(0,30)

        if (word_number % 2 == 0):
            word_y = word_number * pixel_number
            # word_x =  pixel_number 10
        else:
            word_y = word_number   * pixel_number 
        return word_x,word_y

            


    def blitme(self, x, y):
        """ Adiciona uma palavra em sua posição inicial"""
        self.screen.blit(self.word, (x,y))

