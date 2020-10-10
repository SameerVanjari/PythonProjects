# from multiprocessing import Process

# def asdda(no , opp):
#     print (no + opp)


# if __name__ == "__main__":
#     p1 = Process(target=asdda(2, 4))
#     p1.start()
#     p2 = Process(target=asdda(1, 3))
#     p2.start()
#     p1.join()
#     p2.join()
import time 
print("start this shit0")

def readers():
    lin = "this is a line that goes in the coroutine to reads and acheck if the input is in line"
    time.sleep(5)

    while True:
        text = (yield)
        if text in lin:
            print("we found it")
        else:
            print("not found")

ref = readers()
next(ref)
ref.send("samer")
input("press something")
ref.send("line")