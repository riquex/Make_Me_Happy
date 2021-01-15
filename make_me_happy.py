import application as App
import os
import threading

def main():
    root = App.main_screen.Application()
    
    while not root.dead:
        root.update_loop()
        root.preview.update()
    
    return 0

if __name__ == '__main__':
    main()
