import pygame
import time
def play_file(name):
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        inp = input()
        clock.tick(1000)
        if inp == 'end':
            pygame.mixer.music.stop()
            # break
    

# def stop_m():
    # pygame.mixer.music.stop()  

def get_time():
    import datetime
    return datetime.datetime.now()

def filelog(nam):
    f = open(str(nam), "a")
    f.write("\nDone with the task " + " : " + str([str(get_time())]))
    f.close()

def activity_timer(fname, logf, stim):
    time.sleep(stim)
    filelog(logf)
    play_file(fname)
