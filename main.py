import customtkinter
import tkinter
import pandas as pd
import openpyxl


class CustomRightFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.kind_label = customtkinter.CTkLabel(self, text="Kind")
        self.kind_label.grid(row=0, column=0, padx=10, pady=10)

        self.radio_var = tkinter.StringVar()
        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="FOOD",
                                                          variable=self.radio_var, value="FOOD")
        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="DRINK",
                                                          variable=self.radio_var, value="DRINK")
        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="CITY",
                                                          variable=self.radio_var, value="CITY")
        self.radiobutton_4 = customtkinter.CTkRadioButton(self, text="Fixed",
                                                          variable=self.radio_var, value="Fixed")
        self.radiobutton_5 = customtkinter.CTkRadioButton(self, text="Additional",
                                                          variable=self.radio_var, value="Additional")

        self.radiobutton_1.grid(row=0, column=1, padx=10, pady=10)
        self.radiobutton_2.grid(row=0, column=2, padx=10, pady=10)
        self.radiobutton_3.grid(row=0, column=3, padx=10, pady=10)
        self.radiobutton_4.grid(row=0, column=4, padx=10, pady=10)
        self.radiobutton_5.grid(row=0, column=5, padx=10, pady=10)

        self.product_label = customtkinter.CTkLabel(self, text="Product")
        self.product_label.grid(row=1, column=0, padx=10, pady=10)
        self.product_entry = customtkinter.CTkEntry(self,
                                                    placeholder_text="name",
                                                    width=120,
                                                    height=25,
                                                    border_width=2,
                                                    corner_radius=10)
        self.product_entry.grid(row=1, column=1, padx=10, pady=10)

        self.price_label = customtkinter.CTkLabel(self, text="Price")
        self.price_label.grid(row=2, column=0, padx=10, pady=10)
        self.price_entry = customtkinter.CTkEntry(self,
                                                  width=120,
                                                  height=25,
                                                  border_width=2,
                                                  corner_radius=10)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.count_label = customtkinter.CTkLabel(self, text="Count")
        self.count_label.grid(row=3, column=0, padx=10, pady=10)
        self.count_entry = customtkinter.CTkEntry(self,
                                                  width=120,
                                                  height=25,
                                                  border_width=2,
                                                  corner_radius=10)
        self.count_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Add", command=self.add_click)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

    def add_click(self):
        price = float(self.price_entry.get())
        count = float(self.count_entry.get())
        total_price = price * count

        self.price_entry.delete(0, "end")
        self.count_entry.delete(0, "end")

        info_label = customtkinter.CTkLabel(self, text='Added successfully')
        info_label.grid(row=5, column=0, padx=10, pady=10)

        total_price_label = customtkinter.CTkLabel(self, text=f'Total price: {total_price}')
        total_price_label.grid(row=6, column=0, padx=10, pady=10)

        data = {'TYPE': [self.radio_var.get()],
                'NAME': [self.product_entry.get()],
                'PRICE': [price], 'count': [count],
                'SUM': [total_price]}
        df = pd.DataFrame(data)

        try:
            existing_data = pd.read_excel('data.xlsx', sheet_name='data')
            df = pd.concat([existing_data, df], ignore_index=True)
            with pd.ExcelWriter('data.xlsx', mode='a', if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name='data', index=False)
        except FileNotFoundError:
            with pd.ExcelWriter('data.xlsx') as writer:
                df.to_excel(writer, sheet_name='data', index=False)


class FrameMenu(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.right_frame = None
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
        print("button click")

    def insert_click(self):
        self.right_frame = CustomRightFrame(self.master)
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def graph_click(self):
        print("button click")

    def contact_click(self):
        print("button click")

    def exit_click(self):
        print("button click")


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

        self.frame_menu = FrameMenu(master=self)
        self.frame_menu.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
