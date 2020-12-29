import tkinter
import cv2
import PIL.Image, PIL.ImageTk 
from functools import partial
import time
import imutils
import threading


stream  = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    # play the video 
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, anchor=tkinter.NW, image=frame)

    # blinking text for decision pending
    if flag:
        canvas.create_text(133, 36, fill="yellow", font="Times 25 bold", text="Decision Pending")
    flag = not flag

    print(f"You clicked PLay. Speed is {speed}")

def pending(decision):
    # 1. decision pending image 
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, ancho=tkinter.NW, image=frame)

    # 2. Wait 1 sec
    time.sleep(1)

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, ancho=tkinter.NW, image=frame)

    # 44. wait another 2s 
    time.sleep(2)

    # 5. display out/notout image
    if decision == 'out':
        decision_img = 'out.png'
    else : decision_img = 'not_out.png'

    frame = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, ancho=tkinter.NW, image=frame)
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")
    
def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is Not out")

# Set height and width of of the window
SET_WIDTH = 650 
SET_HEIGHT = 368 

window = tkinter.Tk()
window.title("Decision review kit")
welcome_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)#converting image to rgb
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)# setting up window
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(welcome_img))#setting up image
img_to_canvas = canvas.create_image(0,0, ancho=tkinter.NW, image=photo)
canvas.pack()

# buttons to manipulate the screen 
btn = tkinter.Button(window, text="<< Previious (Fast)", width= 50, command=partial(play, -5))
btn.pack()

btn = tkinter.Button(window, text="<< Previious (Slow)", width= 50, command=partial(play, -25))
btn.pack()


btn = tkinter.Button(window, text="Next (Slow) >>", width= 50, command=partial(play, 5))
btn.pack()

btn = tkinter.Button(window, text="Next (Fast) >>", width= 50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width= 50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width= 50, command=not_out)
btn.pack()

window.mainloop()