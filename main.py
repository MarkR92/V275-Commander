import requests
from requests.auth import HTTPBasicAuth
import websocket

from tkinter import *

root = Tk()

jobName = "test"
token = ""


def login(username, password):
    response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/security/login',
                            auth=HTTPBasicAuth(username, password))
    global token
    token = response.headers.get('Authorization')
    print(response.status_code)
    open_web_socket()


def logout():
    headers = {
        'Authorization': token,
        'Content-Type': 'text/plain'

    }
    response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/security/logout',
                            headers=headers)
    print(response.status_code)


def on_message(message):
    print(message)


def open_web_socket():
    # websocket.enableTrace(True)
    # ws = websocket.WebSocket()
    # ws.connect("ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token=+token" + token)
    ws = websocket.WebSocketApp(
        "ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token=" + token,
        on_message=on_message
    )

    ws.run_forever()


def load_job(job_name):
    headers = {
        'Authorization': token,
        'Content-Type': 'text/plain'

    }
    response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/job/load',

                            data=job_name,
                            headers=headers

                            )

    print(response.status_code)


def unload_job():
    headers = {
        'Authorization': token,
        'Content-Type': 'text/plain'

    }
    response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/job/unload',
                            headers=headers)
    print(response.status_code)


# open_web_socket()
# load_job(jobName)
# time.sleep(10)
# unload_job()
# logout()


def login_click():
    login("admin", "admin")


def logout_click():
    logout()


def load_job_click():
    load_job(jobName)


def unload_job_click():
    unload_job()


myLoginButton = Button(root, text="Login", command=login_click)
myLoginButton.pack()

myLogoutButton = Button(root, text="Logout", command=logout_click)
myLogoutButton.pack()

myLoadJobButton = Button(root, text="LoadJob", command=load_job_click)
myLoadJobButton.pack()

myUnLoadJobButton = Button(root, text="UnloadJob", command=unload_job_click)
myUnLoadJobButton.pack()

root.mainloop()
