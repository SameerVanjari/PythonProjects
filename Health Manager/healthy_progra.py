''' This program helps the programmer be healthy by reminding him of takingcare of himself 
    By making him drink 4 litres of water throughout his working hours i.e. 9-5
    then making him work his body by taking a break and getting him off his ass every 45 min
    and then making him give his eyes a rest from screen time every 30 min 
'''
import funxz
import time
from multiprocessing import Process

if __name__ == "__main__":
    print("Good Morning!\nWe will start your daily water,exercise and eye reminders.")
    fil = 'D:/practise/Healthy_programmer/Mirage_320(PaglaSongs).mp3'
    initial_time = time.time()
    drink = 30 
    eye = 60
    exer = 120
    tet = 0
    while True: 
        if tet >= 300:
            print('Over')
            exit()
        
        p1 = Process(target=funxz.activity_timer(fil,'sammer.txt', drink))
        p1.start()
        p2 = Process(target=funxz.activity_timer(fil, 'rajan.txt', eye))
        p2.start()
        p3 = Process(target=funxz.activity_timer(fil, 'amar.txt', exer))
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        
        
        tet = (time.time() - initial_time)
