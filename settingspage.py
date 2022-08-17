import tkinter as tk
from multiprocessing import Process
from tkinter import filedialog


def browse_to_file():
    # tk.mainloop().withdraw(self)
    # self.update()
   # t = filedialog.askopenfile(initialdir="Documents",
                              # title="Select a File",
                               #filetypes=(("Text files",
                                    #       "*.txt*"),
                                     #     ))
    # tk.mainloop().update(self)

    # self.select_file.configure(text=filename)
    print("h")


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.filename = ""

        ip_label = tk.Label(self, text="IP:")
        ip_text_box = tk.Entry(self, width=20)
        ip_text_box.insert(0, "127.0.0.1")

        ip_label.grid(row=1, column=0, sticky='w', pady=2)
        ip_text_box.grid(row=1, column=1, columnspan=2, pady=2)

        port_label = tk.Label(self, text="Port:")
        port_text_box = tk.Entry(self, width=20)
        port_text_box.insert(0, "8080")

        port_label.grid(row=2, column=0, sticky='w', pady=2)
        port_text_box.grid(row=2, column=1, columnspan=2, pady=2)

        confirm_button = tk.Button(self, text="Confirm",
                                   )
        confirm_button.grid(row=4, column=1, sticky='ew')

        exit_button = tk.Button(self, text="Exit",
                                command=lambda: controller.up_frame("WelcomePage"))
        exit_button.grid(row=4, column=2, sticky='ew')

        select_file_button = tk.Button(self, text="Select File",
                                       command=lambda: browse_to_file())
        select_file_button.grid(row=3, column=0, sticky='ew')

        self.select_file = tk.Entry(self, width=20)
        self.select_file.insert(0, self.filename)

        self.select_file.grid(row=3, column=1, columnspan=2, pady=2)

  #  def status_threading2(self):
        # Call work function

      #  t = Process(target=browse_to_file)
      #  t.start()
