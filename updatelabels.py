import json
import time
from threading import Thread


class Updates:

    def __init__(self):
        self.status = ""
        self.message = ""

    def status_threading(self,message):
        # Call work function

        t2 = Thread(target=self.get_message(message))
        t2.start()

        # time.sleep(1)
        # self.status = self.http.get_status()
        # print(self.http.message)

    def get_message(self,message):
        while True:
            time.sleep(0.5)

            # if json.loads(self.http.message):
            msg2 = json.loads(message)
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

            # print(self.status)
            # print(self.job_name)

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
