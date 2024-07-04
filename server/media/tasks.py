from celery import shared_task
import os
from .models import Video


@shared_task
def process_video(video_name, video_id, extension):
    temp_video = f'./files/videos/{video_name}{extension}'
    processed_path = f'./files/processed/'
    video_exists = os.path.exists(temp_video)
    processed_exits = os.path.exists(processed_path)
    if video_exists and processed_exits:
        output_path = os.path.join(processed_path, video_name)
        hls_path = output_path+'/index.m3u8'
        os.mkdir(output_path)

        ffmpeg_command = f'ffmpeg -i "{temp_video}" -codec:v libx264 -codec:a aac -hls_time 10 -hls_playlist_type vod -hls_segment_filename "{output_path}/segment%03d.ts" -start_number 0 "{hls_path}"'
        process = os.system(ffmpeg_command)
        exit_code = process
        if exit_code is 0:
            print('hello')
            video = Video.objects.filter(pk=video_id).get()
            video.upload_status = 'APR'
            video.save()


