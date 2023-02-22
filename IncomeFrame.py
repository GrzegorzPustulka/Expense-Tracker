import customtkinter
import tkinter
import pandas as pd


class IncomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.type = customtkinter.CTkLabel(self, text="Income", font=("oblique", 30))
        self.type.grid(row=0, column=3, padx=10, pady=10)
        self.kind_label = customtkinter.CTkLabel(self, text="Income")
        self.kind_label.grid(row=1, column=0, padx=10, pady=10)

        self.radio_var = tkinter.StringVar()
        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="Additional",
                                                          variable=self.radio_var, value="Additional")
        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="Work",
                                                          variable=self.radio_var, value="Work")
        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="Help",
                                                          variable=self.radio_var, value="Help")

        self.radiobutton_1.grid(row=1, column=1, padx=10, pady=10)
        self.radiobutton_2.grid(row=1, column=2, padx=10, pady=10)
        self.radiobutton_3.grid(row=1, column=3, padx=10, pady=10)

        self.price_label = customtkinter.CTkLabel(self, text="How Much")
        self.price_label.grid(row=2, column=0, padx=10, pady=10)
        self.price_entry = customtkinter.CTkEntry(self,
                                                  width=120,
                                                  height=25,
                                                  border_width=2,
                                                  corner_radius=10)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Add", command=self.add_click)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)

    def add_click(self):
        price = float(self.price_entry.get())

        info_label = customtkinter.CTkLabel(self, text='Added successfully')
        info_label.grid(row=4, column=0, padx=10, pady=10)

        total_price_label = customtkinter.CTkLabel(self, text=f'Total price: {price}')
        total_price_label.grid(row=5, column=0, padx=10, pady=10)

        data = {'TYPE': [self.radio_var.get()],
                'PRICE': [price]}
        df = pd.DataFrame(data)

        try:
            existing_data = pd.read_excel('income.xlsx', sheet_name='data')
            df = pd.concat([existing_data, df], ignore_index=True)
            with pd.ExcelWriter('income.xlsx', mode='a', if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name='data', index=False)
        except FileNotFoundError:
            with pd.ExcelWriter('income.xlsx') as writer:
                df.to_excel(writer, sheet_name='data', index=False)

        self.price_entry.delete(0, "end")
