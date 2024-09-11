# to do
# buttons to display
    # new split
    # select split (dropdown)
    # personal budget (add at a later time)
    # preferences (add at a later time)
    # help (add at a later time)
    # exit
import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="welcome").pack(pady=10)

        #nav
       # tk.Button(self, text="help", command=lambda: parent.show_frame(parent.frames[SplitMain])).pack()

