# importing packages
from pytube import YouTube
import os

def download_mp4(url, destination):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    out_file = video.download(output_path=destination)
    print(yt.title + " has been successfully downloaded as MP4.")

def download_mp3(url, destination):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded as MP3.")

# URL input from user
url = input("Enter the URL of the video you want to download: \n>> ").strip()

if not url:
    print("Invalid URL. Please input a proper URL link")
else:
    # Get the user's home directory and create a 'Downloads' subdirectory
    home_dir = os.path.expanduser("~")
    download_dir = os.path.join(home_dir, 'Downloads')

    # Menu for user to choose between MP3 and MP4 download
    print("Select download format:")
    print("1. MP4")
    print("2. MP3")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        download_mp4(url, download_dir)
    elif choice == '2':
        download_mp3(url, download_dir)
    else:
        print("Invalid choice. Please enter 1 for MP4 or 2 for MP3.")