from youtubesearchpython.__future__ import VideosSearch

from youtube_dl import YoutubeDL
import os
import asyncio

#make new directory for the downloads
current_directory = os.getcwd()
new_directory = "My_Music"
new_directory_path = os.path.join(current_directory,new_directory)
try:
    os.mkdir(new_directory_path)
except:
    pass
finally:
    audio_downloader = YoutubeDL({
        """
        for original format:
        'outtmpl': new_directory_path + '/%(title)s.%(ext)s'
        """
        #for mp3 format:
        'outtmpl': new_directory_path + '/%(title)s.mp3',
        'format' : 'bestaudio'
    })



URLs = []

def get_input():
    print("Enter the name of the song which you want to download!")
    print("If you want to quit, just press enter.")
    return input()

def search_for_music(name_of_song):
    return VideosSearch(name_of_song, limit = 10)

async def display_music(videosSearch):
    videosResult = await videosSearch.next()

    index = 1
    for video in videosResult['result']:
        print(str(index) + ". " + video['title'])
        URLs.append(video['link'])
        index += 1

def select_song():
    print("Which video do you want to download?(enter just the number)")
    print("Enter 0 for other results.")
    print("Press enter to go back.")
    return input()

def download_sound(number_of_song):
    audio_downloader.extract_info(URLs[number_of_song-1])

async def main():
    while True:
        number_of_song  = "0"

        #asks the user the name of the video
        name_of_song = get_input()

        if name_of_song == "": #exit condition
            break

        #an object which is searching
        videosSearch = search_for_music(name_of_song)

        while number_of_song == "0":
            #start a new list of URLs
            URLs.clear()

            #displays the next 10 results of the search
            await display_music(videosSearch)

            #the user selects the number of the video
            number_of_song = select_song()

        #does not download anything
        if number_of_song == "":
            continue

        number_of_song = int(number_of_song)

        #the video is downloaded
        try:
            download_sound(number_of_song)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    asyncio.run(main())
