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
        
class Player():
    def __init__(self):
        #Setup player's icon, movement, and restrictions
        super().__init__()
 
        # Loads an image of the minecart, and sets up its size
        _cart = Image.open("../images/size_2_platform_01.jpg")
        _cartWidth, _cartHeight = _plat2.size
        self._cartImage = pygame.Surface(_cartWidth, _cartHeight)
 
        # Set a reference to the image rect
        self._cart_rect = self._cartImage.get_rect()
 
        # Set speed vector of player
        self._leftRight = 0
        self._upDown = 0
 
        # List of platforms we can roll on
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.leftRight
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # We only want the player to move right, 
            # so we set our right side to the left side of the item we hit
            if self.leftRight > 0:
                self.rect.right = block.rect.left
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self._upDown == 0:
            self._upDown = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self._upDown >= 0:
            self._upDown = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    # Player's movement
    def jump(self):
        # Called when user hits 'jump' button.
        # move down a bit and see if there is a platform below us.
        self.rect.y += 3
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 3
 
        #Set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -8
    
    def go_left(self):
        # Called when the user hits the left arrow.
        self.change_x = -5
 
    def go_right(self):
        # Called when the user hits the right arrow.
        self.change_x = 5
 
    def stop(self):
        """ Called when the user lets off the keyboard.
        self.change_x = 0

def keyentry(): 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

def main():
    keyentry()
    
