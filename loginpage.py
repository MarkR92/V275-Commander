import tkinter as tk


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        user_label = tk.Label(self, text="User Name:")
        user_text_box = tk.Entry(self, width=20)

        user_label.grid(row=1, column=0, sticky='w', pady=2)
        user_text_box.grid(row=1, column=1, columnspan=2, pady=2)

        pass_label = tk.Label(self, text="Password:")
        pass_text_box = tk.Entry(self, width=20)

        pass_label.grid(row=2, column=0, sticky='w', pady=2)
        pass_text_box.grid(row=2, column=1, columnspan=2, pady=2)

        confirm_button = tk.Button(self, text="Confirm",
                                   command=lambda: self.controller.login(user_text_box.get(),
                                                                         pass_text_box.get()))

        confirm_button.grid(row=3, column=1, sticky='ew')

        exit_button = tk.Button(self, text="Exit",
                                command=lambda: controller.up_frame("WelcomePage"))
        exit_button.grid(row=3, column=2, sticky='ew')