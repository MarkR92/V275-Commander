import json
import time
from threading import Thread
import requests
import websocket
from requests.auth import HTTPBasicAuth


class Commands:

    def __init__(self):
        self.str = ""
        self.logged_in = False
        self.token = ""
        self.message = ""
        self.state = ""
        self.out=""

    def login(self, username, password):
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/security/login',
                                auth=HTTPBasicAuth(username, password))

        print(response.status_code)

        if response.status_code == 200:
            self.token = response.headers.get('Authorization')
            self.logged_in = True

    def get_token(self):
        print(self.token)
        return self.token

    def set_token(self, token):
        print(token)
        self.token = token

    def get_logged_in(self):
        print(self.logged_in)
        return self.logged_in

    def set_logged_in(self, logged_in):
        self.logged_in = logged_in

    def logout(self):
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/security/logout',

                                headers=headers

                                )

        print(response.status_code)

    def load_job(self, job_name):
        print(self.token)
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/job/load',

                                data=job_name,
                                headers=headers

                                )

        print(response.status_code)

    def unload_job(self):
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }

        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/job/unload',
                                headers=headers)
        print(response.status_code)

    def run_job(self):
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/start',
                                headers=headers)
        print(response.status_code)

    def stop_job(self):
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/stop',
                                headers=headers)
        print(response.status_code)

    def start_sim(self):
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/startsimprint',
                                headers=headers)
        print(response.status_code)

    def stop_sim(self):
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/run/stopsimprint',
                                headers=headers)
        print(response.status_code)

    def open_web_socket(self, out_q):
        print("here token " + self.token)
        # if controller.get_logged_in():
        if self.logged_in:
            print("here web")
            ws = websocket.WebSocketApp(
                "ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token=" + self.token,
                on_message=self.on_message,
                on_close=self.on_close,
                on_error=self.on_error,
                #on_open=on_open

            )

            out_q.put("a")
            out_q.put("b")
            out_q.put("c")

            #print(ws.header)
            ws.run_forever()

    def set_status(self, message):
        self.message = message
        # self.get_status()
        # print(self.message)

    def on_message(self, ws, message):
        # print(out_q)
       # print(ws.header)
        self.set_status(message)

    def get_message(self):

        # out_q.put("a")
        return self.message

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        ws.close()
        print("### closed ###")

    def match_data(self, data):
        headers = {
            'Authorization': self.token,
            'Content-Type': 'text/plain'

        }
        response = requests.put('http://127.0.0.1:8081/api/printinspection/automation/v1/job/sectors/OCV_1/matchtext',
                                data=data,
                                headers=headers
                                )
        print(response.status_code)
        print("match")

    def read_config_file(self):

        with open("C:/Users/MarkR/OneDrive/Documents/config.json") as json_file:
            file = json.load(json_file)
            data = file.get("info")
            data2 = data[0]
            print(data2["EXP"])
