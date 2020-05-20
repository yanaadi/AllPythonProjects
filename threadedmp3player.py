#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

from tkinter import messagebox,filedialog

import pygame

from threading import Thread

class player:
    
    def __init__(self,win):
        
        pygame.init()
        
        pygame.display.init()
        
        pygame.mixer.init()
        
        self.win = win
        
        self.win.title('Mp3 Player')
        
        self.win.geometry('200x250')
        
        self.win.rowconfigure((0,1,2,3,4,5),weight=1)
        
        self.win.columnconfigure((0,1,2,3,4,5,6),weight=1)
        
        self.v = tk.StringVar()
        
        self.i = 0
        
        self.frm2 = tk.Frame(master = self.win, relief = tk.SUNKEN,borderwidth=5,width =60)
        
        self.frm1 = tk.Frame(master = self.win, relief = tk.SUNKEN,borderwidth = 5)
        
        self.but1 = tk.Button(master =self.frm2,relief = tk.RAISED,text = 'Play', fg = 'Black',bg = 'Grey',command = self.play,width=10)
        
        self.but2 = tk.Button(master=self.frm2,relief = tk.RAISED,text = 'Pause', fg = 'Black',bg = 'Grey',command = self.pause,width=10)
        
        self.but3 = tk.Button(master=self.frm2,relief = tk.RAISED,text = 'Resume', fg = 'Black',bg = 'Grey',command = self.resume,width=10)
        
        self.but5 = tk.Button(text = 'Open File',fg = 'Black',bg = 'Grey',command = self.openfile )
        
        self.lbl1 = tk.Label(master = self.frm1,textvariable = self.v,fg ='Black',width = 100)
        
        self.sld1 = tk.Scale(from_=0,to=1,resolution=0.1,command = self.volumeset)
        
        self.vol = self.sld1.get()
        
        self.but1.grid(row=5,column=0,padx = 3,pady=3)
        
        self.but2.grid(row=5,column=1,padx=3,pady =3)
        
        self.but3.grid(row=5,column=2,padx=3,pady=3)
        
        self.but5.grid(row=1,column=1)
        
        self.frm1.grid(row=1,column =0)
        
        self.frm2.grid()
        
        self.lbl1.grid()
        
        self.sld1.grid(row = 1, column = 6)
        
    def next_(self):
        
        running = True
        
        while running:
            
            if self.i <= len(dir_) - 1:
                
                for event in pygame.event.get():
                    
                    if event.type == pygame.USEREVENT:
                        
                        for _ in range(len(dir_[self.i])):
                            
                            if dir_[self.i][_] == '/' and '/' not in dir_[self.i][_+1:]:
                                
                                self.v.set('Now Playing  '+ dir_[self.i][_+1:])
                                
                        pygame.mixer.music.load(dir_[self.i])
                        
                        pygame.mixer.music.play()
                        
                        self.i+=1
            else:
                
                running = False
        
        
    def play(self):
        
        for j in range(len(dir_[self.i])):
            
            if dir_[self.i][j] == '/' and '/' not in dir_[self.i][j+1:]:
                
                self.v.set('Now Playing  '+ dir_[self.i][j+1:])
                    
        pygame.mixer.music.load(dir_[self.i])
            
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
            
        pygame.mixer.music.play()
            
        self.i+=1
            
        t = Thread(target = self.next_,args = ())
            
        t.start()
        
        
                    
            
    def msg_error(self):
        
        messagebox.showerror('Error','Invalid File Type Detected')
        
    def msg_valid(self):
        
        messagebox.showinfo('Info','All Files Added')
        
    def openfile(self):
        
        global dir_
        
        dir_ = list(filedialog.askopenfilenames())
        
        for songs in dir_:
            
            if bool(songs.endswith('.mp3')) == False:
                
                self.msg_error()
        else:
                
            self.msg_valid()
            
    def volumeset(self,vol1):
        
        pygame.mixer.music.set_volume(float(vol1))
                
    def pause(self):
        
        pygame.mixer.music.pause()
        
    def resume(self):
        
        pygame.mixer.music.unpause()
        
  

win = tk.Tk()                        

a = player(win)

win.mainloop()

