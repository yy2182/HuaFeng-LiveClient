import tkinter as tk
import vlc
import utils

class VideoPlayer:
    def __init__(self, video_url):
        self.root = tk.Tk()
        self.video_url = video_url
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(video_url)
        self.player.set_media(self.media)

        self.create_ui()

    def create_ui(self):
        video_size = utils.getVideoSize(self.video_url)
        if video_size:
            width, height = video_size
            self.root.geometry(f"{width}x{height}")
        else:
            self.root.geometry("800x600")

        self.root.title("Video Player")
        self.video_panel = tk.Frame(self.root)
        self.video_panel.pack(fill=tk.BOTH, expand=1)
        self.player.set_hwnd(self.video_panel.winfo_id())

        self.play_button = tk.Button(self.root, text="Play", command=self.play_video)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_video)
        self.stop_button.pack(side=tk.LEFT)

    def play_video(self):
        self.player.play()

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    video_url = "http://example.com/video.m3u8"  # 替换为实际的视频 URL
    player = VideoPlayer(video_url)
    player.run()

