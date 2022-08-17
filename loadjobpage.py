import tkinter as tk
from threading import Thread


class LoadJob(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        self.status = controller.status

        job_name_label = tk.Label(self, text="Job Name:")
        status_label = tk.Label(self, text="Status:")
        label_count_label = tk.Label(self, text="Label Count:")
        pass_sector_label = tk.Label(self, text="Passed Sectors:")
        fail_sector_label = tk.Label(self, text="Failed Sectors:")
        current_job_label = tk.Label(self, text="Current Job:")

        job_name_text_box = tk.Entry(self, width=20)

        self.status_info_box = tk.Label(self, text="Pending")
        self.job_info_box = tk.Label(self, text="-")
        self.label_count_info_box = tk.Label(self, text="-")
        self.pass_sectors_info_box = tk.Label(self, text="-")
        self.fail_sectors_info_box = tk.Label(self, text="-")

        job_name_label.grid(row=4, column=0, sticky='w', pady=2)
        job_name_text_box.grid(row=4, column=1, columnspan=2, pady=2)

        status_label.grid(row=1, column=0, sticky='w', pady=2)
        current_job_label.grid(row=1, column=3, sticky='w', pady=2)

        label_count_label.grid(row=3, column=0, sticky='w', pady=2)
        self.label_count_info_box.grid(row=3, column=1, columnspan=1, pady=2)
        pass_sector_label.grid(row=3, column=2, sticky='w', pady=2)
        self.pass_sectors_info_box.grid(row=3, column=3, columnspan=1, pady=2)
        fail_sector_label.grid(row=3, column=4, sticky='w', pady=2)
        self.fail_sectors_info_box.grid(row=3, column=5, columnspan=1, pady=2)

        self.status_info_box.grid(row=1, column=1, columnspan=1, pady=2)
        self.job_info_box.grid(row=1, column=4, columnspan=1, pady=2)

        load_button = tk.Button(self, text="Load",
                                command=lambda: self.controller.load_job(job_name_text_box.get()))
        load_button.grid(row=5, column=1, sticky='ew')

        unload_button = tk.Button(self, text="Unload",
                                  command=lambda: controller.unload_job())
        unload_button.grid(row=5, column=2, sticky='ew')

        run_button = tk.Button(self, text="Run",
                               command=lambda: controller.run_job())
        run_button.grid(row=6, column=1, sticky='ew')

        exit_button = tk.Button(self, text="Stop",
                                command=lambda: controller.stop_job())
        exit_button.grid(row=6, column=2, sticky='ew')

        exit_button = tk.Button(self, text="Exit",
                                command=lambda: controller.up_frame("WelcomePage"))
        exit_button.grid(row=7, column=2, sticky='ew')

        self.status_threading2()

    def change_text(self):
        # print("here")
        self.status_info_box.configure(text=self.controller.get_status())
        self.job_info_box.configure(text=self.controller.get_job_name())
        self.label_count_info_box.configure(text=self.controller.get_label_count())
        self.pass_sectors_info_box.configure(text=self.controller.get_pass_sector_count())
        self.fail_sectors_info_box.configure(text=self.controller.get_fail_sector_count())

    def status_threading2(self):
        # Call work function

        t = Thread(target=self.get_update)
        t.start()

    def get_update(self):
        while True:
            self.change_text()