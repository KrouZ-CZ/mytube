#! /usr/bin/env python3


from youtubesearchpython import *
from consolemenu import *
from consolemenu.items import *
import os
import json

def play_video(id_):
    os.system(f'mpv "https://youtu.be/{id_}"')

def videos_channel(nid):
    videos_in_ch = ChannelSearch(*nid)
    menu = ConsoleMenu("Select video", "Select video to play")

    for video in videos_in_ch.result()['result']:
        if video["type"] != "video": continue
        v = FunctionItem(f'{video["title"]} [{video["views"]["simple"]}]', play_video, [video["id"]])
        menu.append_item(v)

    menu.show()

def channel_search():
    name = input("Channel name: ")

    channels = ChannelsSearch(name)
    menu = ConsoleMenu("Select channel", "Select channel in list")

    for channel in channels.result()["result"]:
        v = FunctionItem(f'{channel["title"]} {channel["subscribers"]}', videos_channel, [[channel["title"], channel["id"]]])
        menu.append_item(v)

    menu.show()


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

    menu.append_item(search_video)
    menu.append_item(search_channel)
    menu.show()

if __name__ == "__main__":
    main()