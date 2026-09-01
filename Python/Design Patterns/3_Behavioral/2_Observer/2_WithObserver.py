from abc import ABC, abstractmethod
from typing import List
import weakref

# Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, video_title):
        # Each subscriber decides how it wants to react
        raise NotImplementedError

# Concrete Observer: Email
class EmailSubscriber(Subscriber):
    def __init__(self, email):
        self.email = email

    def update(self, video_title):
        print(f"Email sent to {self.email}: New video uploaded - {video_title}")

class MobileAppSubscriber(Subscriber):
    def __init__(self, username):
        self.username = username

    def update(self, video_title):
        print(f"In-app notification for {self.username}: New video - {video_title}")

# Subject Interface
class Channel(ABC):
    @abstractmethod
    def subscribe(self, subscriber: Subscriber):
        raise NotImplementedError

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        raise NotImplementedError

    @abstractmethod
    def notify_subscribers(self, video_title):
        raise NotImplementedError

# Concrete Subject: Youtube Channel
class YoutubeChannel(Channel):
    def __init__(self, channel_name):
        self.channel_name = channel_name

        # Store subscribers as weak references to reduce memory leak risk
        self._subscribers = weakref.WeakSet()

    def subscribe(self, subscriber: Subscriber):
        # Add the observer
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        # Remove the observer
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify_subscribers(self, video_title):
        # Notify every active subscriber
        for subscriber in list(self._subscribers):
            subscriber.update(video_title)

    def upload_video(self, video_title):
        print(f"{self.channel_name} uploaded: {video_title}")

        # Trigger notifications
        self.notify_subscribers(video_title)

# Create Youtube Channel
ziktor_gaming = YoutubeChannel("ZiKt0R Gaming")

# Create Subscribers (Observers)
mobile = MobileAppSubscriber("Abhinav")
email = EmailSubscriber("abhinav@example.com")

# Subscribe Observers To The Subject
ziktor_gaming.subscribe(mobile)
ziktor_gaming.subscribe(email)

# Upload Video And Notify All Observers
ziktor_gaming.upload_video("Vlog 1")