import customtkinter
import tkinter
import pandas as pd


class InsertFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.type = customtkinter.CTkLabel(self, text="Expenses", font=("Arial", 30))
        self.type.grid(row=0, column=3, padx=10, pady=10)

        self.kind_label = customtkinter.CTkLabel(self, text="Kind")
        self.kind_label.grid(row=1, column=0, padx=10, pady=10)

        self.radio_var = tkinter.StringVar()
        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="Food",
                                                          variable=self.radio_var, value="FOOD")
        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="Drink",
                                                          variable=self.radio_var, value="DRINK")
        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="Fast Food",
                                                          variable=self.radio_var, value="FAST FOOD")
        self.radiobutton_4 = customtkinter.CTkRadioButton(self, text="Energy drink",
                                                          variable=self.radio_var, value="ENERGY DRINK")
        self.radiobutton_5 = customtkinter.CTkRadioButton(self, text="Fixed",
                                                          variable=self.radio_var, value="FIXED")
        self.radiobutton_6 = customtkinter.CTkRadioButton(self, text="Additional",
                                                          variable=self.radio_var, value="ADDITIONAL")

        self.radiobutton_1.grid(row=1, column=1, padx=10, pady=10)
        self.radiobutton_2.grid(row=1, column=2, padx=10, pady=10)
        self.radiobutton_3.grid(row=1, column=3, padx=10, pady=10)
        self.radiobutton_4.grid(row=1, column=4, padx=10, pady=10)
        self.radiobutton_5.grid(row=1, column=5, padx=10, pady=10)
        self.radiobutton_6.grid(row=1, column=6, padx=10, pady=10)

        self.data_label = customtkinter.CTkLabel(self, text="Date")
        self.data_label.grid(row=2, column=0, padx=10, pady=10)
        self.data_entry = customtkinter.CTkEntry(self,
                                                 placeholder_text="DD.MM.YYYY",
                                                 width=120,
                                                 height=25,
                                                 border_width=2,
                                                 corner_radius=10)
        self.data_entry.grid(row=2, column=1, padx=10, pady=10)

        self.product_label = customtkinter.CTkLabel(self, text="Product")
        self.product_label.grid(row=3, column=0, padx=10, pady=10)
        self.product_entry = customtkinter.CTkEntry(self,
                                                    placeholder_text="name",
                                                    width=120,
                                                    height=25,
                                                    border_width=2,
                                                    corner_radius=10)
        self.product_entry.grid(row=3, column=1, padx=10, pady=10)

        self.price_label = customtkinter.CTkLabel(self, text="Price")
        self.price_label.grid(row=4, column=0, padx=10, pady=10)
        self.price_entry = customtkinter.CTkEntry(self,
                                                  width=120,
                                                  height=25,
                                                  border_width=2,
                                                  corner_radius=10)
        self.price_entry.grid(row=4, column=1, padx=10, pady=10)

        self.count_label = customtkinter.CTkLabel(self, text="Count")
        self.count_label.grid(row=5, column=0, padx=10, pady=10)
        self.count_entry = customtkinter.CTkEntry(self,
                                                  width=120,
                                                  height=25,
                                                  border_width=2,
                                                  corner_radius=10)
        self.count_entry.grid(row=5, column=1, padx=10, pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Add", command=self.add_click)
        self.add_button.grid(row=6, column=0, padx=10, pady=10)

    def add_click(self):
        price = float(self.price_entry.get())
        count = float(self.count_entry.get())
        total_price = price * count

        info_label = customtkinter.CTkLabel(self, text='Added successfully')
        info_label.grid(row=7, column=0, padx=10, pady=10)

        total_price_label = customtkinter.CTkLabel(self, text=f'Total price: {total_price}')
        total_price_label.grid(row=8, column=0, padx=10, pady=10)

        data = {'DATE': [self.data_entry.get()],
                'TYPE': [self.radio_var.get()],
                'NAME': [self.product_entry.get()],
                'PRICE': [price],
                'COUNT': [count],
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

        self.price_entry.delete(0, "end")
        self.count_entry.delete(0, "end")
