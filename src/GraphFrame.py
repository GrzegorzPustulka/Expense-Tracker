import customtkinter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = None
        self.profit_sum_expenses = None
        self.profit_sum_expenses_label = None
        self.type_sum_expenses = None
        self.type_sum_expenses_label = None
        self.mean_expenses = None
        self.mean_expenses_label = None
        self.sum_expenses = None
        self.sum_expenses_label = None
        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="Expenditure per day", value=1,
                                                          command=self.graph_expenditure_per_day)
        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="Type of expenses", value=2,
                                                          command=self.graph_type_of_expenses)
        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="Type of incomes", value=3,
                                                          command=self.graph_type_of_incomes)
        self.radiobutton_4 = customtkinter.CTkRadioButton(self, text="Statics", value=4,
                                                          command=self.statics)

        self.radiobutton_1.grid(row=0, column=0, padx=20, pady=10)
        self.radiobutton_2.grid(row=0, column=1, padx=20, pady=10)
        self.radiobutton_3.grid(row=0, column=2, padx=20, pady=10)
        self.radiobutton_4.grid(row=0, column=3, padx=20, pady=10)

    def graph_expenditure_per_day(self):
        df = pd.read_excel("data.xlsx")
        df_grouped = df.groupby('DATE', as_index=False)['SUM'].sum()
        sns.set(rc={'figure.figsize': (11, 5)})
        sns.barplot(x='DATE', y='SUM', data=df_grouped).set(title='EXPENDITURE PER DAY')
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

        df = pd.read_excel("income.xlsx")
        type_sum = df.groupby('TYPE')['PRICE'].sum()
        plt.pie(x=type_sum.values, labels=type_sum.index, autopct='%1.1f%%')
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")
        plt.close()

    def statics(self):
        df_expenses = pd.read_excel("data.xlsx")
        df_expenses['DATE'] = pd.to_datetime(df_expenses['DATE'], format='%d.%m.%Y')
        num_days = df_expenses['DATE'].nunique()

        df_income = pd.read_excel("income.xlsx")

        self.sum_expenses_label = customtkinter.CTkLabel(self, text="Sum of expenses")
        self.sum_expenses_label.grid(row=1, column=0, padx=10, pady=10)
        self.sum_expenses = customtkinter.CTkLabel(self, text=f'{df_expenses["SUM"].sum()} zł')
        self.sum_expenses.grid(row=1, column=1, padx=10, pady=10)

        self.mean_expenses_label = customtkinter.CTkLabel(self, text="Mean of expenses per day")
        self.mean_expenses_label.grid(row=2, column=0, padx=10, pady=10)
        self.mean_expenses = customtkinter.CTkLabel(self, text=f'{round(df_expenses["SUM"].sum() / num_days,2)} zł')
        self.mean_expenses.grid(row=2, column=1, padx=10, pady=10)

        self.type_sum_expenses_label = customtkinter.CTkLabel(self, text="MEAN of expenses")
        self.type_sum_expenses_label.grid(row=3, column=0, padx=10, pady=10)
        self.type_sum_expenses = customtkinter.CTkLabel(self, text=f'{df_expenses.groupby("TYPE")["SUM"].sum()}')
        self.type_sum_expenses.grid(row=3, column=1, padx=10, pady=10)

        profit = df_income['PRICE'].sum() - df_expenses['SUM'].sum()
        self.profit_sum_expenses_label = customtkinter.CTkLabel(self, text="Profit")
        self.profit_sum_expenses_label.grid(row=4, column=0, padx=10, pady=10)
        self.profit_sum_expenses = customtkinter.CTkLabel(self, text=f'{profit} zł')
        self.profit_sum_expenses.grid(row=4, column=1, padx=10, pady=10)
