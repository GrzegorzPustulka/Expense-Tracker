import customtkinter
import pandas as pd


class DisplayFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        df = pd.read_excel("data.xlsx")
        headers = df.columns
        for j, header in enumerate(headers):
            label = customtkinter.CTkLabel(self, text=str(header), font=("Arial", 18), padx=5)
            label.grid(row=0, column=j)

        for i, row in enumerate(df.values):
            for j, value in enumerate(row):
                label = customtkinter.CTkLabel(self, text=str(value))
                label.grid(row=i+1, column=j, padx=15, pady=10)
