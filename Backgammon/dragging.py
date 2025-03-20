import config as c
import bgsetup as bgs
import pygame

def checkDragClick():
    c.dragPieces = []
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pieceClicked = False
    for piece in c.blackPieces:
        if bgs.is_circle_clicked(piece[0][0], piece[0][1], piece[1], mouse_x, mouse_y):
            c.is_dragging = True
            c.drag_color = c.color
            c.blackPieces.remove(piece)
            c.drag_pieces.append([c.drag_color,piece[0],piece[1]])
            pieceClicked = True
            break
    if(not pieceClicked):
        for piece in c.whitePieces:
            if bgs.is_circle_clicked(piece[0][0], piece[0][1], piece[1], mouse_x, mouse_y):
                c.is_dragging = True
                c.drag_color = c.gray
                c.whitePieces.remove(piece)
                c.drag_pieces.append([c.drag_color,piece[0],piece[1]])
                break

def checkDragRelease():
    c.is_dragging = False
    if (len(c.drag_pieces) >0):
        finalDrag = c.drag_pieces.pop(0)
        if (isValidMove(finalDrag)):
            if (finalDrag[0] == c.gray):
                finalDrag.pop(0)
                c.whitePieces.append(finalDrag)
            else:
                finalDrag.pop(0)
                c.blackPieces.append(finalDrag)

def checkDragging():
    if(c.is_dragging):
        mouse_pos = pygame.mouse.get_pos()
        c.drag_pieces.append([c.drag_color,mouse_pos,c.radius])
    if(len(c.drag_pieces) > 1):
        c.drag_pieces.pop(0)

        
def isValidMove(position):
    pass