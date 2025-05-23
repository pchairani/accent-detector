import os
import uuid
from moviepy.video.io.VideoFileClip import VideoFileClip
import yt_dlp

def download_and_extract_audio(video_url):
    try:
        video_id = str(uuid.uuid4())
        video_path = f"{video_id}.mp4"
        audio_path = f"{video_id}.wav"

        ydl_opts = {'outtmpl': video_path}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path)
        clip.close()
        os.remove(video_path)

        return audio_path

    except Exception as e:
        print(f"Error during audio extraction: {e}")
        return None
