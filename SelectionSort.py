from random import random, shuffle
from time import sleep
import pygame
import time


pygame.init()
clock=pygame.time.Clock()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (0,0,255)

#Window config
WIDTH, HEIGHT = 750, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Barras")
WIN.fill(WHITE)
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Algoritmo de Busqueda y Ordenamiento', False, (0, 0, 0))

def selectionSort(aList):
    for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                raise SystemExit
            for i in range(len(aList)):
                print(5)
                least = i
                for k in range(i+1, len(aList)):
                    #draw green lines to visualizate the travel
                    pygame.draw.line(WIN,GREEN,(r[k],0),(r[k],l[k]),5)
                    pygame.display.flip()
                    clock.tick(200)
                    if aList[k] < aList[least]:
                        
                        #erase the previos least red line
                        pygame.draw.line(WIN,BLACK,(r[least],0),(r[least],l[least]),5)
                        pygame.display.flip()
                        clock.tick(200)
                        least = k
                        #draw with red the least
                        pygame.draw.line(WIN,RED,(r[least],0),(r[least],l[least]),5)
                        pygame.display.flip()
                        clock.tick(200)
                    else:
                        
                        #draw Black lines again erase the green line
                        pygame.draw.line(WIN,BLACK,(r[k],0),(r[k],l[k]),5)
                        pygame.display.flip()
                        clock.tick(200) 
                swap(aList, least, i)
    
        
        

#swap least position   
def swap(A, x, y):
        temp = A[x]
#erase lines
        pygame.draw.line(WIN,WHITE,(r[y],0),(r[y],A[y]),5)
        pygame.draw.line(WIN,WHITE,(r[x],0),(r[x],A[x]),5)
        A[x] = A[y]
        A[y] = temp
        #draw the new sawp lines
        pygame.draw.line(WIN,RED,(r[y],0),(r[y],A[y]),5)
        pygame.draw.line(WIN,BLACK,(r[x],0),(r[x],A[x]),5)
        pygame.display.flip()
        clock.tick(5)
        pygame.draw.line(WIN,BLACK,(r[y],0),(r[y],A[y]),5)
        pygame.display.flip()
        clock.tick(30)
    

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, BLACK)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))
    
def createList(l,r):
    x=0
    for i in range(1,80):
        if(x+10 > 750):
            break
        x += 10
        l.append(750-x)
        r.append(x)

def randomList(l,r):
    shuffle(l)
    cont = 0
    WIN.fill(WHITE)
    for c in l:
        pygame.draw.line(WIN,BLACK,(r[cont],0),(r[cont],c),5)
        pygame.display.flip()
        clock.tick(200)
        cont+=1    

l = []
r = []
createList(l,r)
randomList(l,r)
while True:
    pygame.display.flip()
    WIN.blit(text_surface, (100,760))
    b1 = button(WIN, (150, 820), "Iniciar")
    b2 = button(WIN, (300, 820), "Reordenar")
    b3 = button(WIN, (540, 820), "Salir")
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            raise SystemExit
        '''  if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()'''

        if b1.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(1)
                selectionSort(l)
                #time.sleep(2)
        elif b2.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(2)
                randomList(l,r)
        elif b3.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        pygame.display.update()
pygame.quit()
