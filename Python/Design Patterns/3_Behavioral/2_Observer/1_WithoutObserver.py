class YoutubeChannel:
    def upload_new_video(self, video_title):
        print(f"Uploading: {video_title}")

        # Manually Notify Users
        print("Sending email to user1@example.com")
        print("Pushing in-app notification to user3@example.com")

youtube_channel = YoutubeChannel()
youtube_channel.upload_new_video("Test Video 1")