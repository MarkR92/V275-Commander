import json
import time
import tkinter as tk
from queue import Queue
from tkinter import font as tk_font, filedialog

from httpcommands import *
from updatelabels import *
from welcomepage import *
from loginpage import *
from loadjobpage import *
from settingspage import *


class MainFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tk_font.Font(family='Verdana', size=12,
                                       weight="bold", slant='roman')

        container = tk.Frame()
        container.grid(row=1, column=0, sticky='nsew')

        self.id = tk.StringVar()
        self.id.set("Test")
        self.listing = {}
        self.http = Commands()
        self.update = Updates()

        self.status = "Pending"
        self.job_name = "No Job Loaded"
        self.label_count = "-"
        self.pass_sectors = "-"
        self.fail_sectors = "-"

        for p in (WelcomePage, Login, LoadJob, Settings):
            page_name = p.__name__
            # self.changeText(LoadJob)
            frame = p(parent=container, controller=self)
            frame.grid(row=1, column=0, sticky='nsew')
            self.listing[page_name] = frame

        self.up_frame('WelcomePage')

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()

    # page.status_threading2()

    def login(self, username, password):

        self.http.login(username, password)

        if self.http.get_logged_in():

            q = Queue()

            t1 = Thread(target=self.http.open_web_socket, args=(q,))  # Producer Thread

           # time.sleep(1)

            t2 = Thread(target=self.get_message, args=(q,))  # Consumer Thread

            t1.start()
            t2.start()
            self.up_frame("LoadJob")
            self.state = tk.NORMAL

    def logout(self):
        self.http.logout()


    def get_message(self, in_q):

        while True:

           # print(self.http.get_message())
            time.sleep(1)
            data2 = in_q.get()

            print(data2)
            #in_q.task_done()
            print("after")
            # if json.loads(self.http.message):
            msg2 = json.loads(self.http.message)
            system_status = (msg2.get("systemStatus"))
            data = system_status.get("data")

            # print(data.get("state"))
            # if msg2["systemStatus"]["data"]["state"]:
            # print(msg2.get(["systemStatus"]["data"]["state"]))
            # self.status = data.get("state")
            self.set_status(data.get("state"))
            self.set_job_name(data.get("jobName"))
            self.set_label_count(data.get("totalRepeatCount"))
            self.set_pass_sector_count(data.get("totalPassSectorCount"))
            self.set_fail_sector_count(data.get("totalFailSectorCount"))
            #  self.get_state()
            print("after")

            # print(self.status)
            # print(self.job_name)
           # in_q.task_done()

    def set_status(self, data):
        self.status = data

    def get_status(self):
        return self.status

    def set_job_name(self, job_name):
        self.job_name = job_name

    def get_job_name(self):
        return self.job_name

    def set_label_count(self, info):
        self.label_count = info

    def get_label_count(self):
        return self.label_count

    def set_pass_sector_count(self, info):
        self.pass_sectors = info

    def get_pass_sector_count(self):
        return self.pass_sectors

    def set_fail_sector_count(self, info):
        self.fail_sectors = info

    def get_fail_sector_count(self):
        return self.fail_sectors

    def load_job(self, job_name):

        self.http.load_job(job_name)
        # time.sleep(2)
        self.http.match_data('100')
        self.http.read_config_file()

    def unload_job(self):
        self.http.unload_job()

    def run_job(self):
        self.http.run_job()

        self.http.start_sim()

    def stop_job(self):
        self.http.stop_job()

    def start_sim(self):
        self.http.start_sim()

    def stop_sim(self):
        self.http.start_sim()

    def get_info(self):
        self.http.get_status()

    # def threading(self, toke):
    #     # Call work function
    #     t1 = Thread(target=self.open_web_socket(toke))
    #     t1.start()
    #
    #
    # def open_web_socket(self, tokn):
    #     # if controller.get_logged_in():
    #
    #     if not token:
    #         ws = websocket.WebSocketApp(
    #             "ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token=" + tokn,
    #             on_message=on_message,
    #             on_close=on_close,
    #             on_error=on_error
    #
    #         )
    #
    #         ws.run_forever()


# class WebSocket:
#
#     def __init__(self):
#         # self.threading()
#         self.http = Commands
#
#     # Commands.get_token(self)
#
#     def threading(self):
#         # work()
#         # Call work function
#         # _thread.start_new_thread(Commands.open_web_socket(self), ())
#         # Commands.get_token(self)
#         t1 = Thread(target=self.work())
#         t1.start()
#
#     def work(self):
#         print("sleep time start")
#
#         for i in range(10):
#             print(i)
#             time.sleep(1)
#
#         print("sleep time stop")

# class ThreadRun:
#     def __init__(self, t):
#         self.t = t
#        # self.second = s
#     def threading(self):
#         # Call work function
#         t1 = Thread(target=self.open_web_socket)
#         t1.start()
#
#     # def work(self):
#     #     print("sleep time start")
#     #     a = 0
#     #     while 1:
#     #         a = a + 1
#     #         self.open_web_socket()
#
#     def open_web_socket(self):
#         print("here token " + self.t)
#         # if controller.get_logged_in():
#         if self.t:
#             print("here web")
#             ws = websocket.WebSocketApp(
#                 "ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token=" + self.t,
#                 on_message=self.on_message,
#                 on_close=self.on_close,
#                 on_error=self.on_error
#
#             )
#
#             ws.run_forever()
#
#     def on_message(self, ws, message):
#         print(message)
#
#     def on_error(self, ws, error):
#         print(error)
#
#     def on_close(self, ws, close_status_code, close_msg):
#         ws.close()
#         print("### closed ###")


# work function
# class WebSocket:
#     pass
# def work(self):
#     print("sleep time start")
#     a = 0
#     while 1:
#         a = a + 1
#         self.open_web_socket()
#         # time.sleep(1)
#     # for i in range(100):
#     #     print(i)
#     #     open_web_socket()
#     #     time.sleep(1)
#
#     print("sleep time stop")
#
# def open_web_socket(self):
#     print("here token " + token)
#     # if controller.get_logged_in():
#     if token:
#         print("here web")
#         ws = websocket.WebSocketApp(
#             "ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token=" + token,
#             on_message=on_message,
#             on_close=on_close,
#             on_error=on_error
#
#         )
#
#         ws.run_forever()


# Create Button


# def run_job():
#     headers = {
#         'Authorization': token,
#         'Content-Type': 'text/plain'
#
#     }
#     response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/start',
#                             headers=headers)
#     print(response.status_code)
#
#
# def stop_job():
#     headers = {
#         'Authorization': token,
#         'Content-Type': 'text/plain'
#
#     }
#     response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/stop',
#                             headers=headers)
#     print(response.status_code)
#
#
# def start_sim():
#     headers = {
#         'Authorization': token,
#         'Content-Type': 'text/plain'
#
#     }
#     response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/startsimprint',
#                             headers=headers)
#     print(response.status_code)
#
#
# def stop_sim():
#     headers = {
#         'Authorization': token,
#         'Content-Type': 'text/plain'
#
#     }
#     response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/stopsimprint',
#                             headers=headers)
#     print(response.status_code)


# async def on_message_async(self):
#   print("here")
#  url = "ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token="

# async with websockets.connect(url + self.get_token) as ws:
#    msg = await ws.recv()

#   print(msg)
#  msg2 = json.loads(msg)
# print(msg2["systemStatus"]["name"])


if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()
