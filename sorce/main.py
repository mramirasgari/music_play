from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox
window=Tk()
mixer.init()
window.geometry('300x300')
window.title('Python Music Player')

def help_me():
    tkinter.messagebox.showinfo('Help','Howcan i help you')

def borowse_file():
    global filename
    filename=filedialog.askopenfilename()

menubar=Menu(window)
sunmenu=Menu(menubar,tearoff=0)
window.config(menu=menubar)
menubar.add_cascade(label='File',menu=sunmenu)
sunmenu.add_command(label='Open',command=borowse_file)
sunmenu.add_command(label='Exit',command=window.destroy)
sunmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='About Us',menu=sunmenu)
textLabel=Label(window,text='This is play Button')
textLabel.pack()

def play_music():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']='Music is playing'
        except:
            tkinter.messagebox.showerror('File Error','File Not Found')
    else:
        mixer.music.unpause()
        statusbar['text'] = 'Music is resumed'


def stop_music():
    mixer.music.stop()
    statusbar['text'] = 'Music is stopped'

def set_volume(value):
    volume=int(value)/100
    mixer.music.set_volume(volume)

def pause_music():
    global paused
    paused=True
    mixer.music.pause()
    statusbar['text'] = 'Music is paused'

def rewind_music():
    play_music()
    statusbar['text'] = 'Music is rewinded'


frame=Frame(window)
frame.pack(padx=10,pady=10)
photo=PhotoImage(file='../image/play.png')
playButton=Button(frame,image=photo,command=play_music)
playButton.grid(row=0,column=0,padx=10)

stopphoto=PhotoImage(file='../image/stop.png')
stopButton=Button(frame,image=stopphoto,command=stop_music)
stopButton.grid(row=0,column=2,padx=10)

pausePhoto=PhotoImage(file='../image/pause.png')
pausebtn=Button(frame,image=pausePhoto,command=pause_music)
pausebtn.grid(row=0,column=1,padx=10)
bottomframe=Frame(window)
bottomframe.pack()
rewindphoto=PhotoImage(file='../image/rewind.png')
rewindButton=Button(bottomframe,image=rewindphoto,command=rewind_music)
rewindButton.grid(row=1,column=1,padx=10)
scale=Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,command=set_volume)
scale.set(70)
scale.grid(row=0,column=1)
statusbar=Label(window,text="Keep enjoying the music",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)
window.mainloop()
