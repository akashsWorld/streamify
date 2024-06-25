from celery import shared_task
import os
from .models import Video


@shared_task
def process_video(video_name, channel_id, extension):
    exists = os.path.exists('./files/processed/video_name')
    if exists:
        # directory_name = 'New'
        # path = os.path.join('./process/', directory_name)
        # os.mkdir(path)
        # TODO: Implement the functionality to convert the video.
        process = os.system('dr')
        # exit_code = process.
        print(process)
        print("Hello World")
