import pygame_textinput
import os
import sys

def inicialize_text_input():
    text_input = pygame_textinput.TextInputVisualizer()
    return text_input

def remove_word(word_digitalized):
    print(f'Teste: {word_digitalized}')
    list_words_removed = []
    list_words_removed.append(word_digitalized)
    if os.path.exists("palavrasExcluidas.txt"):
        f = open("palavrasExcluidas.txt", "a")
        f.write(f'{word_digitalized},')
        f.close()
    else:
        f = open("palavrasExcluidas.txt", "w")
        f.write(f'{word_digitalized},')
        f.close()

def deleteFileWords():
    if os.path.exists("palavrasExcluidas.txt"):
        os.remove("palavrasExcluidas.txt")
    else:
        print("The file does not exist")

def readFileWords():
    if os.path.exists("palavrasExcluidas.txt"):
        fileObj = open('palavrasExcluidas.txt', "r") #opens the file in read mode
        words = fileObj.read().split(',') #puts the file into an array
        fileObj.close()
        print(words)
        return words
    else:
        f = open("palavrasExcluidas.txt", "w")
        f.write('vazio,')
        f.close()
        



readFileWords()