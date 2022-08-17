import tkinter as tk


class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.state = tk.DISABLED

        frame1 = tk.Frame(self, bg="red", padx=15, pady=15)

        # Displaying the frame1 in row 0 and column 0
        frame1.grid(row=1, column=0)

        label = tk.Label(self, text="AIS_logo\n",
                         font=controller.title_font)
        label.grid(row=1, column=1, columnspan=1, sticky='n', pady=2)

        login_button = tk.Button(self, text="Login",
                                 command=lambda: self.login())

        login_button.grid(row=2, column=1, sticky='e', pady=2)

        self.logout_button = tk.Button(self, text="Logout", state=self.state,
                                       command=lambda: self.logout())

        self.logout_button.grid(row=2, column=2, sticky='e', pady=2)

        settings_button = tk.Button(self, text="Settings",
                                    command=lambda: controller.up_frame("Settings"))

        settings_button.grid(row=2, column=3, sticky='e', pady=2)

    def login(self):
        self.controller.up_frame("Login")

    def logout(self):
        self.controller.logout()