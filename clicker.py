import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
screen_w, screen_h = 800,800
screen = pygame.display.set_mode((screen_w,screen_h))
menu = pygame.Surface((800,800))
start = pygame.Rect(75,400,((screen_w//2)-100),200)
end = pygame.Rect(450,400,((screen_w//2)-100),200)
coord = []

def gen_rand_cord():
    global coord
    coord = []
    randx = random.randint(100,500)
    randy = random.randint(100,500)
    coord.append(randx)
    coord.append(randy)
    return coord

gen_rand_cord()
target = pygame.Rect(coord[0],coord[1],50,50)

def generate_circle():
    pygame.draw.rect(screen,(255,255,255),target)

def check_hover():
    global target
    pos = pygame.mouse.get_pos()
    if pos[0] >= target.left and pos[0] <= target.right and pos[1] <= target.bottom and pos[1] >= target.top:
        return True
    else:
        return False

def delete_cirlce():
    gen_rand_cord()
    target.update(coord[0],coord[1],50,50)

def draw_menu():
    global counter,miss,hit
    menu.fill((0,0,0))
    screen.blit(menu,(0,0))
    pygame.draw.rect(screen,(255,0,0),start)
    pygame.draw.rect(screen,(255,0,0),end)
    
    miss_text = font.render(f'Miss: {miss}', True, (255, 0, 0))
    score_text = font.render(f'Score: {hit}', True, (255, 255, 255))
    screen.blit(score_text, (350, 200))
    screen.blit(miss_text, ((350, 250)))
    start_text = font.render(f'START', True, (0, 255, 0))
    end_text = font.render(f'END', True, (0, 255, 0))
    screen.blit(start_text,(start.centerx-30,start.centery-15))
    screen.blit(end_text,(end.centerx-30,end.centery-15))
    
    pos = pygame.mouse.get_pos()
    if pos[0] >= start.left and pos[0] <= start.right and pos[1] <= start.bottom and pos[1] >= start.top and event.type == pygame.MOUSEBUTTONDOWN:
        counter = 30
        miss = 0
        hit = 0
    if pos[0] >= end.left and pos[0] <= end.right and pos[1] <= end.bottom and pos[1] >= end.top and event.type == pygame.MOUSEBUTTONDOWN:
        pygame.quit()
        quit()





miss = 0
hit = 0
counter = 0
pygame.time.set_timer(pygame.USEREVENT,1000)
def draw_text():
    miss_text = font.render(f'Miss: {miss}', True, (255, 0, 0))
    score_text = font.render(f'Score: {hit}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(miss_text, ((screen_w-100), 10))
    time_display = font.render(f'Time Left: {counter}',True,(255,255,255))
    screen.blit(time_display,(((screen_w//2)-50),10))

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if counter > 0 and event.type == pygame.USEREVENT:
            counter-=1
        if check_hover() == True and event.type == pygame.MOUSEBUTTONDOWN and counter>0:
            delete_cirlce()
            hit = hit+1
        elif check_hover != True and event.type == pygame.MOUSEBUTTONDOWN and counter>0:
            miss=miss + 1
    
    font = pygame.font.Font(None,36)
    screen.fill((0,0,0))
    generate_circle()
    draw_text()
    if counter == 0:
        draw_menu()
    pygame.display.flip()
    clock.tick(60)