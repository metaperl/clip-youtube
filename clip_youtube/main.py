
# importing the module 
from pytube import YouTube 

from traitlets.config import Application
import traitlets

from loguru import logger

class App(Application):

    aliases = {
        "download_folder": "App.download_folder",
        "url": "App.url"
    }

    download_folder = traitlets.Unicode(
        default_value=".",
        help="""
        The location that clips will be downloaded to.
        """,
    ).tag(config=True)

    url = traitlets.Unicode(
        default_value=None,
        help="""
        The URL of the Youtube video to download.
        """,
    ).tag(config=True)

    def start(self):
        yt = YouTube(self.url) 
        mp4files = yt.streams.filter(
            progressive=True,
            file_extension='mp4'
            )
        first = mp4files.order_by('resolution').desc().first()
        logger.debug(f"{first=}")
        first.download()

        logger.debug(f"{mp4files=}")
        # yt.set_filename('holidays')   
        # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
        # d_video.download(self.download_folder) 

        # # let the clipping being
        # from moviepy.editor import *

        # video = VideoFileClip("holidays.mp4").subclip(50,60)
        # video.write_videofile("holidays_edited.mp4",fps=25)

if __name__ == "__main__":
    App.launch_instance()
   




