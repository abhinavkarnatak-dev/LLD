from typing import List

class Video:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

class YoutubePlaylist:
    def __init__(self):
        self._videos: List[Video] = []

    def add_video(self, video: Video):
        self._videos.append(video)

    def get_videos(self):
        return self._videos

playlist = YoutubePlaylist()
playlist.add_video(Video("How to book a train ticket"))
playlist.add_video(Video("How to book a flight ticket"))
videos = playlist.get_videos()
for video in videos:
    print(video.get_title())