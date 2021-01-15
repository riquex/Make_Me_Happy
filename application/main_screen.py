from . import preview
import tkinter as tk
from queue import Queue
from threading import Thread

class Application(tk.Tk): 
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self.dead = False

        self.queue = Queue()

        self.setup_window()
        self.app_menu()
        self.toolbox()

        self.preview = preview.Preview(self)
        self.preview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.preview.update()

    def setup_window(self):
        self.title('Make Me Happy')

    def app_menu(self):
        self.menubar = tk.Menu(self)#{

        self.menubar_file = tk.Menu(self.menubar, tearoff=0)#{
        self.menubar_file.add_command(label='New Project', command=None)
        self.menubar_file.add_command(label='Open Project', command=None)
        self.menubar_file.add_separator()

        self.menubar_file.add_command(label='Export Project', command=None)
        self.menubar_file.add_separator()

        self.menubar_file.add_command(label='Exit', command=self.close)
        #   }

        self.menubar.add_cascade(label='File', menu=self.menubar_file)

        self.menubar_tools = tk.Menu(self.menubar, tearoff=0)#{
        self.menubar_tools.add_command(label='Insert Image', command=None)
        self.menubar_tools.add_command(label='Insert Rectangle', command=None)
        self.menubar_tools.add_command(label='Insert Arc', command=None)
        self.menubar_tools.add_command(label='Insert Elipse', command=None)
        self.menubar_tools.add_command(label='Insert Line', command=None)
        self.menubar_tools.add_command(label='Insert Polygon', command=None)
        
        self.menubar_tools.add_separator()
        self.menubar_tools.add_command(label='Insert Script', command=None)
        #   }

        self.menubar.add_cascade(label='tools', menu=self.menubar_tools)
        #}

        self.config(menu=self.menubar)
    
    def toolbox(self):
        self.toolframe = tk.Frame(self)
        self.toolframe.pack(fill=tk.X, expand=True, side=tk.LEFT)

        self.toolcanvas = tk.Canvas(self.toolframe)
        self.toolcanvas.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    def close(self):
        self.dead = True
        self.destroy()
        self.preview.kill = True
    def update_loop(self):
        self.update()
