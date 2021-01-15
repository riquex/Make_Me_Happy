import tkinter as tk
import pygame as pg
from PIL import Image, ImageTk

class Preview(tk.Frame):
    def __init__(self, master, width=300, height=300, *args, **kwds):
        super().__init__(master, width=300, height=300, *args, **kwds)
        
        size = 300, 300
        self.pg_screen = pg.display.set_mode(size, pg.RESIZABLE|pg.HIDDEN)#|pg.OPENGL|pg.DOUBLEBUF)
        self.pg_screen.fill(pg.Color(0, 0, 0))
        master.update()

        pg.display.init()
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.kill = False

    def screen_update(self, *args, **kwds):
        self.pg_screen.fill(pg.Color(255, 0, 0))

    def get_frame(self):
        self.img = pg.surfarray.array3d(pg.transform.rotate(self.pg_screen, -90))
        self.img_tk = ImageTk.PhotoImage(image=Image.fromarray(self.img))
        return self.img_tk

    def resize(self, width, height):
        self.pg_screen = pg.display.set_mode((width,height), pg.RESIZABLE|pg.HIDDEN)

    def update(self):
        self.canvas.create_image(0, 0, anchor='nw', image=self.get_frame())
        self.screen_update()

        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                self.pg_screen = pg.display.set_mode((event.w,event.h), pg.RESIZABLE|pg.HIDDEN)
        
        if self.kill == True:
            pg.display.quit()
            return

        pg.display.flip()
        #pg.display.update()
        #self.after(1, self.update)
