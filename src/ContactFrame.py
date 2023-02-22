import customtkinter


class ContactFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.github_label = customtkinter.CTkLabel(self, text=f'GITHUB: https://github.com/GrzegorzPustulka',
                                                   font=("Arial", 30))
        self.github_label.grid(row=0, column=0, padx=10, pady=10)

        self.linkedin_label = customtkinter.CTkLabel(self,
                                                     text=f'LINKEDIN: https://www.linkedin.com/in/grzegorzpustulka/',
                                                     font=("Arial", 30))
        self.linkedin_label.grid(row=1, column=0, padx=10, pady=10)

        self.email_label = customtkinter.CTkLabel(self, text=f'EMAIL: kontakt.pustulka@gmail.com',
                                                  font=("Arial", 30))
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
