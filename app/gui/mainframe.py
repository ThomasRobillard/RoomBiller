# to do
# app/gui/mainframe.py

import tkinter as tk

from .start_page import StartPage
# from app.gui.split_main import SplitMain
# from app.gui.new_split import NewSplit

class BudgetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SplitWise")
        self.geometry("600x400")

        # Create container for frames
        # self.frames = {}
        # for F in (StartPage, SplitMain):
        #     frame = F(self)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(StartPage)

    def show_frame(self, context):
        '''Display the requested frame'''
        frame = self.frames[context]
        frame.tkraise()
