'''
Created on Dec 4, 2018

@authors: M.Spencer, M. Reiling & A. Hicks 
'''

from tkinter import *
import tkinter.messagebox
import pygame
import os.path

class Game(Frame):
    def __init__(self):
        #Setup window and widgets
        Frame.__init__(self)
        self.master.title("")
        self.grid()
        
    #def _pause_menu(self):
        #Allows user to pause with Esc  

class Background():
    def __init__(self):
        #Setup background and playing area
        blit(source, (0,0), area=None, special_flags = 0)
        

    def _platforms(self):
        #Sets up the areas where players can land
        _plat2 = Image.open("../images/size_2_platform_01.jpg")
        _width2 = _plat2.size
        
        _plat3 = Image.open("../images/size_3_platform_02.jpg")
        _width3 = _plat3.size
        
        _plat5 = Image.open("../images/size_5_platform_03.jpg")
        _width5 = _plat5.size
        
        _plat7 = Image.open("../images/size_7_platform_04.jpg")
        _width7 = _plat7.size
        
        _plat11 = Image.open("../images/size_11_platform_05.jpg")
        _width11 = _plat11.size
        
        _plat13 = Image.open("../images/size_13_platform_06.jpg")
        _width13 = _plat13.size
        
class Levels(Background):
        
class Player(Background):
    def __init__(self):
        #Setup player's icon, movement, and restrictions
        
    def _movement(self):

def wait_for_key():
    e = pygame.event.wait()
    while e.type != pygame.KEYDOWN
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            return pygame.K_ESCAPE
    return e.key

def main():
    wait_for_key()