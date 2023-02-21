import customtkinter
import tkinter
from InsertFrame import InsertFrame
from DisplayFrame import DisplayFrame


class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.display_frame = None
        self.insert_frame = None

        self.display = customtkinter.CTkButton(self, text="Display", command=self.display_click)
        self.display.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.insert = customtkinter.CTkButton(self, text="Insert", command=self.insert_click)
        self.insert.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.graph = customtkinter.CTkButton(self, text="Graph", command=self.graph_click)
        self.graph.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.contact = customtkinter.CTkButton(self, text="Contact", command=self.contact_click)
        self.contact.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.exit = customtkinter.CTkButton(self, text="exit", command=self.exit_click)
        self.exit.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def display_click(self):
        self.grid_rowconfigure(0, weight=1)
        self.display_frame = DisplayFrame(self.master)
        self.display_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def insert_click(self):
        self.insert_frame = InsertFrame(self.master)
        self.insert_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def graph_click(self):
        print("button click")

    def contact_click(self):
        print("button click")

    def exit_click(self):
        print("button click")
