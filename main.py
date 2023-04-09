from youtubesearchpython import *
from consolemenu import *
from consolemenu.items import *
import os
import json

def play_video(id_):
    os.system(f'mpv "https://youtu.be/{id_}"')

def videos_channel():
    pass

def channel_search():
    pass

def video_search():
    name = input("Video name: ")

    videos = VideosSearch(name)
    menu = ConsoleMenu("Select video", "Select video to play")

    for video in videos.result()["result"]:
        v = FunctionItem(f'{video["title"]} [{video["viewCount"]["short"]}] ({video["channel"]["name"]})', play_video, [video["id"]])
        menu.append_item(v)

    menu.show()


def main():
    menu = ConsoleMenu("Select", "Select type of search")

    search_video = FunctionItem("Video search", video_search)
    search_channel = FunctionItem("Channel search", channel_search)
    videos_in_channel = FunctionItem("Videos in channel", videos_channel)

    menu.append_item(search_video)
    menu.append_item(search_channel)
    menu.append_item(videos_in_channel)
    menu.show()

if __name__ == "__main__":
    main()