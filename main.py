#GUI_mouse1
from tkinter import *
class window_one:
    def __init__(self):
        Button(main_window,text="Quit",command=self.quit) .grid()
        canvas.bind("<Button-1>",self.oval)
    
    def quit(self):
        main_window.destroy()

    def oval(self,event):
        x_val = event.x
        y_val = event.y
        canvas.create_oval(x_val,y_val,x_val+20,y_val+20,fill="red",outline="blue",width=5)
        canvas.update()

main_window = Tk()
canvas = Canvas(main_window, width=400, height=300, bg='lightblue')
canvas.grid()
window_one()

