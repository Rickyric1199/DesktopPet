import pyautogui
import random
from tkinter import *
import tkinter as tk
import tkinter.ttk
from os.path import abspath, dirname
x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
pet = ''
BASE_PATH = abspath(dirname(__file__))
impath = BASE_PATH + '\\images\\'
#transfer random no. to event


def do_nothing():
    pass
def do_exit():
    exit()


def pet_1():
    print('doing the red thing')
    global pet
    pet = '1'

def pet_2():
    print('doing the yellow thing')
    global pet
    pet = '2'

def pet_3():
    print('doing pet things')
    global pet
    pet = '3'

def clicked():
    print(f'clicked {selected.get()}')
    v = selected.get()
    if v == 0:
        do_nothing()
    elif v == 1:
        pet_1()
    elif v == 2:
        pet_2()
    elif v == 3:
        pet_3()
    else:
        print('an error occurred, the wrong value was recieved')


def GUI():

    global rad1, rad2, rad3, selected

    window = tk.Tk()
    window.title("Select Pet")
    selected = tk.IntVar()
    pet1  = PhotoImage(file = impath +'\\1idle.gif\\')
    pet2 = PhotoImage(file = impath +'\\2idle.gif\\')


    rad1 = tk.Radiobutton(window, text='Pet 1', image = pet1, value=1, variable=selected)
    rad2 = tk.Radiobutton(window, text='Pet 2', image = pet2, value=2, variable=selected)
    rad3 = tk.Radiobutton(window, text='Pet 3', value=3, variable=selected)
    
    button1 = tk.Button(window, text="Select", command=clicked)                    
    button2 = tk.Button(window, text="Quit", command=do_exit)
    button3 = tk.Button(window, text="Start", command = window.destroy)

    rad1.grid(column=0, row=0)
    rad2.grid(column=1, row=0)
    rad3.grid(column=2, row=0)
    button1.grid(column=6, row=0)
    button2.grid(column=6, row=1)
    button3.grid(column=6, row=2)

    window.mainloop()


rad1, rad2, rad3, selected = None, None, None, None
GUI()
#

def event(cycle,check,event_number,x):
    if event_number in idle_num:
      check = 0
      print('idle')
      window.after(400,update,cycle,check,event_number,x) #no. 1,2,3,4 = idle
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(100,update,cycle,check,event_number,x) #no. 5 = idle to sleep
    elif event_number in walk_left:
      check = 4
      print('walking towards left')
      window.after(100,update,cycle,check,event_number,x)#no. 6,7 = walk towards left
    elif event_number in walk_right:
      check = 5
      print('walking towards right')
      window.after(100,update,cycle,check,event_number,x)#no 8,9 = walk towards right
    elif event_number in sleep_num:
      check  = 2
      print('sleep')
      window.after(1000,update,cycle,check,event_number,x)#no. 10,11,12,13,15 = sleep
    elif event_number == 14:
      check = 3
      print('from sleep to idle')
      window.after(100,update,cycle,check,event_number,x)#no. 15 = sleep to idle
    #making gif work 
def gif_work(cycle,frames,event_number,first_num,last_num):
    if cycle < len(frames) -1:
        cycle+=1
    else:
        cycle = 0
        event_number = random.randrange(first_num,last_num+1,1)
    return cycle,event_number
    
def update(cycle,check,event_number,x):
    #idle
    if check ==0:
        frame = idle[cycle]
        cycle ,event_number = gif_work(cycle,idle,event_number,1,9)
      
     #idle to sleep
    elif check ==1:
        frame = idle_to_sleep[cycle]
        cycle ,event_number = gif_work(cycle,idle_to_sleep,event_number,10,10)
    #sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle ,event_number = gif_work(cycle,sleep,event_number,10,15)
    #sleep to idle
    elif check ==3:
        frame = sleep_to_idle[cycle]
        cycle ,event_number = gif_work(cycle,sleep_to_idle,event_number,1,1)
    #walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle , event_number = gif_work(cycle,walk_positive,event_number,1,9)
        x -= 3
    #walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle , event_number = gif_work(cycle,walk_negative,event_number,1,9)
        x -= -3
    window.geometry('100x100+'+str(x)+'+939')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_number,x)
        
window = tk.Tk()         
label = tk.Label(window,bd=0,bg='black')


 
#call buddy's action gif
idle = [tk.PhotoImage(file=impath+pet+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif
idle_to_sleep = [tk.PhotoImage(file=impath+pet+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif
sleep = [tk.PhotoImage(file=impath+pet+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif
sleep_to_idle = [tk.PhotoImage(file=impath+pet+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif
walk_positive = [tk.PhotoImage(file=impath+pet+'left.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
walk_negative = [tk.PhotoImage(file=impath+pet+'right.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif

#window configuration
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')
label.pack()

#loop the program
window.after(1,update,cycle,check,event_number,x)
window.mainloop()
