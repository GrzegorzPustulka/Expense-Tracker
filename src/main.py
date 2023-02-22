import customtkinter
from MenuFrame import MenuFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("Dark")
        self.geometry("1200x800")
        self.minsize(600, 450)
        self.title("Expense Tracker")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0, minsize=int(self.winfo_screenwidth() * 0.1))

        self.grid_columnconfigure(1, weight=1)

        self.frame_menu = MenuFrame(master=self)
        self.frame_menu.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
