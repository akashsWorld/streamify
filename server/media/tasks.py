from celery import shared_task
import os
import time


@shared_task
def some_task(param):
    exists = os.path.exists('./files')
    if exists:
        # directory_name = 'New'
        # path = os.path.join('./process/', directory_name)
        # os.mkdir(path)
        time.sleep(12)
        print("Hello World")
