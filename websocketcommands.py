from threading import Thread

import websocket


class ThreadRun2:
    def __init__(self, t):
        self.t = t

    def threading(self):
        # Call work function
        t1 = Thread(target=self.open_web_socket)
        t1.start()

    # def work(self):
    #     print("sleep time start")
    #     a = 0
    #     while 1:
    #         a = a + 1
    #         self.open_web_socket()

    def open_web_socket(self):
        print("here token " + self.t)
        # if controller.get_logged_in():
        if self.t:
            print("here web")
            ws = websocket.WebSocketApp(
                "ws://127.0.0.1:8081/api/printinspection/automation/v1/event/systemstatus?token=" + self.t,
                on_message=self.on_message,
                on_close=self.on_close,
                on_error=self.on_error

            )

            ws.run_forever()

    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        ws.close()
        print("### closed ###")
