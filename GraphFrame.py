import customtkinter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="Expenditure per day", value=1,
                                                          command=self.graph_expenditure_per_day)
        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="Type of expenses", value=2,
                                                          command=self.graph_type_of_expenses)
        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="Type of incomes", value=3,
                                                          command=self.graph_type_of_incomes)
        self.radiobutton_4 = customtkinter.CTkRadioButton(self, text="Statics", value=4)

        self.radiobutton_1.grid(row=0, column=0, padx=20, pady=10)
        self.radiobutton_2.grid(row=0, column=1, padx=20, pady=10)
        self.radiobutton_3.grid(row=0, column=2, padx=20, pady=10)
        self.radiobutton_4.grid(row=0, column=3, padx=20, pady=10)

    def graph_expenditure_per_day(self):
        df = pd.read_excel("data.xlsx")
        df['DATE'] = pd.to_datetime(df['DATE'], format='%d.%m.%Y')
        df['DAY'] = df['DATE'].dt.date

        df_grouped = df.groupby('DAY', as_index=False).agg({'SUM': 'sum'})
        sns.set(rc={'figure.figsize': (11, 5)})
        sns.barplot(x='DAY', y='SUM', data=df_grouped).set(title='EXPENDITURE PER DAY')
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")
        plt.close()

    def graph_type_of_expenses(self):
        df = pd.read_excel("data.xlsx")
        type_sum = df.groupby('TYPE')['SUM'].sum()
        plt.pie(x=type_sum.values, labels=type_sum.index, autopct='%1.1f%%')
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")
        plt.close()

    def graph_type_of_incomes(self):
        pass