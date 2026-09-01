from typing import List


class Video:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title


# Playlist Class (Aggregate)
class YoutubePlaylist:
    def __init__(self):
        self._videos: List[Video] = []

    def add_video(self, video):
        self._videos.append(video)

    def create_iterator(self):
        return YoutubePlaylistIterator(self._videos)


# Iterator Interface
class PlaylistIterator:
    def has_next(self):
        pass

    def next(self):
        pass


# Concrete Iterator Class
class YoutubePlaylistIterator(PlaylistIterator):
    def __init__(self, videos: List[Video]):
        # Store the reference to the list we iterate on
        self._videos = videos

        # Track current position
        self._position = 0

    # Check if more videos are left
    def has_next(self):
        return self._position < len(self._videos)

    # If no next element, return None
    def next(self):
        if not self.has_next():
            return None

        # Return current element and move forward
        video = self._videos[self._position]
        self._position += 1

        return video


# Client
playlist = YoutubePlaylist()

playlist.add_video(Video("How to book a train ticket"))
playlist.add_video(Video("How to book a flight ticket"))

iterator = playlist.create_iterator()

while iterator.has_next():
    video = iterator.next()

    if video is not None:
        print(video.get_title())