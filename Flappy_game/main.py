import random #to generate random nos 
import os #to control the window functions 
import pygame
from pygame.locals import * #general setup import of pygame 

# GLOBAL VARIABLES
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'
highScore = 0 


def wishWelcome():
    """
    This is show the welcome screen of the game
    """
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0
    font = pygame.font.SysFont("comicsans", 48, True)

    while True:
        for event in pygame.event.get():
            # if user clicks the X mark to close
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if the User presses the UP key or Spacebar, Start Game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            
            # else show the message image
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
                text = font.render("Flappy Bird", 1, (225,0,0))
                text1 = font.render("Sam's", 1, (225,0,0))
                SCREEN.blit(text1, (40, 80))
                SCREEN.blit(text, (40,120))

                font1 = pygame.font.SysFont("Times", 28, True, True)
                text2 = font1.render("Tap here", 1, (200,0,0))
                SCREEN.blit(text2, (80,310))

                
                # SCREEN.blit(GAME_SPRITES['message'],(messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def flappyGame():
    score = 0
    playerx = int(SCREENWIDTH/5) 
    playery = int(SCREENHEIGHT/2)
    basex = 0

    #create pipes for blitting
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # upper pie list
    upperPipe = [
        {'x':SCREENWIDTH + 200, 'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y':newPipe2[0]['y']}
    ]
    # lower pie list
    lowerPipe = [
        {'x':SCREENWIDTH + 200, 'y':newPipe1[1]['y']},
        {'x':SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y':newPipe2[1]['y']}
    ]

    pipevelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipe, lowerPipe) # function will return true is player crashed
        if crashTest:
            return
        highScore = score

        #check score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2 
        for pipe in upperPipe:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos + 4 :
                score +=1 
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()
        

        
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY+= playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()    
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)


        # move pipes across screen 
        for upperpipe, lowerpipe in zip(upperPipe, lowerPipe):
            upperpipe['x'] += pipevelX
            lowerpipe['x'] += pipevelX
        
        # add pipes to upper and lower pipe lists when first ones are about to leave screen 
        if 0 < upperPipe[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipe.append(newPipe[0])
            lowerPipe.append(newPipe[1])
        
        #  if the first pipes are out of screen, remove it 
        if upperPipe[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipe.pop(0)
            lowerPipe.pop(0)

        # sprite blits from here
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperpipe , lowerpipe in zip(upperPipe, lowerPipe):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperpipe['x'], upperpipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerpipe['x'], lowerpipe['y']))
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        # score blit
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        # high score 
        high_score_font = pygame.font.SysFont("sans", 30, True)
        high_text = high_score_font.render(f"High score: {highScore}", 1, (0,0,225))
        SCREEN.blit(high_text, (120, 5))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    highScore = score



def isCollide(playerx, playery, upperPipe, lowerPipe):
    if playery > GROUNDY - 25 or playery <0 :
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipe:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    for pipe in lowerPipe:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    return False


def getRandomPipe():
    """
    Generate positions of two pipes( one at bottom and other at top ) for blitting on screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2*offset))
    pipeX = SCREENWIDTH + 10 
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1 },#upper pipe
        {'x': pipeX, 'y': y2} #lower pipe
    ]
    return pipe

if __name__ == "__main__":
    # this is where th)e game starts executing
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Sam's Flappy bird game")
    GAME_SPRITES['numbers']= (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    
    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha() 
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), pygame.image.load(PIPE).convert_alpha())
    
    #Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND)
    GAME_SPRITES['player'] = pygame.image.load(PLAYER)

    while True:
        wishWelcome()
        flappyGame()
