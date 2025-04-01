import sys
import pygame
import bgsetup as bgs
import config as c
import dragging as d

#initialize pygame
pygame.init()

#create the starting pieces
bgs.createPieces()

#create the rectangles
bgs.createSpaces()

while c.running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            d.checkDragClick()
            
        elif event.type==pygame.MOUSEBUTTONUP:
            d.checkDragRelease()  

        elif event.type==pygame.MOUSEMOTION:
            d.checkDragging()

    c.myScreen.fill(c.white)

    bgs.drawEverything()

    pygame.display.flip()

pygame.quit()
sys.exit()


#if the piece(s) is available to move AND the number of spaces moved equals the dice roll, then move
#if it doesn't the move is invalid