from pygame import mixer
from pygame import mixer_music as mx
from os  import path,listdir,chdir
from tkinter import *
import tkinter.ttk as ttk
from tkinter.filedialog import  askdirectory,askopenfilename
from functools import partial
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
#data section
mixer.init()
music_file_types=['mp3','.aac','.waw']
def filterr(var):
    for i in var:
        if i[i.index('.'):]=='.mp3':
            pass
        else:
            var.remove(i)
    return var
class work_flow:
    def __init__(self):
        self.is_file_get=False
        self.listfile=None
        self.song_ptr=-1
        mixer.init()
        self.playing=False
    def get_dir(self,frame):
        dir=askdirectory()
        chdir(dir)
        path=listdir(dir)
        path=filterr(path)
        datas='\n'.join(path)
        self.is_file_get=True
        self.listfile=path
        l=Label(frame,text=datas,border=4)
        l.pack()
    def next_song(self):
        if self.is_file_get:
            self.song_ptr+=1
            if self.song_ptr==len(self.listfile)-1:
                showinfo(title='Info',message='End of list')
                self.song_ptr=0
            try:
                mx.stop()
            except Exception as e:
                pass
            data=mx.load(self.listfile[self.song_ptr])
            mx.play()
            self.playing=True
        else:
            showinfo(title="Directory not found",message='Directory is not set')

    def play(self):
        if self.is_file_get:
            if self.song_ptr==-1:
                self.next_song()
            elif self.playing:
                mx.pause()
                self.playing=False
            elif not self.playing:
                mx.unpause()
                self.playing=True
        else:
            showinfo(title="Directory not found",message='Directory is not set')

    def prev_song(self):
        if self.is_file_get:
            self.song_ptr-=1
            if self.song_ptr<0:
                showinfo(title='Info',message='First music of list')
                self.song_ptr=0
            try:
                mx.stop()
            except Exception as e:
                pass
            data=mx.load(self.listfile[self.song_ptr])
            mx.play()
            self.playing=True
        else:
            showinfo(title="Directory not found",message='Directory is not set')

#mainloop
app=Tk()
app.geometry("420x380")
app.title('Music player')
w=work_flow()
image=Image.open('own_profile.jpg')
image=image.resize((320,320))
defaultImage=ImageTk.PhotoImage(image)

file_frame=Frame(app,width=100,height=480,relief='raised')
file_frame.grid(row=0,column=0,sticky=NW)
file_open=Button(file_frame,text="Open music file",relief=GROOVE,command=partial(w.get_dir,file_frame))
file_open.pack()



player_frame=Frame(app,width=380,height=300)
player_frame.grid(row=0,column=1,sticky=W)
just_info=Label(player_frame,image=defaultImage,width=330,height=325)
just_info.pack(side=TOP)
# bar=ttk.LabeledScale(player_frame,to=100)

button_frame=Frame(app,width=480,height=100)
button_frame.grid(row=4,column=1)



button_prev=Button(button_frame,text='\t<\t',relief=RAISED,command=w.prev_song)
button_prev.grid(column=0,row=0)
button_pause_resume=Button(button_frame,text='\t| |\t',relief=RAISED,command=w.play)
button_pause_resume.grid(column=1,row=0)
button_next=Button(button_frame,text='\t>\t',relief=RAISED,command=w.next_song)
button_next.grid(column=2,row=0,pady=20,)
app.mainloop()
